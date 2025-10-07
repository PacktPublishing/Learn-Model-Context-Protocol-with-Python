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
mcp run server.py
```

## -4- Test the sample

With the server running in one terminal, open another terminal and run the following command:

```bash
mcp dev server.py
```

This should start a web server with a visual interface allowing you to test the sample.

Once the server is connected: 

- try listing tools and run `add`, with args 2 and 4, you should see 6 in the result.
- go to resources and resource template and call get_greeting, type in a name and you should see a greeting with the name you provided.

### Testing in ClI mode

The inspector you ran is actually a Node.js app and `mcp dev` is a wrapper around it. 

You can launch it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

This will list all the tools available in the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "get_orders",
      "description": "get all orders",
      "inputSchema": {
        "type": "object",
        "properties": {
          "customer_id": {
            "default": 0,
            "title": "Customer Id",
            "type": "integer"
          }
        },
        "title": "get_ordersArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "result": {
            "items": {
              "$ref": "#/$defs/Order"
            },
            "title": "Result",
            "type": "array"
          }
        },
        "required": [
          "result"
        ],
        "$defs": {
          "Order": {
            "properties": {
              "id": {
                "format": "uuid",
                "title": "Id",
                "type": "string"
              },
              "customer_id": {
                "title": "Customer Id",
                "type": "integer"
              }
            },
            "required": [
              "id",
              "customer_id"
            ],
            "title": "Order",
            "type": "object"
          }
        },
        "title": "get_ordersOutput"
      }
    },
    {
      "name": "get_order",
      "description": "get order by id",
      "inputSchema": {
        "type": "object",
        "properties": {
          "order_id": {
            "title": "Order Id",
            "type": "integer"
          }
        },
        "required": [
          "order_id"
        ],
        "title": "get_orderArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "id": {
            "format": "uuid",
            "title": "Id",
            "type": "string"
          },
          "customer_id": {
            "title": "Customer Id",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "customer_id"
        ],
        "title": "Order"
      }
    },
    {
      "name": "place_order",
      "description": "place order",
      "inputSchema": {
        "type": "object",
        "properties": {
          "customer_id": {
            "title": "Customer Id",
            "type": "integer"
          }
        },
        "required": [
          "customer_id"
        ],
        "title": "place_orderArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "id": {
            "format": "uuid",
            "title": "Id",
            "type": "string"
          },
          "customer_id": {
            "title": "Customer Id",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "customer_id"
        ],
        "title": "Order"
      }
    },
    {
      "name": "get_cart",
      "description": "get a singular cart",
      "inputSchema": {
        "type": "object",
        "properties": {
          "customer_id": {
            "title": "Customer Id",
            "type": "integer"
          }
        },
        "required": [
          "customer_id"
        ],
        "title": "get_cartArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "result": {
            "items": {
              "$ref": "#/$defs/Cart"
            },
            "title": "Result",
            "type": "array"
          }
        },
        "required": [
          "result"
        ],
        "$defs": {
          "Cart": {
            "properties": {
              "id": {
                "title": "Id",
                "type": "integer"
              },
              "customer_id": {
                "title": "Customer Id",
                "type": "integer"
              }
            },
            "required": [
              "id",
              "customer_id"
            ],
            "title": "Cart",
            "type": "object"
          }
        },
        "title": "get_cartOutput"
      }
    },
    {
      "name": "get_cart_items",
      "description": "get cart items",
      "inputSchema": {
        "type": "object",
        "properties": {
          "cart_id": {
            "title": "Cart Id",
            "type": "integer"
          }
        },
        "required": [
          "cart_id"
        ],
        "title": "get_cart_itemsArguments"
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
            "properties": {
              "id": {
                "title": "Id",
                "type": "integer"
              },
              "cart_id": {
                "format": "uuid",
                "title": "Cart Id",
                "type": "string"
              },
              "product_id": {
                "title": "Product Id",
                "type": "integer"
              },
              "quantity": {
                "title": "Quantity",
                "type": "integer"
              }
            },
            "required": [
              "id",
              "cart_id",
              "product_id",
              "quantity"
            ],
            "title": "CartItem",
            "type": "object"
          }
        },
        "title": "get_cart_itemsOutput"
      }
    },
    {
      "name": "add_to_cart",
      "description": "add to cart",
      "inputSchema": {
        "type": "object",
        "properties": {
          "cart_id": {
            "title": "Cart Id",
            "type": "integer"
          },
          "product_id": {
            "title": "Product Id",
            "type": "integer"
          },
          "quantity": {
            "title": "Quantity",
            "type": "integer"
          }
        },
        "required": [
          "cart_id",
          "product_id",
          "quantity"
        ],
        "title": "add_to_cartArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "cart_id": {
            "format": "uuid",
            "title": "Cart Id",
            "type": "string"
          },
          "product_id": {
            "title": "Product Id",
            "type": "integer"
          },
          "quantity": {
            "title": "Quantity",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "cart_id",
          "product_id",
          "quantity"
        ],
        "title": "CartItem"
      }
    },
    {
      "name": "get_all_products",
      "description": "Get all products",
      "inputSchema": {
        "type": "object",
        "properties": {},
        "title": "get_all_productsArguments"
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
            "properties": {
              "id": {
                "title": "Id",
                "type": "integer"
              },
              "name": {
                "title": "Name",
                "type": "string"
              },
              "price": {
                "title": "Price",
                "type": "number"
              },
              "description": {
                "title": "Description",
                "type": "string"
              }
            },
            "required": [
              "id",
              "name",
              "price",
              "description"
            ],
            "title": "Product",
            "type": "object"
          }
        },
        "title": "get_all_productsOutput"
      }
    },
    {
      "name": "get_product",
      "description": "Get product by ID",
      "inputSchema": {
        "type": "object",
        "properties": {
          "product_id": {
            "title": "Product Id",
            "type": "integer"
          }
        },
        "required": [
          "product_id"
        ],
        "title": "get_productArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "id": {
            "title": "Id",
            "type": "integer"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "price": {
            "title": "Price",
            "type": "number"
          },
          "description": {
            "title": "Description",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "price",
          "description"
        ],
        "title": "Product"
      }
    },
    {
      "name": "get_all_categories",
      "description": "Get all categories",
      "inputSchema": {
        "type": "object",
        "properties": {},
        "title": "get_all_categoriesArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "result": {
            "items": {
              "$ref": "#/$defs/Category"
            },
            "title": "Result",
            "type": "array"
          }
        },
        "required": [
          "result"
        ],
        "$defs": {
          "Category": {
            "properties": {
              "id": {
                "format": "uuid",
                "title": "Id",
                "type": "string"
              },
              "name": {
                "title": "Name",
                "type": "string"
              },
              "description": {
                "title": "Description",
                "type": "string"
              }
            },
            "required": [
              "id",
              "name",
              "description"
            ],
            "title": "Category",
            "type": "object"
          }
        },
        "title": "get_all_categoriesOutput"
      }
    },
    {
      "name": "get_all_customers",
      "description": "Get all customers",
      "inputSchema": {
        "type": "object",
        "properties": {},
        "title": "get_all_customersArguments"
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "result": {
            "items": {
              "$ref": "#/$defs/Customer"
            },
            "title": "Result",
            "type": "array"
          }
        },
        "required": [
          "result"
        ],
        "$defs": {
          "Customer": {
            "properties": {
              "id": {
                "title": "Id",
                "type": "integer"
              },
              "name": {
                "title": "Name",
                "type": "string"
              },
              "email": {
                "title": "Email",
                "type": "string"
              }
            },
            "required": [
              "id",
              "name",
              "email"
            ],
            "title": "Customer",
            "type": "object"
          }
        },
        "title": "get_all_customersOutput"
      }
    }
  ]
}
```

