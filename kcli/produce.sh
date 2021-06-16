#!/bin/bash

# Update the port accordingly (this one is for Kafka running inside Docker)
KAFKA_PORT=9092

# Produce messages from current directory
# All JSON files in current directory will be sent to Kafka via Kafkacat
for file in *.json
do
    echo $file
    kafkacat -b localhost:${KAFKA_PORT} -P -t results $file
    # It is possible to change the sleep value (or remove it completely)
    sleep 1
done
