from application import db

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    supply = db.Column(db.Integer)
    minerals = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    buildtime = db.Column(db.Integer)

   

    def __init__(self, name):
        self.name = name
