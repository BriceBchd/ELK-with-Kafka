# Kafka

### Commands
```bash
docker build -t bricebchd/zookeeper -f Dockerfile.zookeeper .
docker build -t bricebchd/kafka -f Dockerfile.kafka .
```

### Run Locally
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092 --replication-factor 3 --partitions 1 
bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic quickstart-events --from-beginning
sudo filebeat -e -c /home/brice/ELK-Docker/beats/filebeat.yml
```