from data import customers
from .schema import CustomerModel

async def handler(args) -> list[CustomerModel]:
    return customers

tool_get_all_customers = {
    "name": "get_all_customers",
    "description": "Gets all customers",
    "input_schema": None,
    "handler": handler
}