FROM openjdk:11-jre

RUN wget https://dlcdn.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz && \
    tar -xzf kafka_2.13-3.4.0.tgz && \
    mv kafka_2.13-3.4.0 /opt/kafka

WORKDIR /opt/kafka

COPY ./config ./config

EXPOSE 9092

CMD ["bin/kafka-server-start.sh", "config/server.properties"]