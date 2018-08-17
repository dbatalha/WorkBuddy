from PyQt4 import QtCore, QtGui
from ModelTasks import ModelTasks
from Buddy import ProjectsFlow
from Buddy import TasksFlow
from Warning import Warning
from CreatePoject import CreateProject
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
        self.tasks_view.setColumnCount(6)
        self.tasks_view.verticalHeader().setVisible(False)
        self.tasks_view.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Name"))
        self.tasks_view.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("StartDate"))
        self.tasks_view.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("EndDate"))
        self.tasks_view.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Status"))
        self.tasks_view.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Assignee"))
        self.tasks_view.setHorizontalHeaderItem(5, QtGui.QTableWidgetItem("Project"))

        self.write_tasks_table()

        self.retranslateUi(self)

    def _get_all_tasks(self):
        return self.tasks_flow.get_all_data()

    def _get_all_projects(self):
        return self.projects_flow.get_all_data()

    def contextMenuEvent(self, event):
        self.context_menu = QtGui.QMenu(self)
        create_project = QtGui.QAction('New', self)
        activate_deactivate = QtGui.QAction('Activate/Deactivate', self)
        team = QtGui.QAction('Assign to team...', self)
        delete = QtGui.QAction('Delete Project', self)
        activate_deactivate.triggered.connect(self.activate_deactivate_project)
        delete.triggered.connect(self.delete_project)
        create_project.triggered.connect(self.create_new)
        self.context_menu.addAction(create_project)
        self.context_menu.addAction(activate_deactivate)
        self.context_menu.addAction(team)
        self.context_menu.addAction(delete)
        self.context_menu.popup(QtGui.QCursor.pos())

    def create_new(self):
        """
        Create new project
        :return:
        """
        new = CreateProject()
        new.exec_()
        self.write_tasks_table()

    def delete_project(self):
        """
        Delete selected project.
        To delete the project it must be disabled first
        :return:
        """
        projects = self._get_all_projects()

        project_id = projects[self.projects_view.currentRow()].Id
        project_status = projects[self.projects_view.currentRow()].Status

        if project_status is 0:
            warning = Warning(
                "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">"
                "Unable delete project. "
                "Make sure the project is disabled"
                "</span></p></body></html>"
            )
            warning.exec_()
        else:
            self.tasks_flow.delete_project(project_id)
            self.write_tasks_table()

    def activate_deactivate_project(self):
        projects = self._get_all_projects()

        project = projects[self.projects_view.currentRow()].Project
        status = projects[self.projects_view.currentRow()].Status

        if status is 0:
            # Currently deactivated, activate
            self.tasks_flow.tasks_status(project, 1)

        else:
            # Currently enable, deactivate
            self.tasks_flow.tasks_status(project, 0)

        self.write_tasks_table()

    def get_project(self, project_id):
        """
        Defining the project assigned
        :return:
        """
        projects = self._get_all_projects()

        for project in projects:
            if project.Id is project_id:
                return project.Project


    def write_tasks_table(self):
        tasks = self._get_all_tasks()

        self.tasks_view.setRowCount(len(tasks))

        row_counter = 0
        for task in tasks:
            # Project name header
            self.tasks_view.setItem(row_counter, 0, QtGui.QTableWidgetItem(str(task.Name)))
            self.tasks_view.setItem(row_counter, 5, QtGui.QTableWidgetItem(str(self.get_project(task.Project))))

            # Status header
            if task.Status is 1:
                display_status = "Active"

            else:
                display_status = "Disabled"

            self.tasks_view.setItem(row_counter, 2, QtGui.QTableWidgetItem(str(display_status)))

            row_counter += 1

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tasks", None))
        ModelTasks.retranslateUi(self, Dialog)
