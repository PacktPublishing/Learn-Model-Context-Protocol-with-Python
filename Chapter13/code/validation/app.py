from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    id: str
    name: str
    price: float

class Book(BaseModel):
    id: str
    title: str
    author: str
    pages: int
    abstract: str | None = None

product = { "id": "1", "name": "Product 1", "price": 10.0 }
book = { "id": "1", "title": "Book 1", "author": "Author 1", "pages": 100 }

# 2. safer way to validate
try:
   parsed_product = Product(**product)
   parsed_book = Book(**book)
   print(f"Parsed product: {parsed_product}")
   print(f"Parsed book: {parsed_book}")
except ValidationError as e:
    print(f"Validation error: {e}")

# crashes
try:
   product_crashable = { "id": "1", "name": "Product 1" }
   product_that_will_crash = Product(**product_crashable)
except ValidationError as e:
    print(f"Validation error: {e}")

class ComplexUser(BaseModel):
    id: str
    name: str
    age: int
    email: str
    is_active: bool
    attendance: dict[str, bool]

complex_user_data = { 
    "id": "1", 
    "name": "User 1", 
    "age": 30, 
    "email": "user1@example.com", 
    "is_active": True, 
    "attendance": { 
        "2023-01-01": True,
        "2023-01-02": False,
        "2023-01-03": True
    } 
}

complex = ComplexUser(**complex_user_data)
print(f"Complex user: {complex}")