from Database import Database
from Database import ProjectsTable


class ProjectsFlow(object):
    def __init__(self):
        self.database = Database()

    def add_project(self, project_name, project_status):
        """
        Create new project
        :param project_name:
        :return:
        """
        project_table = ProjectsTable(project_name, project_status)

        self.database.create(project_table)
        self.database.commit()

    def get_all_data(self):
        data = self.database.session.query(ProjectsTable).all()
        self.database.commit()

        return data
