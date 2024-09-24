package com.example.hello_kafka_java;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

import com.example.hello_kafka_java.config.KafkaProducerConfig;

@SpringBootApplication
@Import(value = { KafkaProducerConfig.class })
public class HelloKafkaJavaProducerApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloKafkaJavaProducerApplication.class, args);

	}
}
