#!/usr/bin/python3
"""this is for task 5"""
from flask import Flask
from flask import jsonify
from flask import request


users = {}


app = Flask(__name__)


@app.route("/")
def home():
    """this is the method"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status."""
    return 'OK'


@app.route("/users/<username>")
def get_user(username):
    """Return one user."""
    if username in users:
        return jsonify(users[username])
    else:
       return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)
