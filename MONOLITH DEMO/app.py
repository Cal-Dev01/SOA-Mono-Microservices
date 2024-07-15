from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Eve", "age": 35},
    2: {"name": "Frank", "age": 29}
}

inventory = {
    1: {"item": "Monitor", "quantity": 75},
    2: {"item": "Keyboard", "quantity": 150}
}

shipping_info = {
    1: {"status": "delivered", "carrier": "DHL"},
    2: {"status": "in transit", "carrier": "USPS"}
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/details', methods=['GET'])
def get_details():
    user_id = int(request.args.get('user_id'))
    item_id = int(request.args.get('item_id'))
    order_id = int(request.args.get('order_id'))

    user = users.get(user_id, "User not found")
    item = inventory.get(item_id, "Item not found")
    shipping = shipping_info.get(order_id, "Order not found")

    return jsonify({
        "user": user,
        "item": item,
        "order": shipping
    })


if __name__ == '__main__':
    app.run(port=5010)
