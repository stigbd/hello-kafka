from confluent_kafka import Consumer

consumer = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "hello-kafka-python",
    }
)

topic = "hello-kafka-events"
consumer.subscribe([topic])


def print_messages() -> None:
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                pass
            elif msg.error():
                print(f"ERROR: {msg.error()}")
            else:
                print(
                    f"Consumed event from topic {topic}: key = {msg.key().decode()} value = {msg.value().decode()}"
                )

    except KeyboardInterrupt:
        print("\nBye!")
    finally:
        consumer.close()


def main() -> int:
    print("Hello from hello-kafka-python consumer!")
    print_messages()
    return 0
