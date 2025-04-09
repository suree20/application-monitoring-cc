from flask import Flask, jsonify
import logging
import random
import time

app = Flask(__name__)
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

@app.route("/health")
def health():
    logging.info("Health check accessed")
    return jsonify({"status": "ok"})

@app.route("/users")
def users():
    logging.info("Users endpoint hit")
    return jsonify(["user1", "user2"])

@app.route("/orders")
def orders():
    logging.info("Orders endpoint hit")
    return jsonify({"orders": [1, 2, 3]})

@app.route("/fail")
def fail():
    logging.error("Simulated error")
    return jsonify({"error": "Simulated failure"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)