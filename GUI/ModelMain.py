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


class ModelWindow(object):
    def __init__(self):
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