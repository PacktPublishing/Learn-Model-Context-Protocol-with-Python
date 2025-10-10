from .add_to_cart import tool_add_to_cart
from .get_all_categories import tool_get_all_categories
from .get_cart_items import tool_get_all_cart_items
from .get_all_products import tool_get_all_products
from .get_all_customers import tool_get_all_customers
from .get_orders import tool_get_orders
from .get_product import tool_get_product
from .place_order import tool_place_order

tools = {
  tool_add_to_cart["name"] : tool_add_to_cart,
  tool_get_all_categories["name"] : tool_get_all_categories,
  tool_get_all_cart_items["name"] : tool_get_all_cart_items,
  tool_get_all_products["name"] : tool_get_all_products,
  tool_get_all_customers["name"] : tool_get_all_customers,
  tool_get_orders["name"] : tool_get_orders,
  tool_get_product["name"] : tool_get_product,
  tool_place_order["name"] : tool_place_order
}
