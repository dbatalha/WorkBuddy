from PyQt4 import QtCore, QtGui
from ModelCreateProject import ModelCreatePoject
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

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Project", None))
        ModelCreatePoject.retranslateUi(self, Dialog)
