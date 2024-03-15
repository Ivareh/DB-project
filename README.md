# db_project_2024
TDT4145 Database project 2024


Written with Python and SQLite3


## How to run

### Python environment

Activate a python environment:

1. `python -m venv venv`
2. `source activate`
3. `pip install -r requirements.txt`


### Activating the database

1. `sqlite3 theater.db`
2. `.read Theater_DB.sql`
3. `CTRL + C` - Exit sqlite3


### Add database data

Useful commands:

- In the case of non-unique errors, run the command to delete all data from the database:
`python clear_db_data.py`

To add all the data to database:

1. [Activate the python environment](#python-environment)
2. [Activate the database](#activating-the-database)
3. `python add_db_data.py`
4. `python scan-seats-gamle-scene.py`
5. `python scan-seats-hovedscenen.py`
