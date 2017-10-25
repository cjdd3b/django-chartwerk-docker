Chartwerk on Docker
===================

This project deploys the excellent django-chartwerk application using Docker and docker-compose. It uses a bare-bones configuration and is intended as a proof of concept, as well as an excuse for some self-study into the ways of Docker. Feedback is welcome!

Structure
---------

The application is deployed as a series of services, which should run seamlessly on a local machine (in my case a Mac using OSX) and can be deployed to Amazon ECS with some additional configuration.

  - Nginx
  - PostgreSQL
  - Redis (for the Celery queue)
  - A Django-ready web application server

The local configuration will spin up a Postgres container, but in production you may want to use a persistent database like an RDS instance. You should add your database settings as environment variables, which by default live in `config/env`. Just be careful not to check those into Github.

Dependencies
------------

The nice thing about deploying this app via Docker is that the only dependency should be Docker itself. You'll also want an AWS account and a couple utilities if you want to deploy this to the Internet.

Installation instructions for Docker and its associated utilities can be found [here](https://docs.docker.com/docker-for-mac/).

Quickstart
----------

Once you have installed Docker and docker-compose, running the app locally is easy:

```
git clone https://github.com/cjdd3b/django-chartwerk-docker.git
cd django-chartwerk-docker
docker-compose build
docker-compose up
```

Then just visit `127.0.0.1:8000/chartwerk` and it should be running. If debug mode is off, the app will prompt you for a password. The default username and password are both **admin**.

Issues and next steps
---------------------

  - Deploying to ECS requires writing a v2 docker-compose file, plus additional configuration. Would be good to demo that.
  - There seems to be an issue with the screenshotting functionality (ticket here)

Questions?
----------

I'm at chase.davis@gmail.com
