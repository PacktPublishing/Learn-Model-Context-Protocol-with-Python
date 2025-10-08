import sys
import json

while True:
    for line in sys.stdin:
        message = line.strip()
        if message == "hello":
            print("hello there")
            sys.stdout.flush()  # Ensure output is sent immediately
        elif message.startswith('{"jsonrpc":'):
            json_message = json.loads(message)
            match json_message['method']:
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
   