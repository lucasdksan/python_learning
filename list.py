df = [number for number in range(111)]

print(df)

products = [
    {"name": "Product 1", "price": 100},
    {"name": "Product 2", "price": 200},
    {"name": "Product 3", "price": 300},
]

new_products = [{ **product, "price": product["price"] * 1.01 } for product in products]

print(new_products)

new_products_flat = [product["price"] * 1.01 if product["price"] > 200 else product["price"] for product in products]

print(new_products_flat)

list = [n for n in range(100)]

new_list = [n for n in list if n % 2 == 0]

print(new_list)