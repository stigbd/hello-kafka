package com.example.hello_kafka_java;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

import com.example.hello_kafka_java.config.KafkaConsumerConfig;

@SpringBootApplication
@Import(value = { KafkaConsumerConfig.class })
public class HelloKafkaJavaConsumerApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloKafkaJavaConsumerApplication.class, args);

	}
}
