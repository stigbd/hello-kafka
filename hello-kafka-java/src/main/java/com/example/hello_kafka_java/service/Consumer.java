package com.example.hello_kafka_java.service;

import java.util.Set;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class Consumer {

    Map<String, Set<String>> consumedRecords = new ConcurrentHashMap<>();

    @KafkaListener(topics = "hello-kafka-events", groupId = "group-java")
    public void consume(String message) {
        System.out.println("Consumed message: " + message);
    }
}
