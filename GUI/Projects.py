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

        self.retranslateUi(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Projects", None))
        ModelProjects.retranslateUi(self, Dialog)