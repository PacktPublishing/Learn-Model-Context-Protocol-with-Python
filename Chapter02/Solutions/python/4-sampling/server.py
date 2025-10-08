import sys
import json
import queue
import threading
import random

from utils.messages import initializeResponse, progress_notification


initialized = False

product = {
    "id": "12345",
    "name": "Sample Product",
    "price": 19.99,
    "keywords": ["sample", "product", "example"]
}

class ProductStore:
    def __init__(self):
        self.started = False
        self.listeners = {}
        # create timer that adds a product to the queue every 5 seconds

    def add_product(self):
        """Add a product to the store and notify listeners."""
        product = {
            "id": str(random.randint(10000, 99999)),
            "name": f"Product {random.randint(1, 100)}",
            "price": round(random.uniform(10.0, 100.0), 2),
            "keywords": [f"keyword{random.randint(1, 5)}" for _ in range(random.randint(1, 3))]
        }
        self.dispatch_message("new_product", product)

    def start_product_queue_timer(self):
        """Start a timer that adds a product to the queue every 5 seconds."""
        def schedule_next():
            delay = random.uniform(1, 2)
            self.product_timer = threading.Timer(delay, self.add_product)
            self.product_timer.start()

        def add_twice():
            schedule_next()
            schedule_next()

        add_twice()

    def add_listener(self, message, callback):
        if not self.started:
            self.started = True
            self.start_product_queue_timer()
        """Add a listener for product updates."""
        # In a real application, this would register the callback to be called when a new product is added
        callbacks = self.listeners.get(message, [])
        callbacks.append(callback)
        self.listeners[message] = callbacks

    def dispatch_message(self, message, payload):
        """Dispatch a message to all registered listeners."""
        callbacks = self.listeners.get(message, [])
        for callback in callbacks:
            callback(payload)

def create_sampling_message(product):
    sampling_message = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "sampling/createMessage",
        "params": {
            "messages": [{
                "role": "system",
                "content": {
                    "type": "text",
                    "text": f"New product available: {product['name']} (ID: {product['id']}, Price: {product['price']}). Keywords: {', '.join(product['keywords'])}"
                }
            }],
            "systemPrompt": "You are a helpful assistant assisting with product descriptions",
            "includeContext": "thisServer",
            "maxTokens": 300
        }
    }
    return sampling_message

store = ProductStore()
store.add_listener("new_product", lambda product: print(json.dumps(create_sampling_message(product))) and sys.stdout.flush())

def handle_sampling_response(response):
    content = response['result']['content']['text']
    print("[SERVER] [Sampling response received]:", content)
    sys.stdout.flush()
    # TODO, update the store or perform any other action with the response

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

                    print(json.dumps(create_sampling_message(product)))
                    sys.stdout.flush()

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
                    # print(f"Unknown method: {method}")
                    # sys.stdout.flush()
                    if json_message['result']:
                        handle_sampling_response(json_message)
                    # sampling response, deal with it, i.e update the store
                    else:
                        print(f"Unknown method: {json_message['method']}")
                        sys.stdout.flush()
                    break
        elif message == "exit":
            print("Exiting server.")
            sys.stdout.flush()
            sys.exit(0)
        else:
            print(f"Unknown message: {message}")
   