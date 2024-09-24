# hello-kafka-java

For starting and stopping the Kafka environment, see [here](../README.md#start-and-stop-the-kafka-environment).

## Building and running locally

### Building the project

```bash
% ./gradlew clean build
```

### Running the consumer

```bash
% ./gradlew :consumer:bootRun
```

### Running the producer

```bash
% ./gradlew :producer:bootRun
```

### Post a message to the producer

```bash
% curl -i -H "Content-Type: text/plain" -d "hello" -X POST http://localhost:8080/message
```

## References

[Introduction to Apache Kafka](https://www.baeldung.com/apache-kafka)
[Intro to Apache Kafka with Spring](https://www.baeldung.com/spring-kafka)
[Apache Kafka Series](https://www.baeldung.com/apache-kafka-series)

[Gradle Multi-Project Build Basics](https://docs.gradle.org/current/userguide/intro_multi_project_builds.html)
