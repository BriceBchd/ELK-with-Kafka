# ELK-Docker

## Description
This project is a POC to test the ELK stack with Kafka and Filebeat.
The dataflow is the following:
- RedditAPI/FakeECS  -> Kafka -> Filebeat -> Logstash -> Elasticsearch -> Kibana

## Requirements
- Docker
- Docker compose
- Internet 🤖
- 4GB RAM

## Usage
### Reddit script
```bash
cd scripts/reddit
docker-compose up -d
```

### Fake ECS script
```bash
cd scripts/fake-ecs
docker-compose up -d
```

### Kafka
```bash
cd kafka
docker-compose up -d
```

### Filebeat
```bash
cd filebeat
docker-compose up -d
```


## Todos:
- [x] Reddit script
    - [x] Add a script to generate logs from the reddit API.
    - [x] Update script to generate logs every random seconds.
    - [x] Dockerize the reddit scripts.
    - [x] Docker compose the reddit scripts.
- [x] Fake ECS logs
    - [x] Add a script to generate fake apache logs.
    - [x] Update script to generate logs every random seconds.
    - [x] Dockerize the fake apache logs. 
    - [x] Docker compose the fake apache logs.
- [x] Kafka
    - [x] Zookeeper-Kafka local
    - [x] Zookeeper-Kafka docker compose
    - [x] Zookeeper-Kafka docker compose config auto topics
    - [x] Zookeeper-Kafka docker compose config auto partitions & replicas
- [x] Beats
    - [x] Filebeat local
    - [x] Filebeat docker compose
    - [x] Filebeat CasC 
    - [x] Filebeat connected to kafka
    - [x] Filebeat setup input fake-ecs
- [ ] Logstash
    - [ ] Logstash docker compose
    - [ ] Logstash CasC
    - [ ] Logstash input kafka
    - [ ] Logstash output elasticsearch
    - [ ] Logstash filter transform etc...
- [ ] Elasticsearch
    - [ ] Elasticsearch docker compose
    - [ ] Elasticsearch CasC
    - [ ] Elasticsearch index template
    - [ ] Elasticsearch index lifecycle
    - [ ] Elasticsearch index rollover
- [ ] Kibana
    - [ ] Kibana docker compose
    - [ ] Kibana CasC
    - [ ] Kibana index pattern
    - [ ] Kibana dashboard