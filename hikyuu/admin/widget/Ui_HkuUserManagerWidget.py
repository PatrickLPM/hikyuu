# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_HkuUserManagerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserManagerForm(object):
    def setupUi(self, UserManagerForm):
        UserManagerForm.setObjectName("UserManagerForm")
        UserManagerForm.resize(642, 400)
        self.formLayout = QtWidgets.QFormLayout(UserManagerForm)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_user_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.add_user_pushButton.setObjectName("add_user_pushButton")
        self.horizontalLayout.addWidget(self.add_user_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.horizontalLayout.addWidget(self.remove_pushButton)
        self.reset_password_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.reset_password_pushButton.setObjectName("reset_password_pushButton")
        self.horizontalLayout.addWidget(self.reset_password_pushButton)
        self.refresh_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.refresh_pushButton.setObjectName("refresh_pushButton")
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(UserManagerForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(UserManagerForm)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.userid_lineEdit = QtWidgets.QLineEdit(UserManagerForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userid_lineEdit.sizePolicy().hasHeightForWidth())
        self.userid_lineEdit.setSizePolicy(sizePolicy)
        self.userid_lineEdit.setMaxLength(100)
        self.userid_lineEdit.setObjectName("userid_lineEdit")
        self.horizontalLayout_2.addWidget(self.userid_lineEdit)
        self.label_2 = QtWidgets.QLabel(UserManagerForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.name_lineEdit = QtWidgets.QLineEdit(UserManagerForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_lineEdit.setSizePolicy(sizePolicy)
        self.name_lineEdit.setMaxLength(100)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout_2.addWidget(self.name_lineEdit)
        self.query_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.query_pushButton.setObjectName("query_pushButton")
        self.horizontalLayout_2.addWidget(self.query_pushButton)
        self.reset_pushButton = QtWidgets.QPushButton(UserManagerForm)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout_2.addWidget(self.reset_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(UserManagerForm)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.users_tableView = QtWidgets.QTableView(UserManagerForm)
        self.users_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.users_tableView.setAlternatingRowColors(False)
        self.users_tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.users_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.users_tableView.setSortingEnabled(True)
        self.users_tableView.setObjectName("users_tableView")
        self.users_tableView.horizontalHeader().setDefaultSectionSize(140)
        self.users_tableView.horizontalHeader().setMinimumSectionSize(5)
        self.users_tableView.horizontalHeader().setSortIndicatorShown(True)
        self.users_tableView.horizontalHeader().setStretchLastSection(True)
        self.users_tableView.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.users_tableView)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout)

        self.retranslateUi(UserManagerForm)
        QtCore.QMetaObject.connectSlotsByName(UserManagerForm)

    def retranslateUi(self, UserManagerForm):
        _translate = QtCore.QCoreApplication.translate
        UserManagerForm.setWindowTitle(_translate("UserManagerForm", "Form"))
        self.add_user_pushButton.setText(_translate("UserManagerForm", "Add"))
        self.remove_pushButton.setText(_translate("UserManagerForm", "Remove"))
        self.reset_password_pushButton.setText(_translate("UserManagerForm", "Reset password"))
        self.refresh_pushButton.setText(_translate("UserManagerForm", "Refresh"))
        self.label.setText(_translate("UserManagerForm", "Userid"))
        self.label_2.setText(_translate("UserManagerForm", "Name"))
        self.query_pushButton.setText(_translate("UserManagerForm", "Query"))
        self.reset_pushButton.setText(_translate("UserManagerForm", "Reset"))
