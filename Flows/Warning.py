from PyQt4 import QtCore, QtGui
from GUI.ModelWarning import ModelWarning
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


class Warning(QtGui.QDialog, ModelWarning):
    def __init__(self, message, parent=None):
        super(Warning, self).__init__(parent)
        ModelWarning.__init__(self)

        self.event_action = False

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.event_accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.retranslateUi(self)

        self.message.setText(message)

    def retranslateUi(self, Dialog):
        ModelWarning.retranslateUi(self, Dialog)

    def event_accept(self):
        self.event_action = True
        self.accept()
