import sqlite3


class Connection(object):
    def __init__(self):
        self.db_file = "data.db"
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = None

        self._define_cursor()

    def _define_cursor(self):
        self.cursor = self.connection.cursor()

    def create(self, statement):
        """
        The method create new table on sqlite database
        :param statement:
        :return:
        """
        self.cursor.execute(statement)

    def insert(self, statement):
        """
        This method insert data into sqlite table
        :param statement:
        :return:
        """
        self.cursor.execute(statement)

    def update(self, statement):
        """
        This method update data.
        :param statement:
        :return:
        """
        self.cursor.execute(statement)

    def select(self, statement):
        """
        This method select table from sqlite database
        :param statement:
        :return:
        """
        self.cursor.execute(statement)
        data = self.cursor.fetchone()

        return data

    def save(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
