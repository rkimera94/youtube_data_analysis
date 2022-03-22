from server import db
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class VideoTags(db.Model):
    __tablename__ = 'video_tags'

    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String())
    tag = db.Column(db.String())

    def __init__(self, video_id, tag):
        self.video_id = video_id
        self.tag = tag

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"video_id": self.video_id, "tag": self.tag}
