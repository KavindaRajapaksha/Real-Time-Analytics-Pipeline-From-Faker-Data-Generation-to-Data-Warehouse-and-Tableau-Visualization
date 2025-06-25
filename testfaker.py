from faker import Faker
import random
import time
import json


faker = Faker()


def generate_order():
    return {
        "order_id": faker.uuid4(),
        "customer_name": faker.name(),
        "email": faker.email(),
        "product_name": faker.word(),
        "category": faker.random_element(elements=("Electronics", "Books", "Clothing", "Home", "Beauty")),
        "price": round(random.uniform(5.00, 500.00), 2),
        "quantity": random.randint(1, 5),
        "total_amount": 0.0,  
        "order_time": faker.iso8601()
    }


while True:
    order = generate_order()
    order["total_amount"] = round(order["price"] * order["quantity"], 2)
    
    print(json.dumps(order, indent=2))  
    time.sleep(2)  
