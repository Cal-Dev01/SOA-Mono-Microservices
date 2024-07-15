from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-details', methods=['GET'])
def get_details():
    user_id = request.args.get('user_id')
    item_id = request.args.get('item_id')
    order_id = request.args.get('order_id')

    user_response = requests.get(f'http://localhost:5006/user/{user_id}')
    item_response = requests.get(f'http://localhost:5007/inventory/{item_id}')
    order_response = requests.get(f'http://localhost:5008/shipping/{order_id}')

    return jsonify({
        "user": user_response.json(),
        "item": item_response.json(),
        "order": order_response.json()
    })


if __name__ == '__main__':
    app.run(port=5009)
