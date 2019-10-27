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


class ModelCreateTeam(object):
    def __init__(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(443, 89)
        self.setMinimumSize(QtCore.QSize(443, 89))
        self.setMaximumSize(QtCore.QSize(443, 89))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-document-new-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.team_name = QtGui.QLineEdit(self)
        self.team_name.setGeometry(QtCore.QRect(10, 10, 421, 29))
        self.team_name.setText(_fromUtf8(""))
        self.team_name.setObjectName(_fromUtf8("team_name"))
        self.submit_team = QtGui.QPushButton(self)
        self.submit_team.setGeometry(QtCore.QRect(320, 50, 111, 31))
        self.submit_team.setText(_fromUtf8("Create Team"))
        self.submit_team.setObjectName(_fromUtf8("submit_team"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Team", None))
        self.team_name.setToolTip(_translate("Dialog", "<html><head/><body><p>Team name</p></body></html>", None))
        self.team_name.setPlaceholderText(_translate("Dialog", "Add Team Name Here ...", None))
        self.submit_team.setToolTip(_translate("Dialog", "<html><head/><body><p>Push to create team</p></body></html>", None))

