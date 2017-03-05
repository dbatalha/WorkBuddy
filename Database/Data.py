from Connection import Connection


class Database(Connection):
    def __init__(self):
        super(Database, self).__init__()

    def create(self, statement):
        Connection.create(self, statement)

    def insert(self, statement):
        Connection.insert(self, statement)

    def update(self, statement):
        Connection.update(self, statement)

    def select(self, statement):
        data = Connection.select(self, statement)

        return data

    def save(self):
        Connection.save(self)

    def close(self):
        Connection.close(self)
