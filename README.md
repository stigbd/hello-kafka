# hello-kafka

A small project to play with [Apache Kafka](https://kafka.apache.org/) in shell, java and python.

In this README, Kafka's command line tools will be illustrated. For java and python, see the respective subdirectories' READMEs.

## About Kafka

### The core concepts

#### Server

Kafka is run as a cluster of one or more servers that can span multiple datacenters or cloud regions.

#### Client

An application that read, write and process streams of events.

#### Broker

A server forming the storage layer.

#### Event

An event records the fact that "something happened" in the world or in your business.

Also called __record__ or __message__. An event has the following parts:

- key: a serial number or UUID, determines the partition to which an event get's appended to
- value: the payload of the message
- timestamp
- headers (optional)

The messages are guaranteed to be processed in order only if they share the same key.

#### Topics

Events are organized and stored in topics, similar to a folder in a filesystem.

#### Partition

 A topic is spread over a number of partitions ("buckets") located on different brokers.

Note: Events with the same key are written to the same partition.

#### Producer

A client that publish (write) an event to a broker.

#### Consumer

A client that subscribe to (read and process) an event on a broker.

#### Consumer group

A group of consumers that work together to consume a topic. Each partition is consumed by exactly one consumer within each subscribing consumer group at any given time.

### Start and stop the Kafka environment

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

### Using Kafka CLI

#### Install the Kafka binaries

Download the latest Kafka binary relase from [here](https://www.apache.org/dyn/closer.cgi?path=/kafka/3.8.0/kafka_2.13-3.8.0.tgz)

Unzip it into a directory in the root of this project.

```shell
% tar -xzf kafka_2.13-3.8.0.tgz
```

#### Create a topic

```shell
% cd kafka_2.13-3.8.0
% bin/kafka-topics.sh --create --topic hello-kafka-events --bootstrap-server localhost:9092
```

#### Write events to the topic

```shell
% bin/kafka-console-producer.sh --topic hello-kafka-events --bootstrap-server localhost:9092 --property "parse.key=true" --property "key.separator=:"
>This my first event
>This is my second event
>
```

Stop the producer client with `Ctrl-C`.

#### Read the events

```shell
% bin/kafka-console-consumer.sh --topic hello-kafka-events --from-beginning --bootstrap-server localhost:9092
This my first event
This is my second event
```

Stop the producer client with `Ctrl-C`.

#### Using kcat

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
- [Documentation](https://kafka.apache.org/documentation/)
- [Apache Kafka Docker](https://hub.docker.com/r/apache/kafka)
- [Manjula Piyumal (2024), Mastering Kafka: Advanced Concepts Every Senior Software Engineer Should Know](https://manjulapiyumal.medium.com/mastering-kafka-advanced-concepts-every-senior-software-engineer-should-know-9283664c99e1)
