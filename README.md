|             | status |
|-------------|------------|
| **master** | [![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=master)](https://travis-ci.org/afourmy/flask-gentelella) [![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=master)](https://coveralls.io/github/afourmy/flask-gentelella?branch=master)
| **develop** | [![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=develop)](https://travis-ci.org/afourmy/flask-gentelella) [![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=develop)](https://coveralls.io/github/afourmy/flask-gentelella?branch=develop)

# Flask Gentelella

[Gentelella](https://github.com/puikinsh/gentelella) is a free to use Bootstrap admin template.

![Gentelella Bootstrap Admin Template](https://cdn.colorlib.com/wp/wp-content/uploads/sites/2/gentelella-admin-template-preview.jpg "Gentelella Theme Browser Preview")

This project integrates Gentelella with Flask using: 
- [Blueprints](https://flask.palletsprojects.com/en/1.0.x/blueprints/) for scalability.
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system (passwords hashed with bcrypt).
- [flask_migrate](https://flask-migrate.readthedocs.io/en/latest/).

Flask-gentelella also comes with a robust CI/CD pipeline using:
- The [Pytest](https://docs.pytest.org/en/latest/) framework for the test suite (see the `tests` folder).
- A [PostgreSQL](https://www.postgresql.org/) database (optional; see below for installation instructions).
- [Travis CI](https://travis-ci.org/afourmy/flask-gentelella) (automated testing)
- [Coverage](https://coveralls.io/github/afourmy/flask-gentelella) to measure the code coverage of the tests.
- [Selenium](https://www.seleniumhq.org/) to test the application with headless chromium.
- A `Dockerfile` showing how to containerize the application with gunicorn, and a [Docker image](https://hub.docker.com/r/afourmy/flask-gentelella/) available on dockerhub, and integrated to the CI/CD pipeline (see instructions below).
- A `docker-compose` file to start Flask-gentelella with `nginx`, `gunicorn` and a PostgreSQL database.

Here is an example of a real project implemented using Flask-Gentelella:
- [Online demo](http://afourmy.pythonanywhere.com/)
- [Source code](https://github.com/afourmy/eNMS)

This project shows:
- how back-end and front-end can interact responsively with AJAX requests.
- how to implement a graph model with SQLAlchemy and use D3.js for [graph visualization](http://afourmy.pythonanywhere.com/views/logical_view).
- how to implement a [workflow automation](http://afourmy.pythonanywhere.com/automation/workflow_builder/) system using Vis.js.
- how to use [Leaflet.js and WebGL-Earth](http://afourmy.pythonanywhere.com/views/geographical_view) for 2D and 3D GIS programming.
- how to use [Flask APScheduler](https://github.com/viniciuschiele/flask-apscheduler) to implement crontab-like features.


## Run Flask Gentelella in a docker container
    git clone https://github.com/afourmy/flask-gentelella.git
### 1. Fetch the image on dockerhub
    docker pull docker.io/tiangolo/uwsgi-nginx-flask
    
    docker run -d \
    --name gentelella \
    -p 3388:80 \
    --restart=always \
    -v /home/flask-gentelella-master:/app \
    --privileged=true \
    -e FLASK_APP=gentelella.py \
    -e FLASK_DEBUG=1 \
    docker.io/tiangolo/uwsgi-nginx-flask \
    flask run --host=0.0.0.0 --port=80

### 2. Go to http://server_address:3388/, create an account and log in

