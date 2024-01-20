import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../key/oneminutes-53fb9-firebase-adminsdk-u34vq-0bb95a36b3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('games').get()
for doc in docs:
    print(doc.to_dict())
