from PyQt4 import QtCore, QtGui
from GUI.ModelEdit import ModelEdit
from Database import Database
from Database import BuddyTable
import time
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

        self.time_start = day_hours[0]
        time_start = day_hours[0]
        time_lunch = day_hours[1]
        time_after_lunch = day_hours[2]
        time_end = day_hours[3]

        self.row_id = day_hours[4]

        self.day = str(time_start).split()[0]

        self.database = Database()

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

        # Define time to set
        self.start_time = None
        self.lunch_time = None
        self.after_lunch_time = None
        self.end_time = None

        # Set signals to define time.
        QtCore.QObject.connect(self.set_start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.set_start_time)
        QtCore.QObject.connect(self.set_lunch, QtCore.SIGNAL(_fromUtf8("clicked()")), self.set_lunch_time)
        QtCore.QObject.connect(self.set_after_lunch, QtCore.SIGNAL(_fromUtf8("clicked()")), self.set_after_lunch_time)
        QtCore.QObject.connect(self.set_end_day, QtCore.SIGNAL(_fromUtf8("clicked()")), self.set_end_time)

        self.retranslateUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.submit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_start_time(self):
        hour_value = self.start_hour.value()
        minute_value = self.start_minute.value()
        seconds_value = self.start_secound.value()

        if hour_value < 10:
            hour_value = "0" + str(hour_value)

        if minute_value < 10:
            minute_value = "0" + str(minute_value)

        if seconds_value < 10:
            seconds_value = "0" + str(seconds_value)

        self.start_time = "%s:%s:%s" % (hour_value, minute_value, seconds_value)

    def set_lunch_time(self):
        hour_value = self.lunch_hour.value()
        minute_value = self.lunch_minute.value()
        seconds_value = self.lunch_second.value()

        if hour_value < 10:
            hour_value = "0" + str(hour_value)

        if minute_value < 10:
            minute_value = "0" + str(minute_value)

        if seconds_value < 10:
            seconds_value = "0" + str(seconds_value)

        self.lunch_time = "%s:%s:%s" % (hour_value, minute_value, seconds_value)

    def set_after_lunch_time(self):
        hour_value = self.after_lunch_hour.value()
        minute_value = self.after_lunch_minute.value()
        seconds_value = self.after_lunch_second.value()

        if hour_value < 10:
            hour_value = "0" + str(hour_value)

        if minute_value < 10:
            minute_value = "0" + str(minute_value)

        if seconds_value < 10:
            seconds_value = "0" + str(seconds_value)

        self.after_lunch_time = "%s:%s:%s" % (hour_value, minute_value, seconds_value)

    def set_end_time(self):
        hour_value = self.end_hour.value()
        minute_value = self.end_minute.value()
        seconds_value = self.end_second.value()

        if hour_value < 10:
            hour_value = "0" + str(hour_value)

        if minute_value < 10:
            minute_value = "0" + str(minute_value)

        if seconds_value < 10:
            seconds_value = "0" + str(seconds_value)

        self.end_time = "%s:%s:%s" % (hour_value, minute_value, seconds_value)

    def submit(self):
        pattern = '%d-%m-%Y %H:%M:%S'

        if self.lunch_time is not None:
            lunch_time = self.day + " " + self.lunch_time
            epoch = int(time.mktime(time.strptime(lunch_time, pattern)))

            self.database.session.query(BuddyTable).filter_by(Id=int(self.row_id)).update(
                {
                    "LunchTime": lunch_time,
                    "LunchTimeEpoch": epoch
                })

            self.database.commit()

        if self.after_lunch_time is not None:
            after_lunch_time = self.day + " " + self.after_lunch_time
            epoch = int(time.mktime(time.strptime(after_lunch_time, pattern)))

            self.database.session.query(BuddyTable).filter_by(Id=int(self.row_id)).update(
                {
                    "StartAfterLunch": after_lunch_time,
                    "StartAfterLunchEpoch": epoch
                })

            self.database.commit()

        if self.end_time is not None:
            end_time = self.day + " " + self.end_time
            epoch = int(time.mktime(time.strptime(end_time, pattern)))
            start_epoch = int(time.mktime(time.strptime(self.time_start, pattern)))
            total = int(start_epoch) - int(epoch)

            self.database.session.query(BuddyTable).filter_by(Id=int(self.row_id)).update(
                {
                    "EndWorkTime": end_time,
                    "EndWorkEpoch": epoch,
                    "Total": total
                })

            self.database.commit()

        # Close the dialog window
        self.accept()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit Work Day Hours", None))
        ModelEdit.retranslateUi(self, Dialog)
