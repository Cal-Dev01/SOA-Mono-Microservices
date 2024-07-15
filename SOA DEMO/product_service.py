from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    products = {
        1: {"name": "Laptop", "price": 1200},
        2: {"name": "Phone", "price": 800}
    }
    return jsonify(products.get(product_id, "Product not found"))


if __name__ == '__main__':
    app.run(port=5002)
