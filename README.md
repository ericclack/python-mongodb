# Python code to import MongoDB Export back in again

Because my build of MongoDB doesn't have mongoimport

## Set up venv and add libraries

```
python3 -m venv env-python-mongodb
source env-python-mongodb/bin/activate
python -m pip install pymongo
python -m pip install python-dateutil
```

## Create a date-lookup file

```
data/date-lookup.json:

[
    {
	"_id": "media/2017/4/18/id-of-photo1.jpg",
	"datetime": "2010-12-18T10:14:00.0Z" },
    {
	"_id": "media/2017/7/14/id-of-photo2.jpg",
	"datetime": "2017-07-14T21:30:00.0Z"}
]
```

## Symlink up your backup file

```
cd path/to/python-mongodb
cd data
ln -s path/to/backup.json backup.json
```

## Run it

```
source env-python-mongodb/bin/activate
python test_import.py
```

## Docs

https://pymongo.readthedocs.io/en/stable/tutorial.html

## Bugs

Dates in the past are 1 hour out, so:
  1 Sept 1975, 13:00:34
instead of the correct:
  1 Sept 1975, 12:00:34

However, dates in the future are fine.
  