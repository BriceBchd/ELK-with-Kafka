import os
import praw
import logging
import ecs_logging
from dotenv import load_dotenv
from datetime import datetime
import json_log_formatter

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configuration des identifiants de l'API Reddit
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")


# Configuration du logger avec le format ECS standard
logger = logging.getLogger()
logger.setLevel(logging.INFO)
date = datetime.utcnow().strftime("%Y-%m-%d")
handler = logging.FileHandler(f"/home/data/reddit/reddit.{date}.log")
handler.setLevel(logging.INFO)
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

# Connexion à l'API Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="praw-script",
)

# Récupération des subreddits les plus populaires actuellement
subreddits = reddit.subreddit("all").top(limit=10)

# Ecriture des subreddits dans le fichier de log
for subreddit in subreddits:
    print(subreddit.title)
    logger.info(
        {
            "@timestamp": datetime.utcnow().isoformat(),
            "message": subreddit.title,
            "event": {"dataset": "reddit", "module": "subreddits", "category": "info"},
        }
    )
