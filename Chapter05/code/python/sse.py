from flask import Flask, Response
import time

app = Flask(__name__)


port = 8000

@app.route('/sse')
def sse():
    def generate():

        count = 0
        max = 5

        while True:
            yield f"data: {time.ctime()}\n\n"
            count += 1
            if count >= max:
                yield f"data: {max} messages sent, closing connection.\n\n"
                break
            time.sleep(1)
    
    return Response(generate(), mimetype='text/event-stream')

import json


if __name__ == '__main__':
    print(f"Starting SSE server on port {port}...")
    app.run(port=port, debug=True)
