from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP
from typing import List
from pydantic import BaseModel

mcp = FastMCP("My App")


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    category: str

class CartItem(BaseModel):
    cart_id: int
    product_id: int
    quantity: int


products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 10.0,
        "description": "Description of Product 1",
        "category": "Category 1"
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 20.0,
        "description": "Description of Product 2",
        "category": "Category 2"
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 30.0,
        "description": "Description of Product 3",
        "category": "Category 3"
    }
]

cart = []

# get products by category
@mcp.tool()
def get_products_by_category(category: str) -> List[Product]:
    """Get products by category"""
    return [Product(**product) for product in products if product["category"] == category]

# add product to cart
@mcp.tool()
def add_product_to_cart(product_name: str) -> CartItem:
    """Add product to cart"""
    product = next((p for p in products if p["name"] == product_name), None)
    if not product:
        return {"type": "text", "name": f"Product [{product_name}] not found"}
    cart_item = CartItem(cart_id=1, product_id=product["id"], quantity=1)
    cart.append(cart_item)

    return cart_item

# list cart
@mcp.tool()
def list_cart() -> List[CartItem]:
    """List all cart items"""
    return cart

# tool, all products
@mcp.tool()
def get_products() -> List[Product]:
    """Get all products"""
    # convert products to Product objects
    products_vm = [Product(**product) for product in products]
    return products_vm



# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
