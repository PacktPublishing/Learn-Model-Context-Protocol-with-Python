from data import carts
from .schema import AddCartInputModel

async def handler(args) -> list[AddCartInputModel]:
    return carts

tool_get_all_carts = {
    "name": "get_all_carts",
    "description": "Gets all carts",
    "input_schema": None,
    "handler": handler
}
