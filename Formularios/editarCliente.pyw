# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarCliente.ui'
#
# Created: Sun Jan 22 12:06:41 2017
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
        Dialog.resize(400, 190)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 170))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblRut = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblRut.setObjectName(_fromUtf8("lblRut"))
        self.horizontalLayout_5.addWidget(self.lblRut)
        self.leRut = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.leRut.setObjectName(_fromUtf8("leRut"))
        self.horizontalLayout_5.addWidget(self.leRut)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lblNombre = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblNombre.setObjectName(_fromUtf8("lblNombre"))
        self.horizontalLayout_6.addWidget(self.lblNombre)
        self.leNombre = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.leNombre.setObjectName(_fromUtf8("leNombre"))
        self.horizontalLayout_6.addWidget(self.leNombre)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbEditar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout.addWidget(self.pbCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblRut.setText(_translate("Dialog", "Rut Cliente", None))
        self.lblNombre.setText(_translate("Dialog", "Nombre Cliente", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

