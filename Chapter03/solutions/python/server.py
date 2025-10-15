# server.py
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import Union

import uuid

#add an extra import statement
from typing import List, Dict, Any, Optional


# Create an MCP server
mcp = FastMCP("Demo")

class Customer(BaseModel):
    id: int
    name: str
    email: str

    def __init__(self, **data):
        super().__init__(**data)

class Category(BaseModel):
    id: uuid.UUID
    name: str
    description: str

    def __init__(self, **data):
        if 'id' not in data:
            data['id'] = uuid.uuid4()
        super().__init__(**data)

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

class CartItem(BaseModel):
    id: int
    cart_id: uuid.UUID
    product_id: int
    quantity: int

    def __init__(self, cart_id: uuid.UUID, product_id: int, quantity: int):
        if cart_id != uuid.UUID(int=0):
            self.cart_id = cart_id
        else:
            self.cart_id = uuid.uuid4()
        self.product_id = product_id
        self.quantity = quantity

class Cart(BaseModel):
    id: int
    customer_id: int

    def __init__(self, **data):
        if 'id' not in data:
            data['id'] = uuid.uuid4()
        super().__init__(**data)

class Order(BaseModel):
    id: uuid.UUID
    customer_id: int

    def __init__(self, **data):
        if 'id' not in data or not isinstance(data['id'], uuid.UUID):
            data['id'] = uuid.uuid4()
        super().__init__(**data)


products = [
    Product(id=1, name="Product 1", price=10.0, description="Description of Product 1"),
    Product(id=2, name="Product 2", price=20.0, description="Description of Product 2"),
    Product(id=3, name="Product 3", price=30.0, description="Description of Product 3")
]

orders = [
    Order(id=1, customer_id=101),
    Order(id=uuid.uuid4(), customer_id=101),
    Order(id=uuid.uuid4(), customer_id=102)
]

carts = []
cart_items = []

customers = [
    Customer(id=1, name="Customer 1", email="email")
]


categories = [
    Category(id=uuid.uuid4(), name="Category 1", description="Description of Category 1"),
    Category(id=uuid.uuid4(), name="Category 2", description="Description of Category 2"),
    Category(id=uuid.uuid4(), name="Category 3", description="Description of Category 3")
]

product_catalog = [
    {
        "name": "Product 1",
        "price": 10.0,
        "description": "Description of Product 1",
        "category_id": 1
    },
    {
        "name": "Product 2",
        "price": 20.0,
        "description": "Description of Product 2",
        "category_id": 2
    },
    {
        "name": "Product 3",
        "price": 30.0,
        "description": "Description of Product 3",
        "category_id": 3
    }
]


# get orders
@mcp.tool()
def get_orders(customer_id:int = 0) -> List[Order]:
    """get all orders"""

    if customer_id != 0 and not any(customer.id == customer_id for customer in customers):
        raise ValueError(f"Invalid customer_id: {customer_id}")

    filtered_orders = orders
    if customer_id != 0:
        filtered_orders = [order for order in orders if order.customer_id == customer_id]

    return filtered_orders

# get order by id
@mcp.tool()
def get_order(order_id:int) -> Order | None:
    """get order by id"""
    for order in orders:
        if order.order_id == order_id:
            return order
    return None

# place order
@mcp.tool()
def place_order(customer_id:int) -> Order:
    """place order"""
    if customer_id != 0 and not any(customer.id == customer_id for customer in customers):
        raise ValueError(f"Invalid customer_id: {customer_id}")

    new_order = Order(0, customer_id)
    orders.append(new_order)
    return new_order

# get carts
@mcp.tool()
def get_cart(customer_id:int) -> Cart | None:
    """get a singular cart"""

    if customer_id != 0 and not any(customer.id == customer_id for customer in customers):
        raise ValueError(f"Invalid customer_id: {customer_id}")

    # get cart by customer id
    cart = next((cart for cart in carts if cart.customer_id == customer_id), None)
    if cart:
        return cart
    return None

    
# get cart items
@mcp.tool()
def get_cart_items(cart_id:int) -> List[CartItem]:
    """get cart items"""

    # find a specific cart by id
    items = [item for item in cart_items if item.cart_id == cart_id]

    # return items in that cart
    return items

# add to cart
@mcp.tool()
def add_to_cart(cart_id:int, product_id:int, quantity:int) -> CartItem:
    """add to cart"""
    new_cart_item = CartItem(cart_id, product_id, quantity)
    cart_items.append(new_cart_item)
    return new_cart_item

# tool, all products
@mcp.tool()
def get_all_products() -> List[Product]:
    """Get all products"""
    return products

# tool, product by id
@mcp.tool()
def get_product(product_id: int) -> Product | None:
    """Get product by ID"""
    for product in products:
        if product.id == product_id:
            return product
    return None

# tool, all categories
@mcp.tool()
def get_all_categories() -> List[Category]:
    """Get all categories"""
    return categories

# tool, all customers
@mcp.tool()
def get_all_customers() -> List[Customer]:
    """Get all customers"""
    return customers

# resource, product catalog
@mcp.resource("resource:product_catalog") 
def get_product_catalog():
    """Get product catalog"""
    return product_catalog