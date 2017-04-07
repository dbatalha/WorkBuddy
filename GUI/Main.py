from PyQt4 import QtCore, QtGui
from Buddy import Work
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

            string_time = "%s:%s:%s" % (tic_hours_string, tic_minutes_string, tic_seconds_string)

            self.updated.emit(str(string_time))


class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Set Icon to MainWindow.
        self.setWindowIcon(QtGui.QIcon('GUI/Icons/main.png'))

        # Set main window object
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(673, 620)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 359, 129))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.start = QtGui.QPushButton(self.groupBox)
        self.start.setGeometry(QtCore.QRect(20, 50, 163, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(200, 0, 246, 129))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.last_work_days = QtGui.QTableView(self.centralwidget)
        self.last_work_days.setGeometry(QtCore.QRect(0, 150, 671, 421))
        self.last_work_days.setObjectName(_fromUtf8("last_work_days"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(370, 0, 301, 121))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.export_xls = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.export_xls.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Mimes-x-office-spreadsheet-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_xls.setIcon(icon)
        self.export_xls.setIconSize(QtCore.QSize(48, 48))
        self.export_xls.setObjectName(_fromUtf8("export_xls"))
        self.gridLayout_2.addWidget(self.export_xls, 0, 1, 1, 1)
        self.refress_work_days = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.refress_work_days.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-edit-redo-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refress_work_days.setIcon(icon1)
        self.refress_work_days.setIconSize(QtCore.QSize(48, 48))
        self.refress_work_days.setObjectName(_fromUtf8("refress_work_days"))
        self.gridLayout_2.addWidget(self.refress_work_days, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-edit-delete-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 27))
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

        self.ui_translate(self)

        self.stage = "morning"

        if not os.path.isfile("data.db"):
            self.file_exist = False
        else:
            self.file_exist = True

        self._update_watch = UpdateWatch(self)
        self._update_watch.updated.connect(self.update_text)

        # Set signals slots
        QtCore.QObject.connect(self.start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buddy_action)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.start.clicked.connect(self._update_watch.start)

        # Main menu items
        self.actionExit.triggered.connect(self.close_application)

        # Buddy main instance
        self.buddy_main = Work()

    def ui_translate(self, main_window):
        main_window.setWindowTitle(_translate("WorkBuddy", "WorkBuddy", None))
        self.groupBox.setTitle(_translate("MainWindow", "WorkTime", None))
        self.start.setText(_translate("MainWindow", "Start Day", None))
        self.label.setText(_translate("MainWindow", "HH:MM:SS", None))
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

            self.start.setText("Launch")

        elif self.buddy_main.state() == "Started":
            self.buddy_main.launch()

            self.start.setText("Start After Launch")

        elif self.buddy_main.state() == "Launch":
            self.buddy_main.return_from_launch()

            self.start.setText("End Day")

        elif self.buddy_main.state() == "After_Launch":
            self.buddy_main.end_day()

            self.start.setText("Start Day")

            self._update_watch.terminate()

            self.label.setText("HH:MM:SS")

        else:
            raise ValueError("Invalid Option")

    def update_text(self, text):
        self.label.setText(text)

    @ staticmethod
    def close_application():
        sys.exit()

