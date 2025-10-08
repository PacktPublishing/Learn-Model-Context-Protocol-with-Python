# need to start a child process and send info to it via stdin

import subprocess
import json

# Start the child process
proc = subprocess.Popen(
    ['python3', 'server.py'],  # Replace with your child script
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

list_tools_message = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
};

message = 'hello\n'

def send_message(message):
    """Send a message to the child process."""
    print(f'[CLIENT] Sending message to server... Message: {message.strip()}')
    proc.stdin.write(message)
    proc.stdin.flush()

def serialize_message(message):
    """Serialize a message to JSON format."""
    return json.dumps(message) + '\n'

# Send a message to the child
send_message(message)

# Read response from child
response = proc.stdout.readline()
print('[SERVER]:', response.strip())

# send a JSON-RPC message
send_message(serialize_message(list_tools_message))

response = proc.stdout.readline()
print('[SERVER]:', response.strip())

# this closes down the child process aka server
send_message('exit\n')

exit_code = proc.wait()
print(f"Child exited with code {exit_code}")

proc.stdin.close()
proc.terminate()