from flask import Flask, request, jsonify
import time
import random
import logging

app = Flask(__name__)

# Logger configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.route('/api/home', methods=['GET'])
def home():
    logging.info("Accessed Home Endpoint")
    return jsonify({"message": "Welcome to Log Analytics Platform!"})

@app.route('/api/data', methods=['POST'])
def data():
    data = request.json
    logging.info(f"Received data: {data}")
    return jsonify({"status": "Data received successfully"}), 201

@app.route('/api/random', methods=['GET'])
def random_data():
    num = random.randint(1, 100)
    logging.info(f"Generated random number: {num}")
    return jsonify({"random_number": num})

@app.route('/api/slow', methods=['GET'])
def slow():
    time.sleep(3)
    logging.warning("Slow response endpoint triggered")
    return jsonify({"message": "This response was delayed intentionally"}), 200

@app.route('/api/error', methods=['GET'])
def error():
    logging.error("Intentional error triggered")
    return jsonify({"error": "Something went wrong"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
