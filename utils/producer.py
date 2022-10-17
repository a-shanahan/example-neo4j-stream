import uuid
from kafka import KafkaProducer
import json
import random

producer = KafkaProducer(bootstrap_servers='localhost:29092')
topic = 'example-topic'

categories = ['Person', 'Org', 'GPE']
entity = ['Example-1', 'Example-2', 'Example-3']

for _ in range(10):
    msg = json.dumps({'entity': random.choice(entity),
                      'category': random.choice(categories),
                      'docID': uuid.uuid4().hex}).encode('utf-8')
    ack = producer.send(topic, msg)
    metadata = ack.get()
