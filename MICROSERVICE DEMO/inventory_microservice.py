from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory(item_id):
    inventory = {
        1: {"item": "Tablet", "quantity": 100},
        2: {"item": "Headphones", "quantity": 50}
    }
    return jsonify(inventory.get(item_id, "Item not found"))


if __name__ == '__main__':
    app.run(port=5007)
