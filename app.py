from flask import Flask, request, jsonify
import db
import repository 
from models import Product 

app = Flask(__name__)

db.create()

@app.route("/product", methods=['POST'])
def add_product():
    data = request.get_json()
    print(data)
    repository.add_product(data['name'], data['price'])
    return jsonify({'result': 'success'})

@app.route("/products")
def all_products():
    products = repository.get_all_products()
    product_list = []
    for product in products:
        product_list.append(product.serialize())
    return jsonify({'products': product_list})

@app.route("/product", methods=['PUT'])
def update_product():
    data = request.get_json()
    product = Product(data['id'], data['name'], data['price'])
    repository.update_product(product)
    return jsonify({'result': 'success'})

@app.route("/product", methods=['GET'])
def find_product():
    data = request.get_json()
    product = repository.get_product(data['id'])
    return jsonify({'product': product.serialize()})

@app.route("/product", methods=['DELETE'])
def delete_product():
    data = request.get_json()
    product = repository.delete_product(data['id'])
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run()
