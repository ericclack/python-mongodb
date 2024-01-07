# Python code to import MongoDB Export back in again

Because my build of MongoDB doesn't have mongoimport

# Set up venv

```
python3 -m venv env-python-mongodb
source env-python-mongodb/bin/activate
python -m pip install pymongo
python -m pip install python-dateutil
```

# Docs

https://pymongo.readthedocs.io/en/stable/tutorial.html

## Bugs

Dates in the past are 1 hour out, so:
  1 Sept 1975, 13:00:34
instead of the correct:
  1 Sept 1975, 12:00:34

However, dates in the future are fine.
  