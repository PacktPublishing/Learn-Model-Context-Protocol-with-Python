# need to start a child process and send info to it via stdin

import subprocess
import json
import threading
import queue

from utils.messages import list_tools_message, initialize_message, initialized_message

message_queue = queue.Queue()

# Start the child process
proc = subprocess.Popen(
    ['python3', 'server.py'],  # Replace with your child script
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

message = 'hello\n'

def is_sampling_message(message):
    """Check if a message is a sampling message."""
    return message.get('method', '').startswith('sampling')

def is_notification_message(message):
    """Check if a message is a notification."""
    return message.get('method', '').startswith('notifications/')

def create_sampling_message(llm_response):
    """Create a sampling message for a product."""
    sampling_message = {
        "jsonrpc": "2.0",
        "result": {
            "content": {
                "text": llm_response
            }
        }
    }
    return sampling_message

def call_llm(message):
    return "LLM: " + message 


def handle_sampling_message(message):
    """Handle a sampling message."""
    print("[CLIENT] Calling LLM to complete request", message)
    # get content info from message, send that to LLM

    content = message['params']['messages'][0]['content']['text']
    llm_response = call_llm(content)
    message = create_sampling_message(llm_response)
    send_message(serialize_message(message))
    # should call LLM to complete request

def listen_to_stdout():
    """Listen to the stdout of the child process and handle messages."""
    while True:
        response = proc.stdout.readline()
        if not response:
            break  # Exit if no more output

        try:
            parsed_response = json.loads(response)
            if is_sampling_message(parsed_response):
                handle_sampling_message(parsed_response)
                # consume message if it is a sampling message
            else:
                # put message in the queue for further processing
                message_queue.put(response.strip())
        except json.JSONDecodeError:
            # If the response is not JSON, just print it
            print("[THREAD] Non-JSON response received:", response.strip())
            # print_response(response, prefix='[THREAD]: \n')
        

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
    # response = proc.stdout.readline()
    response = message_queue.get()
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
        # response = proc.stdout.readline()
        response = message_queue.get()
        # check if message has result attribute, if so break out of loop
        
        parsed_response = json.loads(response)
        if 'result' in parsed_response:
            has_result = True
            return parsed_response['result']['tools']
        else:
            # this is a notification, we can print it
            print_response(response, prefix=f'[SERVER] {parsed_response["method"]}: \n')

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
        response = message_queue.get()
        # response = proc.stdout.readline()
        parsed_response = json.loads(response)
        if 'result' in parsed_response:
            has_result = True
            return parsed_response["result"]["properties"]["content"]["items"]
        else:
            # this is a notification, we can print it
            print_response(response, prefix=f'[SERVER] {parsed_response["method"]}: \n')

def close_server():
    # send_message('exit\n')

    exit_code = proc.wait()
    print(f"Child exited with code {exit_code}")

tools = []

listener_thread = threading.Thread(target=listen_to_stdout, daemon=True)
listener_thread.start()

def main():
    connect()

    # a sampling message can be sent at any time here

    tool_response = list_tools() 
    tools.extend(tool_response)
    
    print("Tools available:", tools)

    tool = tools[0]

    tool_call_response = call_tool(tool["name"],{"args1": "hello"})
    for content in tool_call_response:
        print_response(content['text'], prefix='[SERVER] tool response: \n')
   
    # call tool, we need a name and arguments
    close_server()

main()


# todo: add notifications support, should loop when calling tools or listing tools and/or use an async system
