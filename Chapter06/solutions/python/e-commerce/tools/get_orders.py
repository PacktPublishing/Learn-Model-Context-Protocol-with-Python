# @mcp.tool()
# def get_orders(customer_id:int = 0) -> [Order]:
#     """get all orders"""

#     if customer_id != 0 and not any(customer.id == customer_id for customer in customers):
#         raise ValueError(f"Invalid customer_id: {customer_id}")

#     filtered_orders = orders
#     if customer_id != 0:
#         filtered_orders = [order for order in orders if order.customer_id == customer_id]

#     return [{"type": "text", "name": f"ID: {order.order_id},customer: {order.customer_id}"} for order in filtered_orders]

from data import orders
from .schema import OrderModel, GetOrderInputModel

async def handler(args) -> list[OrderModel]:
    # get order by id
    input = GetOrderInputModel(**args)
    # filter orders based on customer_id if provided
    filtered_orders = []
    
    if input.customer_id != 0:
        filtered_orders = [order for order in orders if order.customer_id == input.customer_id]
    else:
        filtered_orders = orders
    
    # return the filtered orders
    return filtered_orders

tool_get_orders = {
    "name": "get_orders",
    "description": "Gets all orders",
    "input_schema": GetOrderInputModel,
    "handler": handler
}