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


class ModelEdit(object):
    def __init__(self):
        self.setObjectName(_fromUtf8("Edit Work Day Hours"))
        self.resize(1161, 213)
        self.setMinimumSize(QtCore.QSize(1161, 213))
        self.setMaximumSize(QtCore.QSize(1161, 213))
        self.setSizeIncrement(QtCore.QSize(1161, 213))
        self.setBaseSize(QtCore.QSize(1161, 213))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("GUI/Icons/Actions-document-edit-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(810, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1141, 151))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_group_box = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.start_group_box.setObjectName(_fromUtf8("start_group_box"))
        self.gridLayoutWidget = QtGui.QWidget(self.start_group_box)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.start_layout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.start_layout.setObjectName(_fromUtf8("start_layout"))
        self.start_secound = QtGui.QSpinBox(self.gridLayoutWidget)
        self.start_secound.setMaximum(60)
        self.start_secound.setObjectName(_fromUtf8("start_secound"))
        self.start_layout.addWidget(self.start_secound, 0, 2, 1, 1)
        self.start_minute = QtGui.QSpinBox(self.gridLayoutWidget)
        self.start_minute.setMaximum(60)
        self.start_minute.setObjectName(_fromUtf8("start_minute"))
        self.start_layout.addWidget(self.start_minute, 0, 1, 1, 1)
        self.start_hour = QtGui.QSpinBox(self.gridLayoutWidget)
        self.start_hour.setMinimum(0)
        self.start_hour.setMaximum(23)
        self.start_hour.setObjectName(_fromUtf8("start_hour"))
        self.start_layout.addWidget(self.start_hour, 0, 0, 1, 1)
        self.set_start = QtGui.QPushButton(self.start_group_box)
        self.set_start.setGeometry(QtCore.QRect(90, 90, 90, 31))
        self.set_start.setObjectName(_fromUtf8("set_start"))
        self.horizontalLayout.addWidget(self.start_group_box)
        self.lunch_group_box = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.lunch_group_box.setObjectName(_fromUtf8("lunch_group_box"))
        self.set_lunch = QtGui.QPushButton(self.lunch_group_box)
        self.set_lunch.setGeometry(QtCore.QRect(90, 90, 90, 31))
        self.set_lunch.setObjectName(_fromUtf8("set_lunch"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.lunch_group_box)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.lunch_layout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.lunch_layout.setObjectName(_fromUtf8("lunch_layout"))
        self.lunch_hour = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.lunch_hour.setMaximum(23)
        self.lunch_hour.setObjectName(_fromUtf8("lunch_hour"))
        self.lunch_layout.addWidget(self.lunch_hour, 0, 0, 1, 1)
        self.lunch_minute = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.lunch_minute.setMaximum(60)
        self.lunch_minute.setObjectName(_fromUtf8("lunch_minute"))
        self.lunch_layout.addWidget(self.lunch_minute, 0, 1, 1, 1)
        self.lunch_second = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.lunch_second.setMaximum(60)
        self.lunch_second.setObjectName(_fromUtf8("lunch_second"))
        self.lunch_layout.addWidget(self.lunch_second, 0, 2, 1, 1)
        self.set_lunch.raise_()
        self.gridLayoutWidget_2.raise_()
        self.start_group_box.raise_()
        self.start_group_box.raise_()
        self.horizontalLayout.addWidget(self.lunch_group_box)
        self.after_lunch_group_box = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.after_lunch_group_box.setObjectName(_fromUtf8("after_lunch_group_box"))
        self.set_after_lunch = QtGui.QPushButton(self.after_lunch_group_box)
        self.set_after_lunch.setGeometry(QtCore.QRect(90, 90, 90, 31))
        self.set_after_lunch.setObjectName(_fromUtf8("set_after_lunch"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.after_lunch_group_box)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.after_lunch_layout = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.after_lunch_layout.setObjectName(_fromUtf8("after_lunch_layout"))
        self.after_lunch_second = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.after_lunch_second.setMaximum(60)
        self.after_lunch_second.setObjectName(_fromUtf8("after_lunch_second"))
        self.after_lunch_layout.addWidget(self.after_lunch_second, 0, 2, 1, 1)
        self.after_lunch_hour = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.after_lunch_hour.setMaximum(23)
        self.after_lunch_hour.setObjectName(_fromUtf8("after_lunch_hour"))
        self.after_lunch_layout.addWidget(self.after_lunch_hour, 0, 0, 1, 1)
        self.after_lunch_minute = QtGui.QSpinBox(self.gridLayoutWidget_3)
        self.after_lunch_minute.setMaximum(60)
        self.after_lunch_minute.setObjectName(_fromUtf8("after_lunch_minute"))
        self.after_lunch_layout.addWidget(self.after_lunch_minute, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.after_lunch_group_box)
        self.end_group_box = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.end_group_box.setObjectName(_fromUtf8("end_group_box"))
        self.set_end_day = QtGui.QPushButton(self.end_group_box)
        self.set_end_day.setGeometry(QtCore.QRect(100, 90, 90, 31))
        self.set_end_day.setObjectName(_fromUtf8("set_end_day"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.end_group_box)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(11, 40, 261, 31))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.end_layout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.end_layout.setObjectName(_fromUtf8("end_layout"))
        self.end_minute = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.end_minute.setMaximum(60)
        self.end_minute.setObjectName(_fromUtf8("end_minute"))
        self.end_layout.addWidget(self.end_minute, 0, 1, 1, 1)
        self.end_second = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.end_second.setMaximum(60)
        self.end_second.setObjectName(_fromUtf8("end_second"))
        self.end_layout.addWidget(self.end_second, 0, 2, 1, 1)
        self.end_hour = QtGui.QSpinBox(self.gridLayoutWidget_4)
        self.end_hour.setMaximum(23)
        self.end_hour.setObjectName(_fromUtf8("end_hour"))
        self.end_layout.addWidget(self.end_hour, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.end_group_box)

    def retranslateUi(self, Dialog):
        self.start_group_box.setTitle(_translate("Dialog", "Start", None))
        self.set_start.setText(_translate("Dialog", "Set", None))
        self.lunch_group_box.setTitle(_translate("Dialog", "Lunch", None))
        self.set_lunch.setText(_translate("Dialog", "Set", None))
        self.after_lunch_group_box.setTitle(_translate("Dialog", "After Lunch", None))
        self.set_after_lunch.setText(_translate("Dialog", "Set", None))
        self.end_group_box.setTitle(_translate("Dialog", "End", None))
        self.set_end_day.setText(_translate("Dialog", "Set", None))
