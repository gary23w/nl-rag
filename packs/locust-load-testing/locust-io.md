---
title: "Locust"
source: https://locust.io/
domain: locust-load-testing
license: CC-BY-SA-4.0
tags: locust python, load testing, performance testing, distributed load
fetched: 2026-07-02
---

# Locust

- Define user behaviour in code No need for clunky UIs or bloated XML. Just plain code.
- Distributed & Scalable Locust supports running load tests distributed over multiple machines, and can therefore be used to simulate millions of simultaneous users
- Proven & Battle-tested Locust has been used to simulate millions of simultaneous users. Battlelog, the web app for the Battlefield games, is load tested using Locust, so one can really say Locust is Battle tested ;).
- Need Dedicated Support? Locust.cloud provides dedicated commercial support for Locust.

> I'm impressed not more people talk about locust (http://locust.io/). The thing is awesome :) Shoutout too the guys from ESN :)
> 
> Armin Ronacher
> 
> @mitsuhiko
> 
> Author of Flask, Jinja2 & more

> it’s become a mandatory part of the development of any large scale HTTP service built at DICE at this point.
> 
> Joakim Bodin
> 
> @jbripley
> 
> Lead Software Engineer at EA/DICE

> locust.io is pretty fantastic, wish it had a bit more in the way of docs for non-HTTP stuff though
> 
> Alex Gaynor
> 
> @alex_gaynor
> 
> Django & PyPy core developer

locustfile.py

```
from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/static/assets.js")
        
    @task
    def about(self):
        self.client.get("/about/")
```

```
import random
from locust import HttpUser, between, task
from pyquery import PyQuery

class AwesomeUser(HttpUser):
    host = "https://docs.locust.io/en/latest/"
    
    
    
    
    
    wait_time = between(10, 600)
    
    def on_start(self):
        
        
        self.wait()
        
        self.index_page()
        self.urls_on_current_page = self.toc_urls
    
    @task(10)
    def index_page(self):
        r = self.client.get("")
        pq = PyQuery(r.content)
        link_elements = pq(".toctree-wrapper a.internal")
        self.toc_urls = [
            l.attrib["href"] for l in link_elements
        ]
    
    @task(50)
    def load_page(self):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a.internal")
        self.urls_on_current_page = [
            l.attrib["href"] for l in link_elements
        ]
    
    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)
```

```
from locust import HttpUser, TaskSet, task, between

class ForumThread(TaskSet):
    pass

class ForumPage(TaskSet):
    
    wait_time = between(10, 300)
    
    
    tasks = {
        ForumThread:3
    }
    
    @task(3)
    def forum_index(self):
        pass
    
    @task(1)
    def stop(self):
        self.interrupt()

class AboutPage(TaskSet):
    pass

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    
    tasks = {
        ForumPage: 20,
        AboutPage: 10,
    }
    
    
    
    @task(10)
    def index(self):
        pass
```

$

locust -f locustfile.py

## Example code

A fundamental feature of Locust is that you describe all your test in Python code. No need for clunky UIs or bloated XML, just plain code.

### Select example

### Used by

## Installation

The easiest way to install Locust is from PyPI, using pip:

>

pip install locust

Read more detailed installations instructions in the documentation.

Get the source code at Github.

## Cloud Hosted Locust

We are working on a hosted cloud version of Locust. It's the simplest way to set up large-scale load tests with detailed reporting.

Check it out at locust.cloud

## Maintainers & Contributors

1. Jonatan Heyman @jonatanheyman
2. Corey Goldberg @cgoldberg
3. Peter Darrow @pmdarrow
4. Justin Iso @JustinIso
5. Alden Peterson
6. Mark Beacom @mbeacom
7. Lars Holmberg @cyberw
8. Andrew Baldwin

1. mboutet
2. tdadela
3. DennisKrone
4. mquinnfd
5. HeyHugo
6. Trouv
7. max-rocket-internet
8. cgbystrom
9. ajt89
10. Jahaja
11. FooQoo
12. mgor
13. delulu
14. aek
15. samuelspagl

And more than

200

additional awesome

contributors

!

## Original Authors

1. Jonatan Heyman @jonatanheyman Follow @jonatanheyman
2. Carl Byström @cgbystrom Follow @cgbystrom
3. Joakim Hamrén @jahaaja Follow @jahaaja
4. Hugo Heyman @hugoheyman Follow @hugoheyman
