from flask import Flask, jsonify
import logging

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

@app.route("/login")
def login():
    logging.info("/login endpoint hit")
    return jsonify({"message": "Login endpoint accessed"})

@app.route("/logout")
def logout():
    logging.info("/logout endpoint hit")
    return jsonify({"message": "Logout endpoint accessed"})

@app.route("/register")
def register():
    logging.info("/register endpoint hit")
    return jsonify({"message": "Register endpoint accessed"})

@app.route("/profile")
def profile():
    logging.info("/profile endpoint hit")
    return jsonify({"message": "Profile endpoint accessed"})

@app.route("/checkout")
def checkout():
    logging.info("/checkout endpoint hit")
    return jsonify({"message": "Checkout endpoint accessed"})

@app.route("/reviews")
def reviews():
    logging.info("/reviews endpoint hit")
    return jsonify({"message": "Reviews endpoint accessed"})

@app.route("/notifications")
def notifications():
    logging.info("/notifications endpoint hit")
    return jsonify({"message": "Notifications endpoint accessed"})

@app.route("/settings")
def settings():
    logging.info("/settings endpoint hit")
    return jsonify({"message": "Settings endpoint accessed"})

@app.route("/admin")
def admin():
    logging.info("/admin endpoint hit")
    return jsonify({"message": "Admin endpoint accessed"})

@app.route("/analytics")
def analytics():
    logging.info("/analytics endpoint hit")
    return jsonify({"message": "Analytics endpoint accessed"})

@app.route("/dashboard")
def dashboard():
    logging.info("/dashboard endpoint hit")
    return jsonify({"message": "Dashboard endpoint accessed"})

@app.route("/support")
def support():
    logging.info("/support endpoint hit")
    return jsonify({"message": "Support endpoint accessed"})

@app.route("/search")
def search():
    logging.info("/search endpoint hit")
    return jsonify({"message": "Search endpoint accessed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
