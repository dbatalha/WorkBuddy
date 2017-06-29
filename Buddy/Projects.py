from Database import Database


class Projects(object):
    def __init__(self):
        self.database = Database()

    def create_data_project(self):
        self.database.create("CREATE TABLE IF NOT EXISTS projects (Id INTEGER PRIMARY KEY AUTOINCREMENT, Project,"
                             " Client, Status)")

    def add_project(self, project_name):
        self.database.insert("INSERT INTO projects (Project) VALUES ('%s')" % project_name)

        self.database.save()
