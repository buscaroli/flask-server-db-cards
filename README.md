# Learning Flask + SQLLite

### Notes

- After setting up the database in app.py you have to create the db from the shell (this can probably be automated if deploying with Docker):

```
python / python3
>>> from app import db
>>> db.create_all()
>>> exit()
```
