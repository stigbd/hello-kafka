from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})
TOPIC = "hello-kafka-events"


class Message:
    key: int
    value: str


def delivery_report(err, msg):
    """Called once fo re ach message produced to indicate delivery result.

    Triggered by poll() or flush().
    """
    if err is not None:
        print(f"Messsage delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def send_message(topic: str, message: Message) -> None:
    """Encode and send the message to the topic."""
    producer.poll(0)

    producer.produce(
        topic=topic,
        key=message.key.encode(),
        value=message.value.encode(),
        callback=delivery_report,
    )

    producer.flush()


def main() -> int:
    print("Hello from hello-kafka-python producer!")
    while True:
        try:
            # Get the key and value from the user:
            message = Message()
            message.key = input("key---->")
            message.value = input("value-->")

            # Send the message to the "hello-kafka-events" topic
            send_message(TOPIC, message)

        except KeyboardInterrupt:
            print("\nBye!")
            break

    return 0
