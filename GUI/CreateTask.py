from PyQt4 import QtCore, QtGui
from ModelCreateTask import ModelCreateTask
from Buddy import TasksFlow
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


class CreateTask(QtGui.QDialog, ModelCreateTask):
    def __init__(self, parent=None):
        super(CreateTask, self).__init__(parent)
        ModelCreateTask.__init__(self)

        self.flow_create_task = TasksFlow()

        self.project_assign()

        QtCore.QObject.connect(self.submit_task, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_task)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.retranslateUi(self)

    def project_assign(self):
        """
        Defining the project assigned
        :return:
        """
        projects = self.flow_create_task.get_projects()

        for project in projects:
            self.associated_project.addItem(project.Project)


    def create_task(self):
        """
        Create project
        The default status of the project is active
        :return:
        """
        task = self.task_name.text()

        self.flow_create_task.add_task(str(task), 1)
        self.accept()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Task", None))
        ModelCreateTask.retranslateUi(self, Dialog)
