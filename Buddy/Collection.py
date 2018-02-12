from Database import Database
from Database import BuddyTable

__author__ = 'Daniel Batalha'


class Collection(object):
    def __init__(self):
        self.database = Database()

    def get_all_data(self):
        data = self.database.session.query(BuddyTable).all()

        self.database.commit()
        return data
