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
        self.projects_view.setColumnCount(3)
        self.projects_view.verticalHeader().setVisible(False)
        self.projects_view.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Name"))
        self.projects_view.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Client"))
        self.projects_view.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Status"))

        self.write_projects_table()

        self.retranslateUi(self)

    def write_projects_table(self):
        projects = self.projects_flow.get_all_data()

        self.projects_view.setRowCount(len(projects))

        row_counter = 0
        for project in projects:
            self.projects_view.setItem(row_counter, 0, QtGui.QTableWidgetItem(str(project[1])))

            row_counter += 1

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Projects", None))
        ModelProjects.retranslateUi(self, Dialog)
