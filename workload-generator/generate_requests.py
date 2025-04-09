import requests
import random
import time
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

endpoints = ["/health", "/users", "/orders", "/fail", "/login", "/logout", "/register", "/profile", "/checkout", "/reviews", "/notifications", "/settings", "/admin", "/analytics", "/dashboard", "/support", "/search"]

while True:
    endpoint = random.choice(endpoints)
    start_time = time.time()
    try:
        r = requests.get(f"http://api:5000{endpoint}")
        response_time = (time.time() - start_time) * 1000  # in milliseconds

        log_message = {
            "timestamp": time.time(),
            "level": "INFO",
            "message": f"Called endpoint {endpoint} with status {r.status_code}",
            "endpoint": endpoint,
            "status_code": r.status_code,
            "response_time": response_time
        }
        print(log_message["message"])
    except Exception as e:
        response_time = (time.time() - start_time) * 1000

        log_message = {
            "timestamp": time.time(),
            "level": "ERROR",
            "message": f"Request to {endpoint} failed: {str(e)}",
            "endpoint": endpoint,
            "status_code": "error",
            "response_time": response_time
        }
        print(log_message["message"])

    producer.send('logs', log_message)
    producer.flush()
    time.sleep(1)
