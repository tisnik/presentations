# Monitoring Apache Kafka

![Kafka logo](images/kafka_logo.png)



## Usage of Kafka

* Message broker on steroids
* Lambda architecture
* Kappa architecture
* Logging platform

![Kafka streams](images/kafka_streams.png)

![Kafka kappa](images/kafka_kappa.png)



## Kafka architecture

* (ZooKeeper)
* Message brokers



## Kafka Connect

* "Distributed scalable framework"
* Automatic consuming or producing data
    - with data persistence in-between
* Part of Apache Kafka
* Just configuration files
* And connectors



## Kafka Connect

* Sources
* Kafka Cluster
* Sinks


postgres=# create database kafka_source;
CREATE DATABASE
create table source(id numeric, name varchar, surname varchar);

postgres=# create database kafka_sink;
CREATE DATABASE
create table t1 (message varchar);


postgres://postgres:postgres@127.0.0.1:5432/kafka_source
postgres://postgres:postgres@127.0.0.1:5432/kafka_sink


## Use cases

### Moving data from one DB to another one

![Kafka_Connector_1](images/Kafka_Connect_1.png)

### Connection between MQTT and AWS SQS

![Kafka_Connector_2](images/Kafka_Connect_2.png)

### From one source to various sinks

* Amazon S3
* Logs
* Storage (database)

![Kafka_Connector_3](images/Kafka_Connect_3.png)

#### Custom consumers are possible

* Amazon S3
* Logs
* Storage (database)
* And bunch of custom consumers

![Kafka_Connector_4](images/Kafka_Connect_4.png)



## Kafka Connect from developers PoV

* Is separate process
* It requires no programming
    - failures handling
    - logging
    - monitoring
    - scaling
    - migrating
    - sec. handling etc.
* Lightweight data transformations



## JDBC source

* any insert/update/delete as event to Kafka



## Useful links

* [Apache Kafka vs. Middleware (MQ, ETL, ESB) – Slides + Video](https://www.kai-waehner.de/blog/2019/03/07/apache-kafka-middleware-mq-etl-esb-comparison/)

* [Discover Kafka® connectors and more](https://www.confluent.io/hub/?_ga=2.197519912.642206306.1675149141-1201563621.1675149140)

* [JDBC Connector (Source and Sink)](https://www.confluent.io/hub/confluentinc/kafka-connect-jdbc)

* [From Zero to Hero with Kafka Connect by Robin Moffatt](https://www.youtube.com/watch?v=Jkcp28ki82k)
