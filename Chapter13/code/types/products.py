from typing import List, Dict, Literal, Optional, Union, Any

class Product:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

products: List[Product] = []

products.append(Product(id="1", name="Product 1", price=10.0))

if __name__ == "__main__":
   for p in products:
      print(f"{p.id}, {p.name}, {p.price}")
