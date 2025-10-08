# need to start a child process and send info to it via stdin

import subprocess
import json

from utils.messages import list_tools_message, initialize_message, initialized_message

# Start the child process
proc = subprocess.Popen(
    ['python3', 'server.py'],  # Replace with your child script
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

message = 'hello\n'

def send_message(message):
    """Send a message to the child process."""
    print_response(message, prefix='[CLIENT]: ')
    proc.stdin.write(message)
    proc.stdin.flush()

def serialize_message(message):
    """Serialize a message to JSON format."""
    return json.dumps(message) + '\n'

def print_response(response, prefix = ""):
    """Print the response from the server."""
    try:
        parsed = json.loads(response)
        print(prefix,json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        print(prefix, response.strip())

def connect():
    print("Connecting to the server...")
    # 1. Ask for capabilities
    send_message(serialize_message(initialize_message))

    # Read response from child
    response = proc.stdout.readline()
    print_response(response, prefix='[SERVER]: \n')    

    # 2. Send initialized notification
    send_message(serialize_message(initialized_message))

def send_simple_message(message):
    # Send a simple text message to the child
    send_message(message)

    response = proc.stdout.readline()
    print_response(response, prefix='[SERVER]: \n')  

def list_tools():
    # 3. send a message to list tools
    # send a JSON-RPC message
    send_message(serialize_message(list_tools_message))

    has_result = False
    while not has_result:
        response = proc.stdout.readline()
        # check if message has result attribute, if so break out of loop
        
        parsed_response = json.loads(response)
        if 'result' in parsed_response:
            has_result = True
            return parsed_response['result']['tools']
        else:
            # this is a notification, we can print it
            print_response(response, prefix='[SERVER] notification: \n')

def call_tool(tool_name, args):
    # 4. call a tool
    # send a JSON-RPC message

    tool_message = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "args": args
        },
        "id": 1
    }

    has_result = False
    send_message(serialize_message(tool_message))

    while not has_result:
        response = proc.stdout.readline()
        parsed_response = json.loads(response)
        if 'result' in parsed_response:
            has_result = True
            return parsed_response["result"]["properties"]["content"]["items"]
        else:
            # this is a notification, we can print it
            print_response(response, prefix='[SERVER] notification: \n')

def close_server():
    send_message('exit\n')

    exit_code = proc.wait()
    print(f"Child exited with code {exit_code}")

tools = []

def main():
    connect()
    tool_response = list_tools() 
    tools.extend(tool_response)
    
    print("Tools available:", tools)

    tool = tools[0]

    tool_call_response = call_tool(tool["name"],{"args1": "hello"})
    for content in tool_call_response:
        print_response(content['text'], prefix='[SERVER] tool response: \n')
    # print_response(tool_call_response['result'], prefix='[SERVER]: \n')

    # call tool, we need a name and arguments
    close_server()

main()


# todo: add notifications support, should loop when calling tools or listing tools and/or use an async system
