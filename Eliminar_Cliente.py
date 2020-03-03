# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eliminar_Cliente.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from cliente_controller import ClienteController



class Ui_EliminarCliente():
    dniRecogido=""
    def setupUi(self, EliminarCliente):
        EliminarCliente.setObjectName("EliminarCliente")
        EliminarCliente.resize(604, 0)
        EliminarCliente.setStyleSheet("background-color:rgb(222, 255, 252)")
        self.centralwidget = QtWidgets.QWidget(EliminarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 80, 291, 31))       
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        EliminarCliente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EliminarCliente)
        self.statusbar.setObjectName("statusbar")
        EliminarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(EliminarCliente)
        QtCore.QMetaObject.connectSlotsByName(EliminarCliente)

    def retranslateUi(self, EliminarCliente):
        _translate = QtCore.QCoreApplication.translate
        EliminarCliente.setWindowTitle(_translate("EliminarCliente", "Eliminar Cliente"))
        self.label.setText(_translate("EliminarCliente", "INGRESE EL DNI DEL CLIENTE QUE DESEE ELIMINAR"))
        self.pushButton.setText(_translate("EliminarCliente", "ELIMINAR"))
        self.pushButton_2.setText(_translate("EliminarCliente", "CANCELAR"))

        #dando funcionalidad a eliminar
        self.pushButton.clicked.connect(self.eliminar)
    
    def eliminar(self): 
        dniRecogido = str(self.textEdit.to)
        return dniRecogido
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarCliente = QtWidgets.QMainWindow()
    ui = Ui_EliminarCliente()
    ui.setupUi(EliminarCliente)
    EliminarCliente.show()
    sys.exit(app.exec_())

