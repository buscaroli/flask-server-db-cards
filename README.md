# Learning Flask + SQLite

Implemented a flashcard-like site that allows the user to add, delete and update cards with Q&A.

## Why?

I am learning Python and Flask as part of the curriculum at futureproof.

## Where to play with it

The app is currently hosted on Heroku at [this address](https://flask-question-cards.herokuapp.com/)

## Tech

- Python 3.\*
- Flask
- SQLAlchemy

## How to run

Clone the repo, make sure python 3 is installed, then:

```
cd flask-server-db
pipenv shell
pipenv install
python
>>> from app import db
>>> db.create_all()
>>> exit()
pipenv run python app.py
```

### Notes

- After setting up the database in app.py you have to create the db from the shell (this can probably be automated if deploying with Docker):

```
python / python3
>>> from app import db
>>> db.create_all()
>>> exit()
```

## TODO

- Add auth
- Improve styling
