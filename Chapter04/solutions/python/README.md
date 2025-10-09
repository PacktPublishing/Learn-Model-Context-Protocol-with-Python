# Running this sample

You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

## -1- Activate the virtual environment

```bash
venv\Scrips\activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]"
```

## -3- Run the sample


```bash
uvicorn server:app --port 3000
```

## -4- Test the sample

With the server running in one terminal, open another terminal and run the following command:

```bash
curl http://127.0.0.1:3000/sse
```

You should see a response similar to:

```text
event: endpoint
data: /messages/?session_id=262edd9eb4ba4185abe28756eba2c7f1
```

That is, something that shows you a `session_id`. Great, that means our SSE Server is responding and carrying out a handshake.

### Testing in ClI mode

The inspector you ran is actually a Node.js app and `mcp dev` is a wrapper around it. 

You can launch it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3000/sse --method tools/list
```

This will list all the tools available in the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "add_product_to_cart",
      "description": "Add product to cart",
      "inputSchema": {
        "type": "object",
        "properties": {
          "product_name": {
            "title": "Product Name",
            "type": "string"
          }
        },
        "required": [
          "product_name"
        ],
        "title": "add_product_to_cartArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {},
        "title": "CartItem"
      }
    },
    {
      "name": "list_cart",
      "description": "List all cart items",
      "inputSchema": {
        "type": "object",
        "properties": {},
        "title": "list_cartArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "result": {
            "items": {
              "$ref": "#/$defs/CartItem"
            },
            "title": "Result",
            "type": "array"
          }
        },
        "required": [
          "result"
        ],
        "$defs": {
          "CartItem": {
            "properties": {},
            "title": "CartItem",
            "type": "object"
          }
        },
        "title": "list_cartOutput"
      }
    },
    {
      "name": "get_products",
      "description": "Get all products",
      "inputSchema": {
        "type": "object",
        "properties": {},
        "title": "get_productsArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "result": {
            "items": {
              "$ref": "#/$defs/Product"
            },
            "title": "Result",
            "type": "array"
          }
        },
        "required": [
          "result"
        ],
        "$defs": {
          "Product": {
            "properties": {},
            "title": "Product",
            "type": "object"
          }
        },
        "title": "get_productsOutput"
      }
    }
  ]
}
```

To invoke a tool type:

```bash
npx @modelcontextprotocol/inspector --cli http://127.0.0.1:3000/sse --method tools/call --tool-name list_cart
```

You should see the following output:

```text
{
  "content": [],
  "structuredContent": {
    "result": []
  },
  "isError": false
}
```

Which is to be expected since we haven't added any products to the cart yet.

To add a product to the cart, run the following command:

```bash
npx @modelcontextprotocol/inspector --cli http://127.0.0.1:3000/sse --method tools/call --tool-name add_product_to_cart --tool-arg product_name="Product 1"
```

You should see an output similar to:

```text
{
  "content": [
    {
      "type": "text",
      "text": "{\n  \"cart_id\": 1,\n  \"product_id\": 1,\n  \"quantity\": 1\n}"       
    }
  ],
  "structuredContent": {
    "cart_id": 1,
    "product_id": 1,
    "quantity": 1
  },
  "isError": false
}
```

What you're seeing is a response from the server that contains the ID of the product you just added to the cart. You can now list the cart items again by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli http://127.0.0.1:3000/sse --method tools/call --tool-name list_cart
```

and you should now see:

```text
{
  "content": [
    {
      "type": "text",
      "text": "{\n  \"cart_id\": 1,\n  \"product_id\": 1,\n  \"quantity\": 1\n}"       
    }
  ],
  "structuredContent": {
    "result": [
      {
        "cart_id": 1,
        "product_id": 1,
        "quantity": 1
      }
    ]
  },
  "isError": false
}
```
