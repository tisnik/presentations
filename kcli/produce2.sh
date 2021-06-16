#!/bin/bash

# Update the port accordingly (this one is for Kafka running inside Docker)
KAFKA_PORT=9092

# Produce messages from current directory
# All JSON files in current directory will be sent to Kafka via Kafkacat
for file in *.json
do
    echo $file
    kafkacat -b localhost:${KAFKA_PORT} -P -t partitioned -p 0 $file
    kafkacat -b localhost:${KAFKA_PORT} -P -t partitioned -p 1 $file
    kafkacat -b localhost:${KAFKA_PORT} -P -t partitioned -p 2 $file
    kafkacat -b localhost:${KAFKA_PORT} -P -t partitioned -p 3 $file
    kafkacat -b localhost:${KAFKA_PORT} -P -t partitioned -p 4 $file
    # It is possible to change the sleep value (or remove it completely)
    sleep 1
done
