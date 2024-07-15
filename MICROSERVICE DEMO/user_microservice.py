from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {"name": "Charlie", "age": 28},
        2: {"name": "Dana", "age": 22}
    }
    return jsonify(users.get(user_id, "User not found"))


if __name__ == '__main__':
    app.run(port=5006)
