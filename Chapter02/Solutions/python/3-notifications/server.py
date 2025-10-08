import sys
import json

from utils.messages import initializeResponse, progress_notification

initialized = False

while True:
    for line in sys.stdin:
        message = line.strip()
        if message == "hello":
            print("hello there")
            sys.stdout.flush()  # Ensure output is sent immediately
        elif message.startswith('{"jsonrpc":'):
            json_message = json.loads(message)
            method = json_message.get('method', '')

            if not initialized:
                if method != "initialize" and method != "notifications/initialized":
                    print(f"Server not initialized. Please send an 'initialized' notification first. You sent {method}")
                    sys.stdout.flush()
                    continue

            match method:
                case "notifications/initialized":
                    # print("Server initialized successfully.")
                    sys.stdout.flush()
                    initialized = True
                    break
                case "initialize":
                    print(json.dumps(initializeResponse))
                    sys.stdout.flush()
                    # initialized = True
                    break
                     # should return capabilities
                case "tools/call":
                    tool_name = json_message['params']['name']
                    args = json_message['params']['args']

                    print(json.dumps(progress_notification))
                    sys.stdout.flush()

                    print(json.dumps(progress_notification))
                    sys.stdout.flush()

                    # todo create a response for the tool call, i.e call the right tool
                    response = {
                        "jsonrpc": "2.0",
                        "id": json_message["id"],
                        "result": {
                            "properties": {
                                "content": {
                                    "description": "description of the content",
                                    "items": [
                                        { "type": "text", "text": f"Called tool {tool_name} with arguments {args}" }
                                    ]
                                }
                            }
                        }
                    }
                    print(json.dumps(response))
                    sys.stdout.flush()
                    break
                case "tools/list":

                    # send notification about progress first, then later the response
                    print(json.dumps(progress_notification))
                    sys.stdout.flush()

                    response = {
                        "jsonrpc": "2.0",
                        "id": json_message["id"],
                        "result": {
                            "tools": [
                                {
                                    "name": "example_tool",
                                    "description": "An example tool that does something.",
                                    "inputSchema": {
                                        "type": "object",
                                        "properties": {
                                            "arg1": {
                                                "type": "string",
                                                "description": "An example argument."
                                            }
                                        },
                                        "required": ["arg1"]
                                    }
                                }
                            ]
                        }
                    }
                    print(json.dumps(response))
                    sys.stdout.flush()
                    break
                case _:
                    print(f"Unknown method: {json_message['method']}")
                    sys.stdout.flush()
                    break
        elif message == "exit":
            print("Exiting server.")
            sys.stdout.flush()
            sys.exit(0)
        else:
            print(f"Unknown message: {message}")
   