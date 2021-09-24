# Vendomatic

This project has two folders, one for the backend (Django) and another one for the frontend (React).

First, follow the backend section, and then the frontend one.
## Backend

- In one terminal, located in the `back` folder, execute the following:

- Install poetry with
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
(or follow the instructions from this page: https://python-poetry.org/docs/)

and then

```
poetry install
```

- To activate the poetry environment run: 
```
poetry shell
```

- Run the migrations: 
```
./manage.py migrate
```

- Load the inital data (beverages and coins): 
```
./manage.py loaddata fixtures/*.json
```

- Run the server:
```
./manage.py runserver
```

- Optionally, if you want to run the tests:
```
./manage.py test
```

- If you run out of beverages, you can run the following command:
```
./manage.py loaddata fixtures/beverages.json
```
## Frontend

Make sure you have node >= 14.0.0. and npm >= 5.6 in order to have all running flawlessly.

Open a new terminal in the `front` folder, and then execute `npm install` to install dependencies.

To run the project locally, execute: `npm start`
