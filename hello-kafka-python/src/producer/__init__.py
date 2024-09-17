from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

class Message:
    key: int
    value: str

def send_message(topic: str, message: Message) -> None:
    """Encode and send the message to the topic."""
    producer.send(topic=topic, key=message.key.encode(), value=message.value.encode())


def main() -> int:
    print("Hello from hello-kafka-python producer!")
    while True:
        try:
            # Get the key and value from the user:
            message = Message()
            message.key = input("key---->")
            message.value = input("value-->")

            # Send the message to the "hello-kafka-events" topic
            send_message("hello-kafka-events", message)

        except KeyboardInterrupt:
            print("\nBye!")
            break

    return 0
