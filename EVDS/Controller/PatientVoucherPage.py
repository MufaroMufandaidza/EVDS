# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PatientVoucherPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PatientVoucherPage(object):
    def setupUi(self, PatientVoucherPage):
        PatientVoucherPage.setObjectName("PatientVoucherPage")
        PatientVoucherPage.resize(400, 300)
        self.label = QtWidgets.QLabel(PatientVoucherPage)
        self.label.setGeometry(QtCore.QRect(130, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lb_voucher = QtWidgets.QLabel(PatientVoucherPage)
        self.lb_voucher.setGeometry(QtCore.QRect(170, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_voucher.setFont(font)
        self.lb_voucher.setObjectName("lb_voucher")
        self.label_2 = QtWidgets.QLabel(PatientVoucherPage)
        self.label_2.setGeometry(QtCore.QRect(110, 140, 211, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(PatientVoucherPage)
        QtCore.QMetaObject.connectSlotsByName(PatientVoucherPage)

    def retranslateUi(self, PatientVoucherPage):
        _translate = QtCore.QCoreApplication.translate
        PatientVoucherPage.setWindowTitle(_translate("PatientVoucherPage", "Electronic Vaccination Data System"))
        self.label.setText(_translate("PatientVoucherPage", "This is your Voucher: "))
        self.lb_voucher.setText(_translate("PatientVoucherPage", "TextLabel"))
        self.label_2.setText(_translate("PatientVoucherPage", "Keep it safe for future reference"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatientVoucherPage = QtWidgets.QWidget()
    ui = Ui_PatientVoucherPage()
    ui.setupUi(PatientVoucherPage)
    PatientVoucherPage.show()
    sys.exit(app.exec_())
