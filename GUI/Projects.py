from PyQt4 import QtCore, QtGui
from ModelProjects import ModelProjects
from Buddy import ProjectsFlow
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


class Projects(QtGui.QDialog, ModelProjects):
    def __init__(self, parent=None):
        super(Projects, self).__init__(parent)
        ModelProjects.__init__(self)

        self.projects_flow = ProjectsFlow()

        self.projects_view.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.projects_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.projects_view.setColumnCount(4)
        self.projects_view.verticalHeader().setVisible(False)
        self.projects_view.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Name"))
        self.projects_view.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Client"))
        self.projects_view.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Status"))
        self.projects_view.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Team"))

        self.write_projects_table()

        self.retranslateUi(self)

    def _get_all_projects(self):
        return self.projects_flow.get_all_data()

    def contextMenuEvent(self, event):
        self.context_menu = QtGui.QMenu(self)
        activate_deactivate = QtGui.QAction('Activate/Deactivate', self)
        team = QtGui.QAction('Assign to team...', self)
        activate_deactivate.triggered.connect(self.activate_deactivate_project)
        self.context_menu.addAction(activate_deactivate)
        self.context_menu.addAction(team)
        self.context_menu.popup(QtGui.QCursor.pos())

    def activate_deactivate_project(self):
        projects = self._get_all_projects()

        project = projects[self.projects_view.currentRow()].Project

        if projects[self.projects_view.currentRow()].Status is 0:
            # Currently deactivated, activate
            self.projects_flow.project_status(project, 1)

        else:
            # Currently enable, deactivate
            self.projects_flow.project_status(project, 0)

        self.write_projects_table()

    def write_projects_table(self):
        projects = self._get_all_projects()

        self.projects_view.setRowCount(len(projects))

        row_counter = 0
        for project in projects:
            # Project name header
            self.projects_view.setItem(row_counter, 0, QtGui.QTableWidgetItem(str(project.Project)))

            # Status header
            if project.Status is 1:
                display_status = "Active"

            else:
                display_status = "Disable"

            self.projects_view.setItem(row_counter, 2, QtGui.QTableWidgetItem(str(display_status)))

            row_counter += 1

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Projects", None))
        ModelProjects.retranslateUi(self, Dialog)
