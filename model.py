from mitama.db import BaseDatabase
from mitama.db.types import *


class Database(BaseDatabase):
    pass


db = Database()

class Profile(db.Model):
    name = Column(String(255))
    epoch = Column(Integer)
    image = Column(LargeBytes)
    description = Column(String)
    tags = Column(String(255))

class Invite(db.Model):
    token = Column(String(255))

db.create_all()
