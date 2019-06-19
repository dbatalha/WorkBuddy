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


class TrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, QtGui.QIcon("GUI/Icons/main.png"), parent)
        context_menu = QtGui.QMenu(parent)
        restore_action = context_menu.addAction("Restore")
        self.setContextMenu(context_menu)
        self.restore_trigger = False
        restore_action.triggered.connect(self.restore)

        # Activate window, on double click
        self.activated.connect(self.restore)

        # Define parent window
        self.parent_window = parent

        self.tray_icon = None
        self.tray_icon = self

    def display_message(self, title, message):
        """
        Show and hide and display message in the toast format
        :param title:
        :param message:
        :return:
        """
        self.tray_icon.show()
        self.tray_icon.showMessage(title, message)
        self.tray_icon.hide()

    def restore(self):
        self.restore_trigger = True
        self.parent_window.show()
        self.hide()
