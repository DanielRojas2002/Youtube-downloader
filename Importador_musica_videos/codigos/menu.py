# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu_opciones(object):
    def setupUi(self, Menu_opciones):
        Menu_opciones.setObjectName("Menu_opciones")
        Menu_opciones.resize(357, 174)
        self.centralwidget = QtWidgets.QWidget(Menu_opciones)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(10, 10, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 70, 251, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(23, 20, 20, 111))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(320, 20, 20, 111))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 120, 251, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 90, 251, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_opciones = QtWidgets.QComboBox(self.widget)
        self.cb_opciones.setObjectName("cb_opciones")
        self.cb_opciones.addItem("")
        self.cb_opciones.addItem("")
        self.cb_opciones.addItem("")
        self.cb_opciones.addItem("")
        self.horizontalLayout.addWidget(self.cb_opciones)
        self.btn_opciones = QtWidgets.QPushButton(self.widget)
        self.btn_opciones.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opciones.setObjectName("btn_opciones")
        self.horizontalLayout.addWidget(self.btn_opciones)
        Menu_opciones.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_opciones)
        QtCore.QMetaObject.connectSlotsByName(Menu_opciones)

    def retranslateUi(self, Menu_opciones):
        _translate = QtCore.QCoreApplication.translate
        Menu_opciones.setWindowTitle(_translate("Menu_opciones", "DownloadAU"))
        self.lbl_titulo.setText(_translate("Menu_opciones", "<html><head/><body><p align=\"center\">DESCARGADOR DE</p><p align=\"center\">AUDIOS Y VIDEOS DE YOUTUBE</p></body></html>"))
        self.cb_opciones.setItemText(0, _translate("Menu_opciones", "1 a 1 audio"))
        self.cb_opciones.setItemText(1, _translate("Menu_opciones", "Por archivo .txt audio"))
        self.cb_opciones.setItemText(2, _translate("Menu_opciones", "1 a 1 video"))
        self.cb_opciones.setItemText(3, _translate("Menu_opciones", "Por archivo .txt video"))
        self.btn_opciones.setText(_translate("Menu_opciones", "ELEGIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu_opciones = QtWidgets.QMainWindow()
    ui = Ui_Menu_opciones()
    ui.setupUi(Menu_opciones)
    Menu_opciones.show()
    sys.exit(app.exec_())
