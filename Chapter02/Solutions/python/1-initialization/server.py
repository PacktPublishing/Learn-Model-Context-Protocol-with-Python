import sys
import json

from utils.messages import initializeResponse

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
                case "tools/list":
                
                    response = {
                        "jsonrpc": "2.0",
                        "id": json_message["id"],
                        "result": ["tool1", "tool2"]
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
   