import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../../key/oneminutes-53fb9-firebase-adminsdk-u34vq-0bb95a36b3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    "id": 3,
    "title": "game3",
    "description": "game3 description",
    'image_url': 'test.png',
    'max_pod': 8000,
    "is_open": True,
    "is_legend": False,
    "start": datetime.datetime(2024, 1, 1, 00, 00, 00, 0000),
    "end": datetime.datetime(2024, 2, 28, 23, 59, 59, 0000),
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection("games").add(data)

