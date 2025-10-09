import requests

port = 8000

def consume_stream():
    response = requests.get(f'http://localhost:{port}/stream', stream=True)
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))
consume_stream()