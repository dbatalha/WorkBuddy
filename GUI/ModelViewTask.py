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


class ModelViewTask(object):
    def __init__(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(754, 446)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-document-new-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 751, 391))
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
        self.task_description = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.task_description.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.task_description.setObjectName(_fromUtf8("task_description"))
        self.verticalLayout.addWidget(self.task_description)
        self.update_task = QtGui.QPushButton(self)
        self.update_task.setGeometry(QtCore.QRect(650, 410, 94, 33))
        self.update_task.setObjectName(_fromUtf8("update_task"))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Task", None))
        self.task_name.setToolTip(_translate("Dialog", "<html><head/><body><p>Task Name</p></body></html>", None))
        self.task_name.setPlaceholderText(_translate("Dialog", "Add Task Name Here ...", None))
        self.task_description.setToolTip(_translate("Dialog", "<html><head/><body><p>Task Description</p></body></html>", None))
        self.update_task.setText(_translate("Dialog", "Update", None))
