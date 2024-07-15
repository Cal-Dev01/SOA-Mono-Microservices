from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/shipping/<int:order_id>', methods=['GET'])
def get_shipping(order_id):
    shipping_info = {
        1: {"status": "shipped", "carrier": "UPS"},
        2: {"status": "pending", "carrier": "FedEx"}
    }
    return jsonify(shipping_info.get(order_id, "Order not found"))


if __name__ == '__main__':
    app.run(port=5008)
