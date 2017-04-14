from Database import Database


class Collection(object):
    def __init__(self):
        self.database = Database()

    def get_all_data(self):
        data = self.database.select("select * from buddy")

        # Close database.
        self.database.save()
        self.database.close()
        return data
