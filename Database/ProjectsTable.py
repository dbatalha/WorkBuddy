from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProjectsTable(Base):
    __tablename__ = "projects"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    Project = Column(String())

    Client = Column(String())

    Status = Column(String())

    Team = Column(String())

    def __init__(self, project_name):
        self.Project = project_name
