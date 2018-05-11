from application import db
from application.models import Base
from sqlalchemy.sql import text



class Buildorder(Base):

    name = db.Column(db.String(144), nullable=False)


    buildtype = db.Column(db.String(30))
    race = db.Column(db.String(10))

    description = db.Column(db.String(10000))
    intro = db.Column(db.String(10000))
    vod = db.Column(db.String(144))
    details = db.Column(db.String(10000))
    analysis = db.Column(db.String(20000))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name


    # query for creator username (query result: account.username)

    @staticmethod
    def find_creatorUserName(account_id):

        stmt = text("SELECT Account.username FROM Account, Buildorder"
                     " WHERE Buildorder.account_id = Account.id"
                     " AND Account.id = :account_id"
                     ).params(account_id=account_id)
                     
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])
        

        return response[0]