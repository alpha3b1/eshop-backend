from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pydantic import BaseModel
import json


fs_creds = credentials.Certificate("svcAccKey.json")
firebase_admin.initialize_app(fs_creds)
db = firestore.client()

class Product(BaseModel):
    name: str
    description: str
    coffee_type: str
    price: float


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello world"}

@app.get('/store-management/products')
def get_products():
    products = db.collection('products')

    all_products = products.get()
    product_list = []
    for doc in all_products:
        product_list.append(doc.to_dict())
    
    print(product_list)
    return({'products': product_list})



@app.post('/store-management/products')
def create_product(product: Product):
    products = db.collection('products')

    products.add(product) 
    return({"added":True})
