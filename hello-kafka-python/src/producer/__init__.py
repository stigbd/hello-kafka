from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers="localhost:9092")
TOPIC = "hello-kafka-events"


class MessagePayload:
    body: str


def send_message(topic: str, key: str, value: MessagePayload) -> None:
    """Encode and send the message to the topic."""
    try:
        producer.send(topic=topic, key=key.encode(), value=value.body.encode())
        producer.flush()
    except KafkaError as e:
        print(f"Exception: {e} ")

    print(f"Message delivered to {topic}.")


def main() -> int:
    print("Hello from hello-kafka-python producer!")
    while True:
        try:
            # Get the key and value from the user:
            key = input("key---->")
            payload = MessagePayload()
            payload.body = input("payload-->")

            # Send the message to the "hello-kafka-events" topic
            send_message(topic=TOPIC, key=key, value=payload)

        except KeyboardInterrupt:
            print("\nBye!")
            break

    return 0
