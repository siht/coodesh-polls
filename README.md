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

## run tests
some tests were added, you can execute it all
```sh
python manage.py test
```

## front end

enter to polls-frontend

### dependencies

I use nvm to install the lastest version of node (v26.0.0), aftar that install node dependencies

```sh
npm install
```

### run frontend

```sh
npm run dev
```

after that you run backend and frontend you must enter to localhost:3000 and the react app will be available to use the backend API.

