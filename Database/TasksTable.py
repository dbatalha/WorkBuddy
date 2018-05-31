from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TasksTable(Base):
    __tablename__ = "tasks"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    Task = Column(String())

    Project = Column(Integer())

    def __init__(self, task, project):
        self.Task = task
        self.Project = project