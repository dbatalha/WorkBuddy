from PyQt4 import QtCore, QtGui
from Buddy import Work
from Buddy import Collection
from Buddy import Export
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

            string_time = "<html><head/><body><p align=\"center\">%s:%s:%s</p></body></html>" %\
                          (tic_hours_string, tic_minutes_string, tic_seconds_string)

            self.updated.emit(str(string_time))


class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Set Icon to MainWindow.
        self.setWindowIcon(QtGui.QIcon('GUI/Icons/main.png'))

        # Set main window object
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(944, 663)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(944, 616))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.last_work_days = QtGui.QTableWidget(self.centralwidget)
        self.last_work_days.setObjectName(_fromUtf8("last_work_days"))
        self.last_work_days.setColumnCount(0)
        self.last_work_days.setRowCount(0)
        self.gridLayout.addWidget(self.last_work_days, 1, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 66))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.start = QtGui.QPushButton(self.groupBox)
        self.start.setObjectName(_fromUtf8("start"))
        self.gridLayout_3.addWidget(self.start, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.start.raise_()
        self.label.raise_()
        self.last_work_days.raise_()
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.export_xls = QtGui.QPushButton(self.centralwidget)
        self.export_xls.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Mimes-x-office-spreadsheet-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_xls.setIcon(icon)
        self.export_xls.setIconSize(QtCore.QSize(48, 48))
        self.export_xls.setObjectName(_fromUtf8("export_xls"))
        self.gridLayout_2.addWidget(self.export_xls, 0, 1, 1, 1)
        self.refress_work_days = QtGui.QPushButton(self.centralwidget)
        self.refress_work_days.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-edit-redo-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refress_work_days.setIcon(icon1)
        self.refress_work_days.setIconSize(QtCore.QSize(48, 48))
        self.refress_work_days.setObjectName(_fromUtf8("refress_work_days"))
        self.gridLayout_2.addWidget(self.refress_work_days, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-edit-delete-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label.raise_()
        self.label.raise_()
        self.last_work_days.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.actionExport = QtGui.QAction(self)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionHistory = QtGui.QAction(self)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.actionExit = QtGui.QAction(self)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(self)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionHistory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

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
        QtCore.QMetaObject.connectSlotsByName(self)

        self.start.clicked.connect(self._update_watch.start)

        # Main menu items
        self.actionExit.triggered.connect(self.close_application)

        # Buddy main instance
        self.buddy_main = Work()

        # Write data to status bar, this is the database file and file size.
        self.statusbar.showMessage("Click on button Start Day")

    def ui_translate(self, main_window):
        main_window.setWindowTitle(_translate("WorkBuddy", "WorkBuddy", None))
        self.groupBox.setTitle(_translate("MainWindow", "WorkTime", None))
        self.start.setText(_translate("MainWindow", "Start Day", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">HH:MM:SS</p></body></html>",
                                      None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionHistory.setText(_translate("MainWindow", "History", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

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

            self.label.setText("<html><head/><body><p align=\"center\">HH:MM:SS</p></body></html>")
            self.statusbar.showMessage("Click on button Start Day")

        else:
            raise ValueError("Invalid Option")

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

