"""On veut pouvoir échanger du json entre consumer et producer. Pour rappel le json est un format de donnée textuel. 

1. Dans un nouveau fichier, Créer un second producer qui envoie des messages sous format json sur un topic nommé d'après votre nom de famille. Le message sera le suivant : 

{

   data: [[1, 2,], [3, 4]]

}

Il faudra penser à utiliser la librairie json et encoder le json en utf8 avant d'envoyer le message.

2. Dans un autre fichier, créer un second consumer. Il devra convertir le json reçu en dictionnaire et transformer le tableau de données en tableau numpy. calculer la somme des valeurs et afficher le resultat

Lancer deux consumer identique et lancer votre producer. Est ce que les deux consummer reçoivent le message ou un seul ?
"""

import json
from kafka import KafkaProducer
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers='51.38.185.58:9092')
#producer.send('processed_david_cyn', { # si besoin de tester le script process
#producer.send('chane-yock-nam', { # code de base
""" producer.send('prediction_david.chane-yock-nam', { #  si besoin de tester le script process

   "data" : [[1, 2,], [3, 4]]

}) """

producer.send('prediction_david.chane-yock-nam', { #  si besoin de tester model lineaire

   "data" : [[0.1, 0.2]]

})
producer.flush()