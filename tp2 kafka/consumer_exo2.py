"""2. Dans un autre fichier, créer un second consumer. Il devra convertir le json reçu en dictionnaire et transformer le tableau de données en tableau numpy. calculer la somme des valeurs et afficher le resultat

Lancer deux consumer identique et lancer votre producer. Est ce que les deux consummer reçoivent le message ou un seul ?

"""


from kafka import KafkaConsumer
import json
import numpy as np

consumer = KafkaConsumer('chane-yock-nam', bootstrap_servers="51.38.185.58:9092", value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for msg in consumer:
    received = msg.value.get('data')
    data = np.array(received)
    print(data.sum())