from datetime import datetime
from config import db, ma


class Streamer(db.Model):
    __tablename__ = "streamers"
    userid = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(32))
    username = db.Column(db.String(32))
    streamUrl = db.Column(db.String(256))
    profilePictureUrl = db.Column(db.String(256))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class StreamerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Streamer
        load_instance=True
        sqla_session = db.session


