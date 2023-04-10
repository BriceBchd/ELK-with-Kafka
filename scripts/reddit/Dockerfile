# Utiliser une image Python 3.9 officielle
FROM python:3.9-slim-buster

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter l'application
CMD [ "python", "reddit.py" ]