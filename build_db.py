import os
from config import db
from models import Streamer

# Database init data
Streamers_ = [
    {   "platform": "Twitch",
        "username": "franc",
        "streamUrl": "http://",
        "profilePictureUrl":"https://"},

    {   "platform": "Twitch",
        "username": "marc",
        "streamUrl": "http://",
        "profilePictureUrl":"https://"},

    {   "platform": "Twitch",
        "username": "john",
        "streamUrl": "http://",
        "profilePictureUrl":"https://"},
]

# Delete database file if it exists
if os.path.exists("streamers.db"):
    os.remove("streamers.db")

# Create the database
db.create_all()

# Populate the database
for streamer in Streamers_:
    p = Streamer(   platform=streamer.get("platform"),
                    username=streamer.get("username"),
                    streamUrl=streamer.get("streamUrl"),
                    profilePictureUrl=streamer.get("profilePictureUrl"),
        )
    db.session.add(p)

db.session.commit()
