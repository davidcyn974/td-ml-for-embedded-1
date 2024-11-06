from kafka import KafkaConsumer
# connect to ssh ubuntu@20.86.55.5
consumer = KafkaConsumer('exo1', bootstrap_servers="51.38.185.58:9092")
for msg in consumer:
    print (msg)