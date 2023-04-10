from faker import Faker
import numpy as np
import datetime
import json

fake = Faker()


# Génère un message de log aléatoire au format ECS
def generate_log():
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    message = fake.text(max_nb_chars=100)
    log_level = np.random.choice(
        ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"], p=[0.05, 0.15, 0.50, 0.20, 0.10]
    )
    http_method = np.random.choice(
        ["GET", "POST", "PUT", "DELETE"], p=[0.4, 0.3, 0.2, 0.1]
    )
    response_code = np.random.choice(
        [200, 201, 204, 301, 302, 400, 401, 403, 404, 500, 503],
        p=[0.25, 0.05, 0.05, 0.10, 0.10, 0.10, 0.05, 0.05, 0.10, 0.10, 0.05],
    )
    logger_name = fake.word()
    file_name = fake.file_name()
    line_number = np.random.randint(1, 1000)
    function_name = "generate_logs()"
    service_name = "brice-training"
    service_version = "1.0"
    service_environment = np.random.choice(["dev", "test", "prod"], p=[0.3, 0.2, 0.5])
    event_dataset = "fake.log"

    log = {
        "@timestamp": timestamp,
        "message": message,
        "http.request.method": http_method,
        "http.response.status_code": int(response_code),
        "log.level": log_level,
        "log.logger": logger_name,
        "log.origin.file.name": file_name,
        "log.origin.file.line": int(line_number),
        "log.origin.function": function_name,
        "service.name": service_name,
        "service.version": service_version,
        "service.environment": service_environment,
        "event.dataset": event_dataset,
    }
    return json.dumps(log)


# Écrit un certain nombre de logs aléatoires dans un fichier
def generate_logs(num_logs, file_path):
    with open(file_path, "w") as f:
        for i in range(num_logs):
            log = generate_log()
            f.write(log + "\n")


# Exemple d'utilisation : génère 10 logs aléatoires dans le fichier "logs.txt"
generate_logs(10, "./logs.txt")
