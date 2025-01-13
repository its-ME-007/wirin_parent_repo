import paho.mqtt.client as mqtt
import json
import time

# Define the MQTT broker address and port
broker = "localhost"
port = 1883  # Default MQTT port

# Define the topic for speed (since we are focusing on publishing speed)
topic = "speed"

# Publisher function
def publisher():
    client = mqtt.Client()
    client.connect(broker, port, 60)

    while True:
        try:
            # Get user input for the speed value
            speed_value = input("Enter the speed value to publish (or type 'exit' to quit): ")

            # Convert the input to an integer or float, depending on the requirement
            speed_value = float(speed_value)

            # Prepare the payload
            payload = {"speed": speed_value}
            payload_json = json.dumps(payload)  # Convert to JSON format

            # Publish the payload to the MQTT broker
            client.publish(topic, payload_json)
            print(f"Published to {topic}: {payload_json}")

            # Delay for 1 second before asking for input again
            time.sleep(1)

        except ValueError:
            print("Invalid input. Please enter a valid number for speed.")

if __name__ == "__main__":
    publisher()
