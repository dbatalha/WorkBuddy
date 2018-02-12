from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BuddyTable(Base):
    __tablename__ = "buddy"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    StartWorkTime = Column(String())
    StartWorkEpoch = Column(Integer())

    LunchTime = Column(String())
    LunchTimeEpoch = Column(Integer())

    StartAfterLunch = Column(String())
    StartAfterLunchEpoch = Column(Integer())

    EndWorkTime = Column(String())
    EndWorkEpoch = Column(Integer())

    Total = Column(Integer())
    Username = Column(String())
    Tasks = Column(Integer())

    def __init__(self, start, start_epoch, username):
        self.StartWorkTime = start
        self.StartWorkEpoch = start_epoch

        self.Username = username
