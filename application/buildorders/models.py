from application import db
from application.models import Base


class Buildorder(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000))
    intro = db.Column(db.String(1000))
    vod = db.Column(db.String(144))
    details = db.Column(db.String(1000))
    analysis = db.Column(db.String(5000))

    def __init__(self, name):
        self.name = name