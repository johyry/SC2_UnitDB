from application import db
from application.models import Base
from sqlalchemy.sql import text


class Unit(Base):
    
    name = db.Column(db.String(144), nullable=False)
    supply = db.Column(db.Integer)
    minerals = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    buildtime = db.Column(db.Integer)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name


    # query to get creator username, query result account.username

    @staticmethod
    def find_creatorUserName(account_id):

        stmt = text("SELECT Account.username FROM Account, Unit"
                     " WHERE Unit.account_id = Account.id"
                     " AND Account.id = :account_id"
                     ).params(account_id=account_id)
                     
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])
        

        return response[0]