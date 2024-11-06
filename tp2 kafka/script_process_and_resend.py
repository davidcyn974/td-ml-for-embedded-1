"""
Un programme peut être à la fois consumer et producer. 

Faire un script process_and_resend.py qui lorsqu'il reçoit un json avec des données sous format numpy :

effectue la somme
et renvoie le résultat sur un autre topic nommé “processed”

"""

from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         bootstrap_servers='51.38.185.58:9092')
consumer = KafkaConsumer('processed_david_cyn',
                         bootstrap_servers="51.38.185.58:9092",
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for msg in consumer:
    received = msg.value.get('data')  # Get 'data' from the message
    if received:
        data = np.array(received) 
        data_sum = int(data.sum())
        result = {
            'sum': data_sum
        }
        producer.send('processed_david_cyn', result)
        producer.flush()
        print(f"Result: {result}")