# hello-kafka

## Install the kafka binaries

## Start and stop the Kafka environment

I prefer the docker way.

Start the Kafka environment:

```shell
% docker run --name mykafkacontainer -p 9092:9092 apache/kafka:3.8.0
```

Stop and remove the Kafka environment:

```shell
% docker stop mykafkacontainer 
% docker rm mykafkacontainer
```

## Create a topic

```shell
% cd kafka_2.13-3.8.0
% bin/kafka-topics.sh --create --topic hello-kafka-events --bootstrap-server localhost:9092
```

## Write events to the topic

```shell
% bin/kafka-console-producer.sh --topic hello-kafka-events --bootstrap-server localhost:9092
>This my first event
>This is my second event
>
```

Stop the producer client with `Ctrl-C`.

## Read the events

```shell
% bin/kafka-console-consumer.sh --topic hello-kafka-events --from-beginning --bootstrap-server localhost:9092
This my first event
This is my second event
```

Stop the producer client with `Ctrl-C`.

## References

- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart)
