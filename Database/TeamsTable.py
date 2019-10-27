from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TeamsTable(Base):
    __tablename__ = "teams"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    Name = Column(String())

    Elements = Column(Integer())

    def __init__(self, team_name, team_elements):
        self.Name = team_name
        self.Elements = team_elements
