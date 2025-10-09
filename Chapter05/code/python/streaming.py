from flask import Flask, Response
import time

port = 8000

app = Flask(__name__)
@app.route('/stream')
def stream():
    def generate():
        count = 0
        max_count = 5
        data = {'message': 'Hello, world!'}
        while True:
            yield f"{data}\n"
            count += 1
            if count >= max_count:
                yield f"Reached {max_count} messages, closing connection.\n"
                break
            time.sleep(1)
    
    return Response(generate(), mimetype='application/json')

if __name__ == '__main__':
    print(f"Starting streaming server on port {port}...")
    app.run(port=port)
