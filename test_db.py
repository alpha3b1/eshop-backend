import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


db = credentials.Certificate("svcAccKey.json")
firebase_admin.initialize_app(db)


db = firestore.client()

products = db.collection('products')
product_count =products.count().get()

print(product_count[0][0].value)
all_products = products.get()

all_prods = []
for doc in all_products:
    all_prods.append(doc.to_dict())

print({"products" : all_prods})


