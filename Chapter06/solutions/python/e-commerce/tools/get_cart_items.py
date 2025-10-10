# @mcp.tool()
# def get_cart_items(cart_id:int) -> [CartItem]:
#     """get cart items"""
#     cart_items = [item for item in carts if item.cart_id == cart_id]
#     return [{"type": "text", "name": f"ID: {item.cart_id},product: {item.product_id},quantity: {item.quantity}"} for item in cart_items]

from data import cart_items
from .schema import CartItemModel

async def handler(args) -> list[CartItemModel]:
    return cart_items

tool_get_all_cart_items = {
    "name": "get_all_cart_items",
    "description": "Gets all cart items",
    "input_schema": None,
    "handler": handler
}   
