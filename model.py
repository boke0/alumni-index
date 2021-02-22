from mitama.db import BaseDatabase, relationship
from mitama.db.types import *

from mitama.models import Group


class Database(BaseDatabase):
    pass


db = Database(prefix="alumni_index")

profile_tag = Table(
    "alumni_index_tag_item",
    db.metadata,
    Column("tag_id", String(64), ForeignKey("alumni_index_tag._id")),
    Column("profile_id", String(64), ForeignKey("alumni_index_profile._id"))
)

class Profile(db.Model):
    name = Column(String(255))
    epoch = Column(Integer)
    image = Column(LargeBinary)
    description = Column(String)
    tags = relationship("Tag", secondary=profile_tag, backref="profiles")
    lcm = Column(Boolean)
    mentor = Column(Boolean)
    alumnight = Column(Boolean)

class Tag(db.Model):
    name = Column(String(255))
    def __init__(self, name):
        self.name = name

class Bd(db.Model):
    group_id = Column(String(64), ForeignKey("mitama_group._id"))
    group = relationship(Group)
    @classmethod
    def is_bd(cls, user):
        for group in user.groups:
            try:
                cls.retrieve(group = group)
                return True
            except Exception:
                continue
        return False

db.create_all()
