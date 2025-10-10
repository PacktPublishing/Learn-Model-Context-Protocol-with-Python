from pydantic import BaseModel

from tools.schema import AddCartInputModel, CategoryModel, CustomerModel, ProductModel, CartItemModel, OrderModel

carts: list[AddCartInputModel] = []

categories: list[CategoryModel] = [
    CategoryModel(name="Electronics", description="Devices and gadgets"),
    CategoryModel(name="Books", description="Fiction and non-fiction books"),
    CategoryModel(name="Clothing", description="Apparel and accessories"),
]

customers: list[CustomerModel] = [
    CustomerModel(id=1, name="Alice", email="alice@example.com"),
    CustomerModel(id=2, name="Bob", email="bob@example.com"),
    CustomerModel(id=3, name="Charlie", email="charlie@example.com"),
]

products: list[ProductModel] = [
    ProductModel(id=1, name="Laptop", price=999.99, description="A high-performance laptop"),
    ProductModel(id=2, name="Smartphone", price=499.99, description="A latest model smartphone"),
    ProductModel(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones"),
]

cart_items : list[CartItemModel] = [
    CartItemModel(cart_id=1, product_id=1, quantity=1),
    CartItemModel(cart_id=1, product_id=2, quantity=2),
    CartItemModel(cart_id=2, product_id=3, quantity=1),
]

orders: list[OrderModel] = [
    OrderModel(order_id=1, customer_id=1, quantity=2, total_price=1499.98),
    OrderModel(order_id=2, customer_id=2, quantity=1, total_price=199.99),
    OrderModel(order_id=3, customer_id=3, quantity=3, total_price=299.97),
]