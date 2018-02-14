from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database(object):
    def __init__(self):
        super(Database, self).__init__()

        engine = create_engine('sqlite:///data.db')

        session_maker = sessionmaker(bind=engine)
        self.session = session_maker()

    def create(self, table):
        self.session.add(table)

    def commit(self):
        self.session.commit()
