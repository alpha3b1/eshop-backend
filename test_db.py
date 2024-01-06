import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


db = credentials.Certificate("svcAccKey.json")
firebase_admin.initialize_app(db)


db = firestore.client()

products = db.collection('products')
product_count =products.count().get()

print(product_count[0][0].value)
print(products.document().get().to_dict())
