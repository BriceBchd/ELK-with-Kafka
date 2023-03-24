# ELK-Docker

Dans ce fichier de configuration Docker Compose, vous pouvez voir que nous avons défini quatre services différents :

- zookeeper: Le service ZooKeeper est utilisé pour gérer la coordination des brokers Kafka.
- kafka: Le service Kafka est responsable du stockage et de la diffusion des messages.
- logstash: Le service Logstash est utilisé pour consommer les messages Kafka, les traiter et les envoyer à Elasticsearch.
- elasticsearch: Le service Elasticsearch est utilisé pour stocker les données de Logstash.
