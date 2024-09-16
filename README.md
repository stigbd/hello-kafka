# hello-kafka

A small project to play with [Apache Kafka](https://kafka.apache.org/) in shell, java and python.

In this README, Kafka's command line tools will be illustrated. For java and python, see the respective subdirectories' READMEs.

## Start and stop the Kafka environment

I prefer the docker way.

Start the Kafka environment:

```shell
% docker run --name kafka0 -p 9092:9092 apache/kafka:3.8.0
```

Stop and remove the Kafka environment:

```shell
% docker stop kafka0 
% docker rm kafka0
```

## Using Kafka CLI

### Install the Kafka binaries

Download the latest Kafka binary relase from [here](https://www.apache.org/dyn/closer.cgi?path=/kafka/3.8.0/kafka_2.13-3.8.0.tgz)

Unzip it into a directory in the root of this project.

```shell
% tar -xzf kafka_2.13-3.8.0.tgz
```

### Create a topic

```shell
% cd kafka_2.13-3.8.0
% bin/kafka-topics.sh --create --topic hello-kafka-events --bootstrap-server localhost:9092
```

### Write events to the topic

```shell
% bin/kafka-console-producer.sh --topic hello-kafka-events --bootstrap-server localhost:9092 --property "parse.key=true" --property "key.separator=:"
>This my first event
>This is my second event
>
```

Stop the producer client with `Ctrl-C`.

### Read the events

```shell
% bin/kafka-console-consumer.sh --topic hello-kafka-events --from-beginning --bootstrap-server localhost:9092
This my first event
This is my second event
```

Stop the producer client with `Ctrl-C`.

### Using kcat

[kcat](https://github.com/edenhill/kcat) can be installed by doing

```shell
% sudo apt install kcat
```

Count the number of messages in a topic and exit:

```shell
% kcat -C -b localhost:9092 -t hello-kafka-events -e -q
```

## References

- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart)
