from Work import WorkSystem
from Work import Time
from Database import Database
from Database import TasksTable
from Database import ProjectsTable

IN_PROGRESS = 1
DONE = 0


class TasksFlow(object):
    def __init__(self):
        self.database = Database()

    def add_task(self, task_name, task_status, task_project, task_description):
        """
        Create new task
        :param task_name:
        :param task_status:
        :param task_project:
        :param task_description:
        :return:
        """
        tasks_table = TasksTable(task_name, task_project)

        self.database.create(tasks_table)
        self.database.commit()

        task_id = self.get_task_id_by_name(task_name)
        self.set_start_date(task_id)

        self.set_status(task_id, IN_PROGRESS)
        self.set_task_assignee(task_id)
        self.set_task_description(task_id, task_description)

    def set_status(self, task, status):
        """
        Set the task status Done or In Progress
        :param task: the Id of the task
        :param status: Status of the task
        :return:
        """
        if status is DONE:
            self.set_end_date(task)

        self.database.session.query(TasksTable).filter_by(Id=task).update({"Status": status})
        self.database.commit()

    def set_task_assignee(self, task):
        self.database.session.query(TasksTable).filter_by(Id=task).update(
            {"Assignee": WorkSystem.WorkSystem.get_system_username()})
        self.database.commit()

    def set_start_date(self, task):
        self.database.session.query(TasksTable).filter_by(Id=task).update({"StartDate": Time.actual()})
        self.database.commit()

    def set_end_date(self, task):
        self.database.session.query(TasksTable).filter_by(Id=task).update({"EndDate": Time.actual()})
        self.database.commit()

    def set_task_description(self, task, description):
        self.database.session.query(TasksTable).filter_by(Id=task).update({"Description": str(description)})
        self.database.commit()

    def set_task_name(self, task, name):
        self.database.session.query(TasksTable).filter_by(Id=task).update({"Name": str(name)})
        self.database.commit()

    def set_task_project(self, task, project):
        self.database.session.query(TasksTable).filter_by(Id=task).update({"Project": int(project)})
        self.database.commit()

    def get_projects(self):
        tasks = self.database.session.query(ProjectsTable).all()
        self.database.commit()

        return tasks

    def delete_task(self, task_id):
        """
        Delete task
        :param task_id:
        :return:
        """
        self.database.session.query(TasksTable).filter_by(Id=task_id).delete()
        self.database.commit()

    def update_task(self, task, name, description, project):
        """
        Set project name description and project.
        :param task:
        :param name:
        :param description:
        :param project:
        :return:
        """
        self.set_task_name(task, name)
        self.set_task_description(task, description)
        self.set_task_project(task, project)

    def get_tasks(self):
        tasks = self.database.session.query(TasksTable).all()
        self.database.commit()

        return tasks

    def get_task_id_by_name(self, name):
        tasks = self.get_tasks()

        for task in tasks:
            if task.Name == name:
                return task.Id

    def get_all_data(self):
        data = self.database.session.query(TasksTable).all()
        self.database.commit()

        return data
