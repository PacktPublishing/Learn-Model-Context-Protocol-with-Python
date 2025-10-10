# Running this sample

## Install dependencies

First, create a virtual environment:

```sh
python -m venv venv
source ./venv/bin/activate
```

```sh
pip install "mcp[cli]"
```

## Test the server out

Start up the server:

```
cd e-commerce
python server.py
```

In a separate terminal:

Place order

```
npx @modelcontextprotocol/inspector --cli http://localhost:8000/sse --method tools/call --tool-name place_order --tool-arg order_id=0 --tool-arg customer_id=1 --tool-arg quantity=1 --tool-arg total_price=100
```

Get orders (all orders)

```sh
npx @modelcontextprotocol/inspector --cli http://localhost:8000/sse --method tools/call --tool-name get_orders --tool-arg customer_id=0
```
