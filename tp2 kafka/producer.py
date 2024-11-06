"""Partie 2 : Création de producer

1. Créer un second script “produce.py”

2. Instancier la classe KafkaProducer avec les bon paramètre. Le topic devra être “exo1”

3. Faire en sorte que le client envoie le message “coucou” suivi de votre nom

4. Lancer un second terminal et lancer votre script. Vérifier que vous et vos camarades reçoivent le message.
"""

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
for _ in range(10):
    producer.send('exo1', b'fe bour aou')
    producer.flush()