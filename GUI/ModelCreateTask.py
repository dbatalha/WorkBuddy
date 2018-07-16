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
        self.resize(372, 157)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-view-pim-tasks-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.submit_task = QtGui.QPushButton(self)
        self.submit_task.setGeometry(QtCore.QRect(260, 120, 105, 31))
        self.submit_task.setText(_fromUtf8("Create Task"))
        self.submit_task.setObjectName(_fromUtf8("submit_project"))
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 371, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.task_name = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.task_name.setText(_fromUtf8(""))
        self.task_name.setObjectName(_fromUtf8("task_name"))
        self.verticalLayout.addWidget(self.task_name)
        self.associated_project = QtGui.QComboBox(self.verticalLayoutWidget)
        self.associated_project.setObjectName(_fromUtf8("associated_project"))
        self.verticalLayout.addWidget(self.associated_project)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Task", None))
        self.submit_task.setToolTip(_translate("Dialog", "<html><head/><body><p>Push to create task</p></body></html>", None))
        self.task_name.setToolTip(_translate("Dialog", "<html><head/><body><p>Project name</p></body></html>", None))
        self.task_name.setPlaceholderText(_translate("Dialog", "Add Task Name Here ...", None))