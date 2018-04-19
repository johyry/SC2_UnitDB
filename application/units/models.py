from application import db
from application.models import Base


class Unit(Base):
    
    name = db.Column(db.String(144), nullable=False)
    supply = db.Column(db.Integer)
    minerals = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    buildtime = db.Column(db.Integer)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
