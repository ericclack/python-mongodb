# Python code to import MongoDB Export back in again

Because my build of MongoDB doesn't have mongoimport

# Docs

https://pymongo.readthedocs.io/en/stable/tutorial.html

## Bugs

Dates in the past are 1 hour out, so:
  1 Sept 1975, 13:00:34
instead of the correct:
  1 Sept 1975, 12:00:34

However, dates in the future are fine.
  