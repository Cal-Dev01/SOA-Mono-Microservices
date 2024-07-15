from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    orders = {
        1: {"user_id": 1, "product_id": 1, "quantity": 2},
        2: {"user_id": 2, "product_id": 2, "quantity": 1}
    }
    return jsonify(orders.get(order_id, "Order not found"))


if __name__ == '__main__':
    app.run(port=5003)
