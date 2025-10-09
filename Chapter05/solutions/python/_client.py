import requests

import json
port = 8000

def consume_stream():
    headers = {
        'Accept': 'application/json, text/event-stream',
        'Content-Type': 'application/json'
    }

    # json rpc message with initialized
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

    initialized = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }

    listTools = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }

    callTool = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "echo",
            "arguments": {
                "message": "chris"
            }
        }
    }

    # post /mcp, gets us the session_id
    # get should give the session back
    # where to post the data?

    response = requests.post(
        f'http://localhost:{port}/mcp', 
        stream=True, 
        headers=headers,
        data=json.dumps(message))
    
    print("Session ID:", response.headers.get('mcp-session-id'))
    
    # for line in response.iter_lines():
    #     if line:
    #         print(line.decode('utf-8'))

    # print("HEADERS: ",response.headers)
    # session_id = response.headers.get('mcp-session-id')
    # print("Session ID:", session_id)

    headers['mcp-session-id'] = response.headers.get('mcp-session-id')

    print("Calling initialized...")
    response = requests.post(
        f'http://localhost:{port}/mcp', 
        stream=True, 
        headers=headers,
        data=json.dumps(initialized))

    print("Calling list tools...")
    response = requests.post(
        f'http://localhost:{port}/mcp', 
        stream=True, 
        headers=headers,
        data=json.dumps(listTools))

    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))

    print("Calling tool: echo...")
    response = requests.post(
        f'http://localhost:{port}/mcp', 
        stream=True, 
        headers=headers,
        data=json.dumps(callTool))

    print("Tool call headers:", response.headers)

    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))

consume_stream()