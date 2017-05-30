from PyQt4 import QtCore, QtGui
from Buddy import Work
from Buddy import Collection
from Buddy import Export
from ModelMain import ModelWindow
import sys
import os.path
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


class UpdateWatch(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(UpdateWatch, self).__init__(parent)
        self.loop_status = True

    def update_watch_status(self, status):
        self.loop_status = status

    def run(self):
        tic_seconds = 00
        tic_minutes = 00
        tic_hours = 00

        while True:
            time.sleep(1)
            tic_seconds += 1
            if tic_seconds > 59:
                tic_seconds = 00
                tic_minutes += 1

            if tic_minutes > 59:
                tic_seconds = 00
                tic_minutes = 00
                tic_hours += 1

            # Put 0 behind number if less than 10
            # Statement for seconds
            if tic_seconds < 10:
                tic_seconds_string = str("0%s" % tic_seconds)

            else:
                tic_seconds_string = str(tic_seconds)

            # Statement for minutes
            if tic_minutes < 10:
                tic_minutes_string = str("0%s" % tic_minutes)

            else:
                tic_minutes_string = str(tic_minutes)

            # Statement for hours
            if tic_hours < 10:
                tic_hours_string = str("0%s" % tic_hours)

            else:
                tic_hours_string = str(tic_hours)

            if self.loop_status is False:
                break
            else:
                pass

            string_time = "<html><head/><body><p align=\"center\">%s:%s:%s</p></body></html>" %\
                          (tic_hours_string, tic_minutes_string, tic_seconds_string)

            self.updated.emit(str(string_time))


class Window(QtGui.QMainWindow, ModelWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        ModelWindow.__init__(self)

        # Tables properties
        self.last_work_days.setColumnCount(6)
        self.last_work_days.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Start"))
        self.last_work_days.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Lunch"))
        self.last_work_days.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("After Lunch"))
        self.last_work_days.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("End"))
        self.last_work_days.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("Total"))
        self.last_work_days.setHorizontalHeaderItem(5, QtGui.QTableWidgetItem("Username"))

        self.ui_translate(self)

        # Instance Collection
        self.collection = Collection()

        # Display data on table.
        self.construct_data_grid()

        self.stage = "morning"

        if not os.path.isfile("data.db"):
            self.file_exist = False
        else:
            self.file_exist = True

        self._update_watch = UpdateWatch(self)
        self._update_watch.updated.connect(self.update_text)

        # Set signals slots
        QtCore.QObject.connect(self.start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buddy_action)
        QtCore.QObject.connect(self.export_xls, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export)
        QtCore.QObject.connect(self.refress_work_days, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update_table)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.start.clicked.connect(self._update_watch.start)

        # Main menu items
        self.actionExit.triggered.connect(self.close_application)

        # Buddy main instance
        self.buddy_main = Work()

        # Write data to status bar, this is the database file and file size.
        self.statusbar.showMessage("Click on button Start Day")

    def ui_translate(self, main_window):
        ModelWindow.ui_translate(self, main_window)

    def buddy_action(self):
        if self.buddy_main.state() == "Void":
            if not self.file_exist:
                self.buddy_main.create_data()

            self.buddy_main.start()
            self.statusbar.showMessage("Currently on morning shift")

            self.start.setText("Launch")

        elif self.buddy_main.state() == "Started":
            self.buddy_main.launch()
            self.statusbar.showMessage("Finally lunch time")

            self.start.setText("Start After Launch")

        elif self.buddy_main.state() == "Launch":
            self.buddy_main.return_from_launch()
            self.statusbar.showMessage("Currently on afternoon shift")

            self.start.setText("End Day")

        elif self.buddy_main.state() == "After_Launch":
            self.buddy_main.end_day()

            self.start.setText("Start Day")

            self._update_watch.terminate()

            self._update_watch.update_watch_status(False)
            self.label.setText("<html><head/><body><p align=\"center\">HH:MM:SS</p></body></html>")
            self.statusbar.showMessage("Click on button Start Day")

        else:
            raise ValueError("Invalid Option")

    def update_table(self):
        """
        Update work log table
        :return:
        """
        self.clear_table()

        # Instance Collection
        self.collection = Collection()

        # Display data on table.
        self.construct_data_grid()

    def clear_table(self):
        """
        Clear work log table
        :return:
        """
        self.last_work_days.clearContents()

    def update_text(self, text):
        self.label.setText(text)

    def construct_data_grid(self):
        # Get all data from table buddy and convert to python object list.
        all_data = self.collection.get_all_data()
        all_data = list(all_data)

        self.last_work_days.setRowCount(len(all_data))

        row_counter = 0
        for row in all_data:
            header = self.last_work_days.horizontalHeader()

            # Add username to GUI table
            self.last_work_days.setItem(row_counter, 5, QtGui.QTableWidgetItem(row[9]))
            header.setResizeMode(5, QtGui.QHeaderView.ResizeToContents)

            # Add Total, this value could be empty (None).
            if row[8] is not None:
                self.last_work_days.setItem(row_counter, 4, QtGui.QTableWidgetItem(row[8]))
            else:
                self.last_work_days.setItem(row_counter, 4, QtGui.QTableWidgetItem("EMPTY"))
            header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)

            # Add end work time in date format to GUI table.
            if row[4] is not None:
                self.last_work_days.setItem(row_counter, 3, QtGui.QTableWidgetItem(row[4]))
            else:
                self.last_work_days.setItem(row_counter, 3, QtGui.QTableWidgetItem("EMPTY"))
            header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)

            # Add after lunch time in date format to GUI table.
            if row[6] is not None:
                self.last_work_days.setItem(row_counter, 2, QtGui.QTableWidgetItem(row[6]))
            else:
                self.last_work_days.setItem(row_counter, 2, QtGui.QTableWidgetItem("EMPTY"))
            header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)

            # Add lunch time in date format to GUI table.
            if row[2] is not None:
                self.last_work_days.setItem(row_counter, 1, QtGui.QTableWidgetItem(row[2]))
            else:
                self.last_work_days.setItem(row_counter, 1, QtGui.QTableWidgetItem("EMPTY"))
            header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)

            # Add start work time in date format to GUI table.
            if row[0] is not None:
                self.last_work_days.setItem(row_counter, 0, QtGui.QTableWidgetItem(row[0]))
            else:
                self.last_work_days.setItem(row_counter, 0, QtGui.QTableWidgetItem("EMPTY"))
            header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)

            row_counter += 1

    @ staticmethod
    def export():
        export = Export()
        export.export_csv()

    @ staticmethod
    def close_application():
        sys.exit()

