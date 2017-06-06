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


class ModelAbout(object):
    def __init__(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(400, 229)
        self.setMaximumSize(QtCore.QSize(400, 229))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/main.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setSizeGripEnabled(True)
        self.setModal(False)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(300, 190, 90, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 170, 401, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.logo = QtGui.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(20, 50, 71, 71))
        self.logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/main.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.title = QtGui.QLabel(self)
        self.title.setGeometry(QtCore.QRect(110, 30, 231, 31))
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setObjectName(_fromUtf8("title"))
        self.description = QtGui.QLabel(self)
        self.description.setGeometry(QtCore.QRect(110, 70, 211, 51))
        self.description.setObjectName(_fromUtf8("description"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 150, 271, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About WorkBuddy", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">WorkBuddy Version V0.0.4</span></p></body></html>", None))
        self.description.setText(_translate("Dialog", " Keep track of your work hours. \n"
" WorkBuddy sores your data locally on your own \n"
" hard drive.", None))
        self.label.setText(_translate("Dialog", "Open Source Software @ Daniel Batalha", None))