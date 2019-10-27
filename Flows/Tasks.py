from PyQt4 import QtCore, QtGui

from Core.Timer import Time
from GUI.ModelTasks import ModelTasks
from Core import ProjectsFlow
from Core import TasksFlow
from Flows.Warning import Warning
from CreateTask import CreateTask
from Core.ViewTask import ViewTask
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

__author__ = 'Daniel Batalha'


class Tasks(QtGui.QDialog, ModelTasks):
    def __init__(self, parent=None):
        super(Tasks, self).__init__(parent)
        ModelTasks.__init__(self)

        self.tasks_flow = TasksFlow()
        self.projects_flow = ProjectsFlow()

        self.tasks_view.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tasks_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tasks_view.setColumnCount(8)
        self.tasks_view.verticalHeader().setVisible(False)
        self.tasks_view.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Name"))
        self.tasks_view.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("StartDate"))
        self.tasks_view.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("EndDate"))
        self.tasks_view.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Status"))
        self.tasks_view.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Assignee"))
        self.tasks_view.setHorizontalHeaderItem(5, QtGui.QTableWidgetItem("Project"))
        self.tasks_view.setHorizontalHeaderItem(6, QtGui.QTableWidgetItem("Description"))
        self.tasks_view.setHorizontalHeaderItem(7, QtGui.QTableWidgetItem("Id"))

        self.tasks_view.setColumnHidden(7, True)

        self.write_tasks_table()

        self.retranslateUi(self)

    def _get_all_tasks(self):
        return self.tasks_flow.get_all_data()

    def _get_all_projects(self):
        return self.projects_flow.get_all_data()

    def contextMenuEvent(self, event):
        self.context_menu = QtGui.QMenu(self)
        create_task = QtGui.QAction('New', self)
        view_task = QtGui.QAction('View/Update', self)
        set_task_done = QtGui.QAction('Set to Done', self)
        set_task_in_progress = QtGui.QAction('Set to In Progress', self)
        delete = QtGui.QAction('Delete', self)
        set_task_done.triggered.connect(self.set_task_done)
        view_task.triggered.connect(self.view_task)
        set_task_in_progress.triggered.connect(self.set_task_in_progress)
        delete.triggered.connect(self.delete_project)
        create_task.triggered.connect(self.create_new)
        self.context_menu.addAction(create_task)
        self.context_menu.addAction(view_task)
        self.context_menu.addAction(set_task_done)
        self.context_menu.addAction(set_task_in_progress)
        self.context_menu.addAction(delete)
        self.context_menu.popup(QtGui.QCursor.pos())

    def create_new(self):
        """
        Create new task
        :return:
        """
        new = CreateTask()
        new.exec_()
        self.write_tasks_table()

    def view_task(self):
        """
        Create new task
        :return:
        """
        task_id = self.tasks_view.item(self.tasks_view.currentRow(), 7)
        task_name = self.tasks_view.item(self.tasks_view.currentRow(), 0)
        task_description = self.tasks_view.item(self.tasks_view.currentRow(), 6)
        task_project = self.tasks_view.item(self.tasks_view.currentRow(), 5)

        tasks = dict()
        tasks.update({"Name": task_name.text(), "Description": task_description.text(),
                      "Id": task_id.text(), "Project": task_project})

        new = ViewTask(tasks)
        new.exec_()
        self.write_tasks_table()

    def delete_project(self):
        """
        Delete selected task.
        To delete the project it must be disabled first
        :return:
        """
        tasks = self._get_all_tasks()

        task_id = tasks[self.tasks_view.currentRow()].Id
        task_status = tasks[self.tasks_view.currentRow()].Status

        if task_status is 0:
            warning = Warning(
                "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">"
                "Unable delete Task. "
                "Make sure the Task is Done"
                "</span></p></body></html>"
            )
            warning.exec_()
        else:
            self.tasks_flow.delete_task(task_id)
            self.write_tasks_table()

    def set_task_done(self):
        """
        Set selected task as Done
        :return:
        """

        tasks = self._get_all_tasks()

        task_id = tasks[self.tasks_view.currentRow()].Id

        self.tasks_flow.set_status(task_id, 0)

        # Refresh the table
        self.write_tasks_table()

    def set_task_in_progress(self):
        """
        Set selected task as in progress
        :return:
        """

        tasks = self._get_all_tasks()

        task_id = tasks[self.tasks_view.currentRow()].Id

        self.tasks_flow.set_status(task_id, 1)

        # Refresh the table
        self.write_tasks_table()

    def get_project(self, project_id):
        """
        Get the project name by project ID
        :return: Return the project name if match the input project ID
        """
        projects = self._get_all_projects()

        for project in projects:
            if project.Id is project_id:
                return project.Project

    def write_tasks_table(self):
        """
        Draw the main table
        :return:
        """
        tasks = self._get_all_tasks()

        self.tasks_view.setRowCount(len(tasks))

        row_counter = 0
        for task in tasks:

            end_time = None
            start_time = None

            # Convert to display data
            if task.StartDate is not None:
                start_time = Time.date_time_format(int(task.StartDate))

            if task.EndDate is not None:
                end_time = Time.date_time_format(int(task.EndDate))

            # Project name header
            self.tasks_view.setItem(row_counter, 0, QtGui.QTableWidgetItem(str(task.Name)))
            self.tasks_view.setItem(row_counter, 1, QtGui.QTableWidgetItem(str(start_time)))
            self.tasks_view.setItem(row_counter, 2, QtGui.QTableWidgetItem(str(end_time)))
            self.tasks_view.setItem(row_counter, 4, QtGui.QTableWidgetItem(str(task.Assignee)))
            self.tasks_view.setItem(row_counter, 5, QtGui.QTableWidgetItem(str(self.get_project(task.Project))))
            self.tasks_view.setItem(row_counter, 6, QtGui.QTableWidgetItem(str(task.Description)))
            self.tasks_view.setItem(row_counter, 7, QtGui.QTableWidgetItem(str(task.Id)))

            # Status header
            if task.Status is None:
                task.Status = int(0)

            if int(task.Status) is 1:
                # TODO need translation
                display_status = "In Progress"

            else:
                # TODO need translation
                display_status = "Done"

            self.tasks_view.setItem(row_counter, 3, QtGui.QTableWidgetItem(str(display_status)))

            if task.Description is not None:
                self.tasks_view.setItem(row_counter, 6, QtGui.QTableWidgetItem(task.Description))

            row_counter += 1

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tasks", None))
        ModelTasks.retranslateUi(self, Dialog)
