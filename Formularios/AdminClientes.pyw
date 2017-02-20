# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminClientes.ui'
#
# Created: Sun Jan 22 11:11:08 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(476, 323)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 456, 303))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblRut = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblRut.setObjectName(_fromUtf8("lblRut"))
        self.horizontalLayout.addWidget(self.lblRut)
        self.leRut = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.leRut.setObjectName(_fromUtf8("leRut"))
        self.horizontalLayout.addWidget(self.leRut)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblNombre = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblNombre.setObjectName(_fromUtf8("lblNombre"))
        self.horizontalLayout_2.addWidget(self.lblNombre)
        self.leNombre = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.leNombre.setObjectName(_fromUtf8("leNombre"))
        self.horizontalLayout_2.addWidget(self.leNombre)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pbAniadir = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbAniadir.setObjectName(_fromUtf8("pbAniadir"))
        self.verticalLayout.addWidget(self.pbAniadir)
        self.pbEditar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.verticalLayout.addWidget(self.pbEditar)
        self.pbEliminar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbEliminar.setObjectName(_fromUtf8("pbEliminar"))
        self.verticalLayout.addWidget(self.pbEliminar)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lblCliente = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblCliente.setObjectName(_fromUtf8("lblCliente"))
        self.verticalLayout_2.addWidget(self.lblCliente)
        self.twCliente = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.twCliente.setObjectName(_fromUtf8("twCliente"))
        self.twCliente.setColumnCount(2)
        self.twCliente.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twCliente.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twCliente.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.twCliente)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblRut.setText(_translate("Dialog", "Rut Cliente", None))
        self.lblNombre.setText(_translate("Dialog", "Nombre Cliente", None))
        self.pbAniadir.setText(_translate("Dialog", "Añadir Cliente", None))
        self.pbEditar.setText(_translate("Dialog", "Editar Cliente", None))
        self.pbEliminar.setText(_translate("Dialog", "Eliminar Cliente", None))
        self.lblCliente.setText(_translate("Dialog", "Clientes", None))
        item = self.twCliente.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Rut ", None))
        item = self.twCliente.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre", None))

