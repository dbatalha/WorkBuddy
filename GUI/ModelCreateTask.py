from PyQt4 import QtCore, QtGui
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


class ModelCreateTask(object):
    def __init__(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(443, 89)
        self.setMinimumSize(QtCore.QSize(443, 89))
        self.setMaximumSize(QtCore.QSize(443, 89))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-view-pim-tasks-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.task_name = QtGui.QLineEdit(self)
        self.task_name.setGeometry(QtCore.QRect(10, 10, 421, 29))
        self.task_name.setText(_fromUtf8(""))
        self.task_name.setObjectName(_fromUtf8("project_name"))
        self.submit_task = QtGui.QPushButton(self)
        self.submit_task.setGeometry(QtCore.QRect(320, 50, 111, 31))
        self.submit_task.setText(_fromUtf8("Create Task"))
        self.submit_task.setObjectName(_fromUtf8("submit_project"))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Task", None))
        self.task_name.setToolTip(_translate("Dialog", "<html><head/><body><p>Project name</p></body></html>", None))
        self.task_name.setPlaceholderText(_translate("Dialog", "Task Name Here ...", None))
        self.submit_task.setToolTip(_translate("Dialog", "<html><head/><body><p>Push to create task</p></body></html>", None))
