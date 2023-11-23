import json
from bson import json_util

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def write_msg(name: str):
    for i in range(10):
        data = { 
            'tag ': 'blah',
            'name' : name,
            'index' : i,
            'score': 
            {
                'row1': 100,
                'row2': 200
            }
        }   
        producer.send('orders', json.dumps(data, default=json_util.default).encode('utf-8'))
