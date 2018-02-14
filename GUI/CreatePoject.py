from PyQt4 import QtCore, QtGui
from ModelCreateProject import ModelCreatePoject
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


class CreateProject(QtGui.QDialog, ModelCreatePoject):
    def __init__(self, parent=None):
        super(CreateProject, self).__init__(parent)
        ModelCreatePoject.__init__(self)

        self.flow_create_project = ProjectsFlow()

        QtCore.QObject.connect(self.submit_project, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_project)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.retranslateUi(self)

    def create_project(self):
        """
        Create project
        The default status of the project is active
        :return:
        """
        project = self.project_name.text()

        self.flow_create_project.add_project(str(project), True)
        self.accept()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Project", None))
        ModelCreatePoject.retranslateUi(self, Dialog)
