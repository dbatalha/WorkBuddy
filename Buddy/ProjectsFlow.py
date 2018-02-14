from Database import Database
from Database import ProjectsTable


class ProjectsFlow(object):
    def __init__(self):
        print "Projects"
        self.database = Database()

    def add_project(self, project_name):
        #self.database.insert("INSERT INTO projects (Project) VALUES ('%s')" % project_name)

        project_table = ProjectsTable(project_name)

        self.database.create(project_table)
        self.database.commit()

    def get_all_data(self):
        #data = self.database.select("SELECT * FROM projects")

        data = self.database.session.query(ProjectsTable).all()
        self.database.commit()

        return data
