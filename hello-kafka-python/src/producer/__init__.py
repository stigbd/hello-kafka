from confluent_kafka import KafkaException, Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})
TOPIC = "hello-kafka-events"


class MessagePayload:
    body: str


def delivery_report(err, message):
    """Called once fo re ach message produced to indicate delivery result.

    Triggered by poll() or flush().
    """
    if err is not None:
        print(f"Messsage delivery failed: {err}")
    else:
        print(f"Message delivered to {message.topic()} [{message.partition()}]")


def send_message(topic: str, key: str, value: MessagePayload) -> None:
    """Encode and send the message to the topic."""
    producer.poll(0)

    producer.produce(
        topic=topic,
        key=key.encode(),
        value=value.body.encode(),
        on_delivery=delivery_report,
    )

    producer.flush()


def main() -> int:
    print("Hello from hello-kafka-python producer!")
    while True:
        try:
            # Get the key and value from the user:
            key = input("key---->")
            payload = MessagePayload()
            payload.body = input("payload-->")

            # Send the message to the "hello-kafka-events" topic
            try:
                send_message(topic=TOPIC, key=key, value=payload)
            except KafkaException as e:
                print(e)

        except KeyboardInterrupt:
            print("\nBye!")
            break

    return 0
