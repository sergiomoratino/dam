# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 490)
        MainWindow.setStyleSheet("background-color:rgb(222, 255, 252)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 191, 41))
        self.label.setMinimumSize(QtCore.QSize(191, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.dni = QtWidgets.QLabel(self.centralwidget)
        self.dni.setGeometry(QtCore.QRect(31, 61, 31, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dni.setFont(font)
        self.dni.setObjectName("dni")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(31, 117, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nombre.setFont(font)
        self.nombre.setObjectName("nombre")
        self.apellidos = QtWidgets.QLabel(self.centralwidget)
        self.apellidos.setGeometry(QtCore.QRect(31, 174, 92, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.apellidos.setFont(font)
        self.apellidos.setObjectName("apellidos")
        self.genero = QtWidgets.QLabel(self.centralwidget)
        self.genero.setGeometry(QtCore.QRect(31, 230, 68, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.genero.setFont(font)
        self.genero.setObjectName("genero")
        self.direccion = QtWidgets.QLabel(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(31, 287, 94, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.direccion.setFont(font)
        self.direccion.setObjectName("direccion")
        self.fnacimiento = QtWidgets.QLabel(self.centralwidget)
        self.fnacimiento.setGeometry(QtCore.QRect(31, 343, 122, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fnacimiento.setFont(font)
        self.fnacimiento.setObjectName("fnacimiento")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(31, 400, 136, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 220, 321, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 160, 321, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 60, 321, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 110, 321, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(210, 270, 321, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(210, 330, 321, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(210, 390, 321, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(159, 255, 117);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(571, 308, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(159, 255, 117);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(571, 152, 198, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(159, 255, 117);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(571, 230, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(159, 255, 117);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 440, 221, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/DERECHA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 440, 221, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Desktop/IZQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.textEdit_5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clientes"))
        self.label.setText(_translate("MainWindow", "CLIENTES"))
        self.dni.setText(_translate("MainWindow", "DNI"))
        self.nombre.setText(_translate("MainWindow", "NOMBRE"))
        self.apellidos.setText(_translate("MainWindow", "APELLIDOS"))
        self.genero.setText(_translate("MainWindow", "GÉNERO"))
        self.direccion.setText(_translate("MainWindow", "DIRECCIÓN"))
        self.fnacimiento.setText(_translate("MainWindow", "F.NACIMIENTO"))
        self.label_8.setText(_translate("MainWindow", "CODIGO POSTAL"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MASCULINO"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FEMENINO"))
        self.pushButton.setText(_translate("MainWindow", "ACTUALIZAR DATOS"))
        self.pushButton_2.setText(_translate("MainWindow", "AÑADIR CLIENTE"))
        self.pushButton_3.setText(_translate("MainWindow", "ELIMINAR CLIENTE"))
        self.pushButton_4.setText(_translate("MainWindow", "BUSCAR CLIENTE"))
        self.pushButton_5.setText(_translate("MainWindow", "SIGUIENTE CLIENTE"))
        self.pushButton_6.setText(_translate("MainWindow", "SIGUIENTE CLIENTE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
