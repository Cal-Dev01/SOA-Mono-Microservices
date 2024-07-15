from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/order-details/<int:order_id>', methods=['GET'])
def get_order_details(order_id):
    order_response = requests.get(f'http://localhost:5003/order/{order_id}')

    if order_response.status_code != 200:
        return jsonify({"error": "Order service error"}), order_response.status_code

    order_data = order_response.json()
    if "Order not found" in order_data:
        return jsonify(order_data), 404

    user_response = requests.get(f'http://localhost:5001/user/{order_data["user_id"]}')
    if user_response.status_code != 200:
        return jsonify({"error": "User service error"}), user_response.status_code

    product_response = requests.get(f'http://localhost:5002/product/{order_data["product_id"]}')
    if product_response.status_code != 200:
        return jsonify({"error": "Product service error"}), product_response.status_code

    return jsonify({
        "order": order_data,
        "user": user_response.json(),
        "product": product_response.json()
    })


if __name__ == '__main__':
    app.run(port=5020)
