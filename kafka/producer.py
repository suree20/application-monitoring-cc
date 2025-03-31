from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_log():
    endpoints = ["/api/home", "/api/data", "/api/random", "/api/slow", "/api/error"]
    for _ in range(10):
        log_data = {
            "endpoint": random.choice(endpoints),
            "response_time": round(random.uniform(0.1, 3.0), 2),
            "status": random.choice([200, 400, 500])
        }
        producer.send("logs", log_data)
        time.sleep(1)

if __name__ == "__main__":
    send_log()
