from Database import Database
from Database import ProjectsTable


class ProjectsFlow(object):
    def __init__(self):
        self.database = Database()

    def add_project(self, project_name, project_status):
        """
        Create new project
        :param project_name:
        :param project_status:
        :return:
        """
        project_table = ProjectsTable(project_name, project_status)

        self.database.create(project_table)
        self.database.commit()

    def project_status(self, project, status):
        """
        Status is INT 0 represent disable 1 represent enable

        :param project:
        :param status:
        :return:
        """
        self.database.session.query(ProjectsTable).filter_by(Project=project).update({"Status": status})
        self.database.commit()

    def delete_project(self, project_id):
        """
        Delete project
        :param project_id:
        :return:
        """
        self.database.session.query(ProjectsTable).filter_by(Id=project_id).delete()
        self.database.commit()

    def get_all_data(self):
        data = self.database.session.query(ProjectsTable).all()
        self.database.commit()

        return data
