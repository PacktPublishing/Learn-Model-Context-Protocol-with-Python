from data import categories
from .schema import CategoryModel

async def handler(args) -> list[CategoryModel]:
    return categories

tool_get_all_categories = {
    "name": "get_all_categories",
    "description": "Gets all product categories",
    "input_schema": None,
    "handler": handler 
}