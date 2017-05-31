from PyQt4 import QtCore, QtGui
from ModelAbout import ModelAbout
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


class About(QtGui.QDialog, ModelAbout):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        ModelAbout.__init__(self)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept)

        self.retranslateUi(self)

    def retranslateUi(self, Dialog):
        ModelAbout.retranslateUi(self, Dialog)
