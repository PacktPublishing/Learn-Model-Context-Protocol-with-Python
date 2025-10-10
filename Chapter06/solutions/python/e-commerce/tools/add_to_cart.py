from .schema import AddCartInputModel
from data import carts

async def add_handler(args) -> str:

    try:
        # Validate input using Pydantic model
        input_model = AddCartInputModel(**args)
        carts.append(input_model)

    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return f" Added to cart"

tool_add_to_cart = {
    "name": "add_to_cart",
    "description": "Adds a product to the shopping cart",
    "input_schema": AddCartInputModel,
    "handler": add_handler 
}