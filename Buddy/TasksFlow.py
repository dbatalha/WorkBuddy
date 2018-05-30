from Database import Database
from Database import TasksTable


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
        project_table = TasksTable(task_name, task_status)

        self.database.create(project_table)
        self.database.commit()

    def project_status(self, tasks, status):
        """
        Status is INT 0 represent disable 1 represent enable

        :param tasks:
        :param status:
        :return:
        """
        self.database.session.query(TasksTable).filter_by(Project=tasks).update({"Status": status})
        self.database.commit()

    def get_all_data(self):
        data = self.database.session.query(TasksTable).all()
        self.database.commit()

        return data
