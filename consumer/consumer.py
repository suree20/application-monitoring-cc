from kafka import KafkaConsumer
import psycopg2
import json
from datetime import datetime

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='log-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

conn = psycopg2.connect(
    dbname='logsdb', user='postgres', password='postgres', host='db', port='5432'
)
cursor = conn.cursor()

for message in consumer:
    log = message.value
    print("Received log:", log)
    log_time = datetime.fromtimestamp(log['timestamp'])
    cursor.execute(
        "INSERT INTO logs (timestamp, level, message, endpoint, response_time) VALUES (%s, %s, %s, %s, %s)",
        (log_time, log['level'], log['message'], log['endpoint'], log.get('response_time'))
    )
    conn.commit()
