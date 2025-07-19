import adafruit_dht
import board
import paho.mqtt.client as mqtt
import time
import json

dht = adafruit_dht.DHT11(board.D4)

MQTT_BROKER = "192.168.1.41"  # Replace with your Docker host IP
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/dht"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

while True:
    try:
        # Read sensor data
        temperature = dht.temperature
        humidity = dht.humidity
        
        if temperature is not None and humidity is not None:
            payload = json.dumps({
                "temperature": temperature,
                "humidity": humidity
            })
            client.publish(MQTT_TOPIC, payload)
            print(f"Published: {payload}")
        else:
            print("Failed to retrieve data from sensor")
            
    except RuntimeError as error:
        # DHT sensors can occasionally fail to read
        print(f"Reading error: {error.args[0]}")
        
    except Exception as error:
        # Handle other potential errors
        print(f"Unexpected error: {error}")
        
    time.sleep(60)