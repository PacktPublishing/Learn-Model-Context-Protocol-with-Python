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
python client.py
```

You should see the following output:

```text
LISTING TOOLS
Tool:  add_product_to_cart
Tool:  list_cart
Tool:  get_products
Enter command (or 'quit' to exit):
```

## -4- Test the sample

Test the sample through below input. We assume you have the app running at this point.

1. Type the following command **get_products**, you should see the following output

  ```text
  Using tool: get_products
  Tool arguments: {'properties': {}, 'title': 'get_productsArguments', 'type': 'object'}
  [05/22/25 15:17:53] INFO     Processing request of type CallToolRequest                                        server.py:551
  Result:  [TextContent(type='text', text='{\n  "type": "text",\n  "name": "Name: Product 1"\n}', annotations=None), TextContent(type='text', text='{\n  "type": "text",\n  "name": "Name: Product 2"\n}', annotations=None), TextContent(type='text', text='{\n  "type": "text",\n  "name": "Name: Product 3"\n}', annotations=None)]
  ```

  This tells you that there's a list of products to choose from

1. Add an item to the cart like by typing **add_product_to_cart**. You should see another prompt asking you to "Enter product name", type **Product 2**. You should see a response like so:

  ```text
  [05/22/25 15:19:51] INFO     Processing request of type CallToolRequest                                        server.py:551
  Result:  [TextContent(type='text', text='{\n  "type": "text",\n  "name": "ID: 45eef588-3a29-4798-b1ae-44dbfa92075d,product: 2,quantity: 1"\n}', annotations=None)]
  ```

 1. List cart content with the command **list_cart**, you should see the following response:

  ```text
  Using tool: list_cart
  Tool arguments: {'properties': {}, 'title': 'list_cartArguments', 'type': 'object'}
  [05/22/25 15:20:51] INFO     Processing request of type CallToolRequest                                        server.py:551
  Result:  [TextContent(type='text', text='{\n  "type": "text",\n  "name": "ID: 45eef588-3a29-4798-b1ae-44dbfa92075d,product: 2,quantity: 1"\n}', annotations=None)]
  ``` 

  This correctly shows us the item we just added.

## Test the LLm sample

1. Install dependencies (we need to support calling an LLM)

  ```sh
  pip install openai
  ```

1. Run the LLM client by typing the following:

  ```sh
  python client_llm.py
  ```

  You should see the following output:

  ```text
  LISTING TOOLS
  Tool:  add_product_to_cart
  Tool:  list_cart
  Tool:  get_products
  Waiting for input... (type 'quit' to exit)
  Enter prompt:
  ```

1. Type **show me products**, like so:

  ```text
  Enter prompt: show me products
  ```

  You should see the following output:

  ```text
  ALLING LLM
  TOOL NAME:  get_products
  [05/22/25 16:35:14] INFO     Processing request of type CallToolRequest                                        server.py:551
  TOOLS result:  [TextContent(type='text', text='{\n  "type": "text",\n  "name": "Name: Product 1"\n}', annotations=None), TextContent(type='text', text='{\n  "type": "text",\n  "name": "Name: Product 2"\n}', annotations=None), TextContent(type='text', text='{\n  "type": "text",\n  "name": "Name: Product 3"\n}', annotations=None)]
  Waiting for input... (type 'quit' to exit)
  ```

1. Now add a product by typing the following **Add Product 1 to the cart**, you should see the following output:

  ```text
  CALLING LLM
  TOOL NAME:  add_product_to_cart
  [05/22/25 17:21:31] INFO     Processing request of type CallToolRequest                                        server.py:551
  TOOLS result:  [TextContent(type='text', text='{\n  "type": "text",\n  "name": "ID: 921f95e8-0855-40ca-8587-8a6e38bfd69d,product: 1,quantity: 1"\n}', annotations=None)]
  Waiting for input... (type 'quit' to exit)
  ```

1. Let's double check by typing **show me cart content**, you should see the following output:

  ```text
  CALLING LLM
  TOOL NAME:  list_cart
  [05/22/25 17:23:10] INFO     Processing request of type CallToolRequest                                        server.py:551
  TOOLS result:  [TextContent(type='text', text='{\n  "type": "text",\n  "name": "ID: 9d0e23f3-23d5-4d7e-bfa9-71be86b26f04,product: 1,quantity: 1"\n}', annotations=None)]
  Waiting for input... (type 'quit' to exit)
  ````

  As you can see, your added product is in the cart.
