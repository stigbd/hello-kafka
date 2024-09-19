import os

from confluent_kafka import Consumer, KafkaException, Message

consumer = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "hello-kafka-python",
    }
)

topic = "hello-kafka-events"
consumer.subscribe([topic])


def print_message(message: Message) -> None:
    """Prints message to the standard output."""
    print(
        f"Consumed message from topic {topic}:",
        f"\tkey: {message.key().decode()}",
        f"\tvalue size: {len(message)}",
        f"\tvalue: {message.value().decode()}",
        f"\theaders: {message.headers()}",
        f"\ttimestamp: {message.timestamp()}",
        f"\tpartition: {message.partition()}",
        f"\toffset: {message.offset()}",
        f"\tleader epoch: {message.leader_epoch()}",
        sep=os.linesep,
    )


def consume_messages() -> None:
    """Consumes messages from topic until user interupts."""
    try:
        while True:
            message = consumer.poll(1.0)
            if message is None:
                pass
            elif message.error():
                print(f"ERROR: {message.error()}")
            else:
                print_message(message)

    except KeyboardInterrupt:
        print("\nBye!")
    finally:
        try:
            consumer.close()
        except KafkaException:
            pass


def main() -> int:
    """Consume messages."""
    print("Hello from hello-kafka-python consumer!")
    consume_messages()
    return 0
