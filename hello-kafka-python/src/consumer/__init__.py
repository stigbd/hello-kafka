from kafka import KafkaConsumer


def print_messages() -> None:
    consumer = KafkaConsumer(
        bootstrap_servers="localhost:9092",
        key_deserializer=lambda k: k.decode("utf-8"),
        value_deserializer=lambda v: v.decode("utf-8"),
    )

    consumer.subscribe(["hello-kafka-events"])

    try:
        for msg in consumer:
            print(msg)
    except KeyboardInterrupt:
        print("\nBye!")


def main() -> int:
    print("Hello from hello-kafka-python consumer!")
    print_messages()
    return 0
