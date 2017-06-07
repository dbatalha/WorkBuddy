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


class ModelWarning(object):
    def __init__(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(370, 140)
        self.setMinimumSize(QtCore.QSize(370, 140))
        self.setMaximumSize(QtCore.QSize(370, 140))
        self.setBaseSize(QtCore.QSize(370, 140))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Status-dialog-warning-icon.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setSizeGripEnabled(True)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.warning = QtGui.QLabel(self)
        self.warning.setGeometry(QtCore.QRect(20, 20, 71, 81))
        self.warning.setText(_fromUtf8(""))
        self.warning.setPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Status-dialog-warning-icon.png")))
        self.warning.setObjectName(_fromUtf8("warning"))
        self.message = QtGui.QLabel(self)
        self.message.setGeometry(QtCore.QRect(110, 50, 211, 21))
        self.message.setObjectName(_fromUtf8("message"))

        self.retranslateUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Warning", None))
        self.message.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TextLabel</span></p></body></html>",
                                        None))