# ELK-Docker

Dans ce fichier de configuration Docker Compose, vous pouvez voir que nous avons défini quatre services différents :

- zookeeper: Le service ZooKeeper est utilisé pour gérer la coordination des brokers Kafka.
- kafka: Le service Kafka est responsable du stockage et de la diffusion des messages.
- logstash: Le service Logstash est utilisé pour consommer les messages Kafka, les traiter et les envoyer à Elasticsearch.
- elasticsearch: Le service Elasticsearch est utilisé pour stocker les données de Logstash.


## Scripts

Ce répertoire contient des scripts pour générer des logs.
Todos:
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