To invoke a tool type:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name get_all_categories
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "{\n  \"id\": \"a231765d-7eae-4462-9042-a6e00b211bf0\",\n  \"name\": \"Category 1\",\n  \"description\": \"Description of Category 1\"\n}"
    },
    {
      "type": "text",
      "text": "{\n  \"id\": \"50285d76-e7b8-4939-b2df-08452750b5da\",\n  \"name\": \"Category 2\",\n  \"description\": \"Description of Category 2\"\n}"
    },
    {
      "type": "text",
      "text": "{\n  \"id\": \"fdd934ee-f8c8-47dc-ab63-1efe68a8bbb2\",\n  \"name\": \"Category 3\",\n  \"description\": \"Description of Category 3\"\n}"
    }
  ],
  "structuredContent": {
    "result": [
      {
        "id": "a231765d-7eae-4462-9042-a6e00b211bf0",
        "name": "Category 1",
        "description": "Description of Category 1"
      },
      {
        "id": "50285d76-e7b8-4939-b2df-08452750b5da",
        "name": "Category 2",
        "description": "Description of Category 2"
      },
      {
        "id": "fdd934ee-f8c8-47dc-ab63-1efe68a8bbb2",
        "name": "Category 3",
        "description": "Description of Category 3"
      }
    ]
  },
  "isError": false
}
```

> ![!TIP]
> It's usually a lot faster to run the ispector in CLI mode than in the browser.
> Read more about the inspector [here](https://github.com/modelcontextprotocol/inspector).