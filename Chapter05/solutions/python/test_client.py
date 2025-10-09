import requests
import json

message = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
            "roots": {
                "listChanged": True
            },
            "sampling": {}
            },
            "clientInfo": {
            "name": "ExampleClient",
            "version": "1.0.0"
            }
        }
    }

headers = {
        'Accept': 'application/json, text/event-stream',
        'Content-Type': 'application/json'
    }

response = requests.post(
        f'http://localhost:{8000}/stream', 
        stream=True, 
        headers=headers,
        data=json.dumps(message))

for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))