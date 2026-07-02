---
title: "RQ: Using RQ on Heroku"
source: https://python-rq.org/patterns/
domain: rq-queue
license: CC-BY-SA-4.0
tags: python rq, redis queue library, rq task worker
fetched: 2026-07-02
---

# RQ: Using RQ on Heroku

- Home
- Docs
- Patterns
- Contributing
- Chat

- Heroku
- Django
- Sentry
- Supervisor
- Systemd

## Using RQ on Heroku

To setup RQ on Heroku, first add it to your `requirements.txt` file:

```plaintext
redis>=3
rq>=0.13
```

Create a file called `run-worker.py` with the following content (assuming you are using Heroku Data For Redis with Heroku):

```python
import os
import redis
from redis import Redis
from rq import Queue, Connection
from rq.worker import HerokuWorker as Worker

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL')
if not redis_url:
    raise RuntimeError("Set up Heroku Data For Redis first, \
    make sure its config var is named 'REDIS_URL'.")

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
```

Then, add the command to your `Procfile`:

```plaintext
worker: python -u run-worker.py
```

Now, all you have to do is spin up a worker:

```console
$ heroku scale worker=1
```

If the from_url function fails to parse your credentials, you might need to do so manually:

```console
conn = redis.Redis(
    host=host,
    password=password,
    port=port,
    ssl=True,
    ssl_cert_reqs=None,
    ssl_ca_data=ssl_cert_str
)
```

The details are from the ‘settings’ page of your Redis add-on on the Heroku dashboard.

and for using the cli:

```console
rq info --config rq_conf
```

Where the rq_conf.py file looks like:

```console
REDIS_HOST = "host"
REDIS_PORT = port
REDIS_PASSWORD = "password"
REDIS_SSL = True
REDIS_SSL_CA_CERTS = None
REDIS_DB = 0
REDIS_SSL_CERT_REQS = None
REDIS_SSL_CA_DATA = "-----BEGIN CERTIFICATE-----\n****"
```

## Putting RQ under foreman

Foreman is probably the process manager you use when you host your app on Heroku, or just because it’s a pretty friendly tool to use in development.

When using RQ under `foreman`, you may experience that the workers are a bit quiet sometimes. This is because of Python buffering the output, so `foreman` cannot (yet) echo it. Here’s a related Wiki page.

Just change the way you run your worker process, by adding the `-u` option (to force stdin, stdout and stderr to be totally unbuffered):

```plaintext
worker: python -u run-worker.py
```
