import os

from kafka import KafkaConsumer
from kafka.errors import KafkaError

consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
)

topic = "hello-kafka-events"
consumer.subscribe([topic])


def print_message(message) -> None:
    """Prints message to the standard output."""
    print(
        f"Consumed message from topic {topic}:",
        f"\tkey: {message.key.decode()}",
        f"\tvalue size: {len(message.value)}",
        f"\tvalue: {message.value.decode()}",
        f"\theaders: {message.headers}",
        f"\ttimestamp: {message.timestamp}",
        f"\ttimestamp_type: {message.timestamp_type}",
        f"\tpartition: {message.partition}",
        f"\toffset: {message.offset}",
        sep=os.linesep,
    )


def consume_messages() -> None:
    """Consumes messages from topic until user interupts."""
    try:
        for message in consumer:
            print_message(message)
    except KeyboardInterrupt:
        print("\nBye!")
    finally:
        try:
            consumer.close()
        except KafkaError:
            pass


def main() -> int:
    """Consume messages."""
    print("Hello from hello-kafka-python consumer!")
    consume_messages()
    return 0
