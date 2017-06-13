from PyQt4 import QtCore, QtGui
from ModelEdit import ModelEdit
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


class Edit(QtGui.QDialog, ModelEdit):
    def __init__(self, day_hours, parent=None):
        super(Edit, self).__init__(parent)
        ModelEdit.__init__(self)

        time_start = day_hours[0]
        time_lunch = day_hours[1]
        time_after_lunch = day_hours[2]
        time_end = day_hours[3]

        if time_start == "EMPTY":
            self.start_group_box.setEnabled(True)

        else:
            self.start_group_box.setEnabled(False)

        if time_lunch == "EMPTY":
            self.lunch_group_box.setEnabled(True)

        else:
            self.lunch_group_box.setEnabled(False)

        if time_after_lunch == "EMPTY":
            self.after_lunch_group_box.setEnabled(True)
        else:
            self.after_lunch_group_box.setEnabled(False)

        if time_end == "EMPTY":
            self.end_group_box.setEnabled(True)
        else:
            self.end_group_box.setEnabled(False)

        self.retranslateUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        ModelEdit.retranslateUi(self, Dialog)
