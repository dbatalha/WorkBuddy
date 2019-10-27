from PyQt4 import QtCore, QtGui

from Core.TrayIcon import TrayIcon
from GUI.ModelCreateTeam import ModelCreateTeam
from Core import TeamsFlow
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


class CreateTeam(QtGui.QDialog, ModelCreateTeam):
    def __init__(self, parent=None):
        super(CreateTeam, self).__init__(parent)
        ModelCreateTeam.__init__(self)

        self.flow_create_team = TeamsFlow()

        QtCore.QObject.connect(self.submit_team, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_team)
        QtCore.QMetaObject.connectSlotsByName(self)

        # Tray icon application
        self.tray_icon = None
        self.tray_icon = TrayIcon(self)

        self.retranslateUi(self)

    def create_team(self):
        """
        Create team
        The default status of the project is active
        :return:
        """
        team = self.team_name.text()

        self.flow_create_team.add_team(str(team).encode('utf-8'), True)
        self.accept()

        # TODO : add to translation
        title = "Teams Flow"
        message = str(team) + " created."

        self.tray_icon.display_message(title, message)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Team", None))
        ModelCreateTeam.retranslateUi(self, Dialog)
