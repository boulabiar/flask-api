# Basic flask connexion example

This code is a test on creating a CRUD api (without the U) using flask and connexion.
It uses requests to connect to twitch API for very basic stuff and populate a sqlite database.
I haven't got enough time to make code better, but it was a good exercice for using connexion.

Secrets are stored in a mysecrets.py, but would be better in ENV vars fetched and constructed in a deployement process.


# Install

After creating a venv, please install the packages from requirements.py
First you need to build the database using build_db.py
Start the server.py (dev on port 8000)


# Use

the api point is at
{server}/api/v1/
{server}/api/v1/ui/  for swagger ui


/api/v1/streamers 		GET (list of streamers)
/api/v1/{platform}:{username}	GET (specific streamer)
/api/v1/{platform}:{username}	DELETE (a streamer)

/api/v1/streamers 		POST (add a streamer by platform and username on twitch)


Prod server uses nginx and uwsgi, deployed directly on a real physical server at home always connected to the internet.
Haven't got the time neither for docker nor for tests, really sorry.
