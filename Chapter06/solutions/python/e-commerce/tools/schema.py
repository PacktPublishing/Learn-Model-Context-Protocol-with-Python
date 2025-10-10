from pydantic import BaseModel

class AddCartInputModel(BaseModel):
    cart_id: int
    product_id: int
    quantity: int

class AddInputModel(BaseModel):
    a: float
    b: float

class CategoryModel(BaseModel):
    name: str
    description: str

class CustomerModel(BaseModel):
    id: int
    name: str
    email: str

class ProductModel(BaseModel):
    id: int
    name: str
    price: float
    description: str

class CartItemModel(BaseModel):
    cart_id: int
    product_id: int
    quantity: int

class OrderModel(BaseModel):
    order_id: int
    customer_id: int
    quantity: int
    total_price: float

class GetOrderInputModel(BaseModel):
    customer_id: int

class GetProductInputModel(BaseModel):
    product_id: int