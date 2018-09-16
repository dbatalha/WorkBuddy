from Database import Database
from Database import TasksTable
from Database import ProjectsTable


class TasksFlow(object):
    def __init__(self):
        self.database = Database()

    def add_task(self, task_name, task_status, task_project):
        """
        Create new task
        :param task_name:
        :param task_status:
        :param task_project:
        :return:
        """
        tasks_table = TasksTable(task_name, task_project)

        self.database.create(tasks_table)
        self.database.commit()

    def set_status(self, task, status):
        """
        Set the task status Done or In Progress
        :param task: the Id of the task
        :param status: Status of the task
        :return:
        """
        self.database.session.query(TasksTable).filter_by(Id=task).update({"Status": status})
        self.database.commit()

    def get_projects(self):
        projects = self.database.session.query(ProjectsTable).all()
        self.database.commit()

        return projects

    def delete_task(self, task_id):
        """
        Delete task
        :param task_id:
        :return:
        """
        self.database.session.query(TasksTable).filter_by(Id=task_id).delete()
        self.database.commit()

    def get_tasks(self):
        tasks = self.database.session.query(TasksTable).all()
        self.database.commit()

        return tasks

    def get_all_data(self):
        data = self.database.session.query(TasksTable).all()
        self.database.commit()

        return data
