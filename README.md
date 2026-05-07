# Coodesh challenge

This is a challenge by [Coodesh](https://coodesh.com/)

## requirements

- prefer use a virtual environment (venv, conda, etc)
- python 3.14
- requirements.txt must be installed `pip install -r requirements.txt`

## setup

once satisfied all requirements you must run:

```sh
python manage.py migrate
```

to apply all changes to database

## run backend

once requirements applied and setup done only run 

```sh
python manage.py runserver
```

and the urls bellow will be available on localhost:8000


## urls
- /openapi/schema/swagger-ui/
- /openapi/schema/redoc/
- /api/polls/
- /api/polls/<int:id>/results/
- /api/vote/