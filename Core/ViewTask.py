from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from GUI.ModelViewTask import ModelViewTask
from Core import TasksFlow
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


class ViewTask(QtGui.QDialog, ModelViewTask):
    def __init__(self, task_data, parent=None):
        super(ViewTask, self).__init__(parent)
        ModelViewTask.__init__(self)

        self.task_data = task_data

        self.projects = list()
        self.flow_task = TasksFlow()

        self.project_assign()
        self.write_task_screen()

        QtCore.QObject.connect(self.update_task, QtCore.SIGNAL(_fromUtf8("clicked()")), self.view_task)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.retranslateUi(self)

    def write_task_screen(self):
        task_name = self.task_data.get("Name")
        task_description = self.task_data.get("Description")

        self.task_name.setText(task_name)
        self.task_description.setText(task_description)

    def project_assign(self):
        """
        Defining the project assigned
        :return:
        """
        projects = self.flow_task.get_projects()
        task_project = self.task_data.get("Project")

        count = 0
        for project in projects:
            project_map = dict()
            project_map.update({"Project": project.Project, "Id": project.Id})
            self.projects.append(project_map)

            self.associated_project.addItem(project.Project)

            if project.Project == task_project.text():
                self.associated_project.setCurrentIndex(count)

            count = count + 1

    def view_task(self):
        """
        View task, this method update the task with new values set by user.
        :return:
        """
        project_id = None
        task_id = self.task_data.get("Id")
        for project in self.projects:
            if project.get("Project") == str(self.associated_project.currentText()):
                project_id = project.get("Id")

        self.flow_task.update_task(int(task_id), self.task_name.text(), self.task_description.toPlainText(), project_id)

        self.accept()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "View Task", None))
        ModelViewTask.retranslateUi(self, Dialog)
