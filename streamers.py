"""
streamers module REST actions
"""
from flask import make_response, abort
from config import db
from models import Streamer, StreamerSchema
import streamFetcher as streamf

def read_all():
    """
    This function responds to a request for /api/v1/streamers
    with the complete lists of streamers

    :return:        json string of list of streamers
    """
    streamer = Streamer.query.order_by(Streamer.userid).with_entities(Streamer.platform, Streamer.username, Streamer.streamUrl, Streamer.profilePictureUrl).all()
    #streamer = Streamer.query.all()

    # Serialize the data for the response
    streamer_schema = StreamerSchema(many=True)
    data = streamer_schema.dump(streamer)
    return data
    #return {}

def read_one(platform, username):
    """
    This function responds to a request for /api/v1/streamer/{platform}:{username}
    with one matching streamer

    :param platform:  platform of streamer
    :param streamer_id:   Id of streamer to find
    :return:            streamer matching id
    """
    # Get the streamer requested
    streamer = Streamer.query.filter(Streamer.platform == platform, Streamer.username == username).one_or_none()

    if streamer is not None:
        # Serialize the data for the response
        streamer_schema = StreamerSchema()
        data = streamer_schema.dump(streamer)
        return data
    else:
        abort(
            404,
            "Streamer not found for Id: {username}".format(username=username),
        )


def create(streamer):
    """
    This function creates a new streamer
    based on the passed in streamer username and platform

    :param streamer:  streamer to create
    :return:        201 on success, 406 on streamer exists
    """
    username = streamer.get("username")
    platform = streamer.get("platform")

    existing_streamer = (
        Streamer.query.filter(Streamer.username == username)
        .filter(Streamer.platform == platform)
        .one_or_none()
    )

    if existing_streamer is None:
        streamer = streamf.streamerBuilder(username, platform)

        # Create a streamer instance using the schema and the passed in streamer
        schema = StreamerSchema()
        new_streamer = schema.load(streamer, session=db.session)

        # Add the streamer to the database
        db.session.add(new_streamer)
        db.session.commit()

        # Serialize and return the newly created streamer in the response
        data = schema.dump(new_streamer)

        return data, 201

    else:
        abort(
            409,
            "Streamer {platform} {streamer} exists already".format(
                platform=platform, username=username
            ),
        )

def createBasic(streamer):
    """
    This function creates a new streamer
    based on the passed in streamer data.
    This was used before connecting to Twitch.

    :param streamer:  streamer to create
    :return:        201 on success, 406 on streamer exists
    """
    platform = streamer.get("platform")
    username = streamer.get("username")
    streamUrl = streamer.get("streamUrl")
    profilePictureUrl = streamer.get("profilePictureUr")

    existing_streamer = (
        Streamer.query.filter(Streamer.username == username)
        .filter(Streamer.platform == platform)
        .one_or_none()
    )

    if existing_streamer is None:
        schema = StreamerSchema()
        new_streamer = schema.load(streamer, session=db.session)

        db.session.add(new_streamer)
        db.session.commit()

        # Serialize and return the newly created streamer in the response
        data = schema.dump(new_streamer)

        return data, 201

    else:
        abort(
            409,
            "Streamer {platform} {streamer} exists already".format(
                platform=platform, username=username
            ),
        )

def delete(platform, username):
    """
    This function deletes a streamer

    :param platform:   platform of the streamer to delete
    :param streamer_id:   Id of the streamer to delete
    :return:            200 on successful delete, 404 if not found
    """
    streamer = Streamer.query.filter(Streamer.platform == platform, Streamer.username == username).one_or_none()

    if streamer is not None:
        db.session.delete(streamer)
        db.session.commit()
        return make_response(
            "Streamer {platform} {username} deleted".format(platform=platform, username=username), 200
        )

    else:
        abort(
            404,
            "Streamer not found for Platform:Username: {platform}:{username}".format(platform=platform, username=username),
        )

