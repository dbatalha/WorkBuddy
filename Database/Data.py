from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database(object):
    def __init__(self):
        super(Database, self).__init__()

        engine = create_engine('sqlite:///data.db')

        if not engine.dialect.has_table(engine, "projects"):
            print True

        else:
            print False

        session_maker = sessionmaker(bind=engine)
        self.session = session_maker()

    def create(self, table):
        self.session.add(table)

    def commit(self):
        self.session.commit()
