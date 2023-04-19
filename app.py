from flask import Flask, request, jsonify, render_template
import db
import repository 
from models import Product 

app = Flask(__name__)

db.create()

@app.route("/api/product", methods=['POST'])
def add_product():
    data = request.get_json()
    print(data)
    repository.add_product(data['name'], data['price'])
    return jsonify({'result': 'success'})

@app.route("/api/products")
def all_products():
    products = repository.get_all_products()
    product_list = []
    for product in products:
        product_list.append(product.serialize())
    return jsonify({'products': product_list})

@app.route("/api/product", methods=['PUT'])
def update_product():
    data = request.get_json()
    product = Product(data['id'], data['name'], data['price'])
    repository.update_product(product)
    return jsonify({'result': 'success'})

@app.route("/api/product/<id>", methods=['GET'])
def find_product(id):
    product = repository.get_product(id)
    return jsonify({'product': product.serialize()})

@app.route("/api/product", methods=['DELETE'])
def delete_product():
    data = request.get_json()
    product = repository.delete_product(data['id'])
    return jsonify({'result': 'success'})

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/add/product")
def add_product_form():
    return render_template("add_product.html")

@app.route("/edit/product/<id>")
def edit_product_form(id):
    return render_template("edit_product.html", id=id)

@app.route("/delete/product/<id>")
def delete_product_form(id):
    return render_template("delete_product.html", id=id)

if __name__ == '__main__':
    app.run()
