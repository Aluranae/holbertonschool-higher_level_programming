from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/', methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=["GET"])
def get_data():
    data = list(users.keys())
    return jsonify(data), 200


@app.route('/status', methods=["GET"])
def status():
    return "OK"


@app.route('/users/<username>', methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
