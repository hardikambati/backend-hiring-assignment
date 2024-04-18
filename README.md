# Project & Task Management API's | Pixeldust
`v1.0.0`

## Project Description

This backend service exposes API's which can :
- perform CRUD operation on tasks
- perform CRUD operation on projects

<br>

## Docker Container Description

This system consists of one service :

- wsgi : The main wsgi container running on port `8000`

<br>

## System Prerequisites

1. Make sure you have docker and docker-compose installed on your local system.
2. Creating a `.env` environment file
    ```
    SECRET_KEY='<SECRET_KEY>'
    ```

<br>

## Spinning up the server using Docker

1. Create migration files locally
    ```
    docker-compose run wsgi python3 manage.py makemigrations
    ```
2. The following command will spin up all the docker container services
    ```
    docker-compose up --build
    ```
3. On startup, the setup file will automatically do the following tasks (defined in `setup.py` file)
    - migrate the changes
    - create superuser
    - create base user
    - collect all static files in /static/ folder
4. The API's can be accessed on the swagger panel [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

<br>

## Directory Structure

```
root
|
|----- core
|       |----- urls.py
|       |----- settings.py
|       |----- others...
|
|----- main
|        |----- urls.py
|        |----- views.py
|        |----- models.py
|        |----- decorators.py
|        |----- serializers.py
|        |----- others...
|
|----- scripts
|        |----- setup.py
|
|----- utils
|        |----- config.py
|        |----- helpers.py
|        |----- pagination.py
|        |----- docs
|                  |----- task.py
|                  |----- project.py
|                  |----- generic.py
|
|
|----- DockerFile
|----- docker-compose.yaml
|
|----- requirements.txt
|
|----- .env
|----- .gitignore
|
|----- README.md
```


<br>

## Important URL's

Swagger Panel : [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

Developed by : Hardik Ambati [LinkedIn](https://www.linkedin.com/in/hardik-ambati)