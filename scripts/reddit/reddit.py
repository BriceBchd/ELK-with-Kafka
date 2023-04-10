import os
import praw
import logging
import ecs_logging
from dotenv import load_dotenv
from datetime import datetime, timedelta
from random import randint
from time import sleep

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configuration des identifiants de l'API Reddit
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")

# Configuration du logger avec le format ECS standard
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
date = datetime.utcnow().strftime("%Y-%m-%d")
handler = logging.FileHandler(f"/home/data/reddit/reddit.{date}.log")
handler.setLevel(logging.INFO)
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

# Configuration d'un second handler pour la sortie standard
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

# Connexion à l'API Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="praw-script",
)


# Fonction pour récupérer les subreddits les plus populaires actuellement
def get_popular_subreddits():
    subreddits = reddit.subreddit("all").search(
        query="elasticsearch", sort="new", limit=10
    )
    return subreddits


# Boucle pour récupérer les subreddits et les écrire dans le fichier de log
while True:
    try:
        subreddits = get_popular_subreddits()
        for subreddit in subreddits:
            logger.info(
                {
                    "title": subreddit.title,
                    "url": subreddit.url,
                    "created_utc": subreddit.created_utc,
                }
            )
        sleep(randint(60, 300))
    except Exception as e:
        logger.error(str(e))
        break
