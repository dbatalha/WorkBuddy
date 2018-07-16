from Database import Database
from Database import TasksTable
from Database import ProjectsTable


class TasksFlow(object):
    def __init__(self):
        self.database = Database()

    def add_task(self, task_name, task_status):
        """
        Create new task
        :param task_name:
        :param task_status:
        :return:
        """
        tasks_table = TasksTable(task_name, task_status)

        self.database.create(tasks_table)
        self.database.commit()

    def tasks_status(self, tasks, status):
        """
        Status is INT 0 represent disable 1 represent enable

        :param tasks:
        :param status:
        :return:
        """
        self.database.session.query(TasksTable).filter_by(Project=tasks).update({"Status": status})
        self.database.commit()

    def get_projects(self):
        projects = self.database.session.query(ProjectsTable).all()
        self.database.commit()

        return projects

    def get_all_data(self):
        data = self.database.session.query(TasksTable).all()
        self.database.commit()

        return data
