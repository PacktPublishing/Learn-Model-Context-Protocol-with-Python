# @mcp.tool()
# def get_product(product_id: int) -> Product:
#     """Get product by ID"""
#     for product in products:
#         if product.name == product_id:
#             return {"type": "text", "name": f"ID: {product.name},price: {product.price},description: {product.description}"}
#     return None

from data import products
from .schema import ProductModel, GetProductInputModel

async def handler(args) -> ProductModel:
    # Get product by id
    input = GetProductInputModel(**args)
    
    # Find the product with the given id
    for product in products:
        if product.id == input.product_id:
            return product
    
    # If no product found, return None or raise an error
    return None

tool_get_product = {
    "name": "get_product",
    "description": "Gets a product by ID",
    "input_schema": GetProductInputModel,
    "handler": handler
}