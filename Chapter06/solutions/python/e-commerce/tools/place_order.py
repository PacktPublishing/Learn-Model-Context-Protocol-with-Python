# @mcp.tool()
# def place_order(customer_id:int) -> Order:
#     """place order"""
#     if customer_id != 0 and not any(customer.id == customer_id for customer in customers):
#         raise ValueError(f"Invalid customer_id: {customer_id}")

#     new_order = Order(0, customer_id)
#     orders.append(new_order)
#     return {"type": "text", "name": f"ID: {new_order.order_id},customer: {new_order.customer_id}"}

from data import orders, customers
from .schema import OrderModel

async def handler(args) -> OrderModel:
    order = OrderModel(**args)

    if order.customer_id != 0 and not any(customer.id == order.customer_id for customer in customers):
        raise ValueError(f"Invalid customer_id: {order.customer_id}")

    # Create a new order with a new ID
    new_order = OrderModel(order_id=len(orders) + 1, customer_id=order.customer_id, quantity=order.quantity, total_price=order.total_price)
    orders.append(new_order)

    return new_order

tool_place_order = {
    "name": "place_order",
    "description": "Places a new order for a customer",
    "input_schema": OrderModel,
    "handler": handler
}