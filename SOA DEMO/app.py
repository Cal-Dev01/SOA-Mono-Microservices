from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order-details', methods=['GET'])
def get_order_details():
    order_id = request.args.get('order_id')
    response = requests.get(f'http://localhost:5020/order-details/{order_id}')

    if response.status_code != 200:
        return jsonify({"error": "ESB service error"}), response.status_code

    return jsonify(response.json())


if __name__ == '__main__':
    app.run(port=5005)
