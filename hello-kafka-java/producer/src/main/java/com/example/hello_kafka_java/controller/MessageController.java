package com.example.hello_kafka_java.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.hello_kafka_java.service.Producer;

@RestController
@RequestMapping("/message")
class MessageController {

    private final Producer producer;

    public MessageController(Producer producer) {
        this.producer = producer;
    }

    @PostMapping
    public void sendMessage(@RequestBody String message) {
        producer.sendMessage(message);
    }
}
