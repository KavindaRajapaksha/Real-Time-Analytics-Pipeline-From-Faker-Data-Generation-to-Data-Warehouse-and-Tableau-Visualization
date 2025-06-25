from faker import Faker
from kafka import KafkaProducer
import json
import time
import random

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {
        'user_id': fake.uuid4(),
        'user_name': fake.name(),
        'product': fake.word(),
        'price': round(random.uniform(10, 1000), 2),
        'timestamp': fake.iso8601()
    }

topic = 'transactions'

for _ in range(10000):  # Simulate 10,000 events
    event = generate_transaction()
    producer.send(topic, event)
    print(f"Produced: {event}")
    time.sleep(0.01)  # 10ms interval


producer.flush()
producer.close()