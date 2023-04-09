# Scripts
This directory contains scripts to generate logs.

<br />

---

## reddit.py
This script generates a log of reddit posts. It uses the [PRAW](https://praw.readthedocs.io/en/latest/) library to access the reddit API.

To define le log format you can check the [Elastic Doc](https://www.elastic.co/guide/en/ecs-logging/python/current/installation.html).

---

#### Usage
Simply run the script with python3.
```bash
python3 reddit.py
```

---

#### Environment variables
The script uses the following environment variables:
- `REDDIT_CLIENT_ID`: The client id of the reddit app.
- `REDDIT_CLIENT_SECRET`: The client secret of the reddit app.
- `REDDIT_USER_AGENT`: The user agent of the reddit app.
- `REDDIT_PASSWORD`: The password of the reddit account.

You can set these variables in the `.env` file in the root directory of the project.

---

#### Cleaning the log
This script clean the log files older than 7 days.
```bash
find /home/data/reddit/ -name 'reddit.*.log' -mtime +7 -delete
```