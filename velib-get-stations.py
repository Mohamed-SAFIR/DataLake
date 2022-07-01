#stocker les données de station de vélos dans des messages Kafka :

import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "271d02bad1d8ae0d11b958ab299240de7b9eb15b" # clé l'API
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())# stocké dans Kafka sous la forme d'une chaîne de caractères au format JSON
    for station in stations:
        producer.send("velib-stations", json.dumps(station).encode())
    print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1) # réaliser un appel à l'API toutes les secondes