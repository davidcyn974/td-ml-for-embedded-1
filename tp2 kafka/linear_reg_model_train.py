from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=2, noise=1, random_state=42)
# Exemple : 100 maison, caractéristiques : surface, nombre de chambres , 
# prix à prédire

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

import joblib
joblib.dump(model, "my_linear_model.joblib")

# 3. Créer une fonction python qui charge le fichier de votre votre modèle et le retourne
def load_model():
    return joblib.load("my_linear_model.joblib")

# 4. Tester le modèle en utilisant la fonction predict et vérifier qu'il renvoie bien la prédiction
sample_to_be_tested = [[0.381,  0.974]]
print(model.predict(sample_to_be_tested))
# 5. Créer un consumer python. Il devra faire la prédiction avec le modèle à chaque donnée reçu. Dans un premier temps vous devrez seulement afficher la prédiction. 
import numpy as np
import json
from kafka import KafkaConsumer, KafkaProducer
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         bootstrap_servers='51.38.185.58:9092')
consumer = KafkaConsumer('prediction_david.chane-yock-nam',
                         bootstrap_servers="51.38.185.58:9092",
                         #group_id='1',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))
model = load_model()

for msg in consumer:
    data = msg.value.get('data')
    if data : 
        print("Message : ")
        print(msg)
        data_np = np.array(data)
        print("Prediction : ")
        pred = model.predict(data_np)
        print(pred)
        result = {
                'prediction': pred.tolist()
            }
        producer.send('prediction_david.chane-yock-nam', result)
        producer.flush()
        
    


