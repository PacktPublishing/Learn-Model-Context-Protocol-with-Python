from data import products
from .schema import ProductModel

async def handler(args) -> list[ProductModel]:
    return products

tool_get_all_products = {
    "name": "get_all_products",
    "description": "Gets all products",
    "input_schema": None,
    "handler": handler
}   
