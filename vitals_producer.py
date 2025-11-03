import json
import os
import time
import random
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

output_topic = os.getenv("OUTPUT_TOPIC")
bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS")
sasl_username = os.getenv("SASL_USERNAME")
sasl_password = os.getenv("SASL_PASSWORD")
interval_ms = int(os.getenv("INTERVAL_MS"))
security_protocol = os.getenv("SECURITY_PROTOCOL")
sasl_mechanism = os.getenv("SASL_MECHANISM")

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)  # Realistic body temp
    heart_rate = random.randint(60, 100)  # Realistic heart rate
    systolic = random.randint(110, 140)  # Realistic systolic pressure
    diastolic = random.randint(70, 90)  # Realistic diastolic pressure
    breaths = random.randint(12, 20)  # Realistic breaths per minute
    oxygen = random.randint(95, 100)  # Realistic oxygen saturation
    glucose = random.randint(70, 140)  # Realistic blood glucose

    return {
        "body_temp": body_temp,
        "heart_rate": heart_rate,
        "systolic": systolic,
        "diastolic": diastolic,
        "breaths": breaths,
        "oxygen": oxygen,
        "glucose": glucose
    }

while True:
    vitals = generate_vitals()
    producer.send(output_topic, vitals)
    print(f"Sent: {vitals}")
    time.sleep(interval_ms / 1000)
