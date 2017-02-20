# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConsultaFichaTecnica.ui'
#
# Created: Tue Jan 31 13:10:41 2017
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
        Dialog.resize(563, 443)
        self.verticalLayout_6 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 543, 423))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rbCategoria = QtGui.QRadioButton(self.groupBox)
        self.rbCategoria.setObjectName(_fromUtf8("rbCategoria"))
        self.verticalLayout.addWidget(self.rbCategoria)
        self.rbPedidos = QtGui.QRadioButton(self.groupBox)
        self.rbPedidos.setObjectName(_fromUtf8("rbPedidos"))
        self.verticalLayout.addWidget(self.rbPedidos)
        self.rbEtiqueta = QtGui.QRadioButton(self.groupBox)
        self.rbEtiqueta.setObjectName(_fromUtf8("rbEtiqueta"))
        self.verticalLayout.addWidget(self.rbEtiqueta)
        self.rbCliente = QtGui.QRadioButton(self.groupBox)
        self.rbCliente.setObjectName(_fromUtf8("rbCliente"))
        self.verticalLayout.addWidget(self.rbCliente)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cmbBusqueda = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.cmbBusqueda.setObjectName(_fromUtf8("cmbBusqueda"))
        self.verticalLayout_3.addWidget(self.cmbBusqueda)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.twFichas = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.twFichas.setObjectName(_fromUtf8("twFichas"))
        self.twFichas.setColumnCount(0)
        self.twFichas.setRowCount(0)
        self.verticalLayout_4.addWidget(self.twFichas)
        self.pbMostrarFicha = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbMostrarFicha.setObjectName(_fromUtf8("pbMostrarFicha"))
        self.verticalLayout_4.addWidget(self.pbMostrarFicha)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Consultar Ficha Tecnica", None))
        self.groupBox.setTitle(_translate("Dialog", "Filtrar por", None))
        self.rbCategoria.setText(_translate("Dialog", "Categoria", None))
        self.rbPedidos.setText(_translate("Dialog", "Pedidos", None))
        self.rbEtiqueta.setText(_translate("Dialog", "Etiqueta", None))
        self.rbCliente.setText(_translate("Dialog", "Cliente", None))
        self.pbMostrarFicha.setText(_translate("Dialog", "Mostrar Ficha", None))

