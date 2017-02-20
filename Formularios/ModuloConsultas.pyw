# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModuloConsultas.ui'
#
# Created: Tue Feb 14 14:06:34 2017
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
        Dialog.resize(634, 443)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabOpFichas = QtGui.QTabWidget(Dialog)
        self.tabOpFichas.setObjectName(_fromUtf8("tabOpFichas"))
        self.tabConsultarFicha = QtGui.QWidget()
        self.tabConsultarFicha.setObjectName(_fromUtf8("tabConsultarFicha"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tabConsultarFicha)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.scrollArea = QtGui.QScrollArea(self.tabConsultarFicha)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 590, 379))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.rbCategoria = QtGui.QRadioButton(self.groupBox)
        self.rbCategoria.setObjectName(_fromUtf8("rbCategoria"))
        self.verticalLayout_7.addWidget(self.rbCategoria)
        self.rbPedidos = QtGui.QRadioButton(self.groupBox)
        self.rbPedidos.setObjectName(_fromUtf8("rbPedidos"))
        self.verticalLayout_7.addWidget(self.rbPedidos)
        self.rbEtiqueta = QtGui.QRadioButton(self.groupBox)
        self.rbEtiqueta.setObjectName(_fromUtf8("rbEtiqueta"))
        self.verticalLayout_7.addWidget(self.rbEtiqueta)
        self.rbCliente = QtGui.QRadioButton(self.groupBox)
        self.rbCliente.setObjectName(_fromUtf8("rbCliente"))
        self.verticalLayout_7.addWidget(self.rbCliente)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.cmbBusqueda = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.cmbBusqueda.setObjectName(_fromUtf8("cmbBusqueda"))
        self.verticalLayout_8.addWidget(self.cmbBusqueda)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.twFichas = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.twFichas.setObjectName(_fromUtf8("twFichas"))
        self.twFichas.setColumnCount(0)
        self.twFichas.setRowCount(0)
        self.verticalLayout_6.addWidget(self.twFichas)
        self.pbMostrarFicha = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbMostrarFicha.setObjectName(_fromUtf8("pbMostrarFicha"))
        self.verticalLayout_6.addWidget(self.pbMostrarFicha)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.tabOpFichas.addTab(self.tabConsultarFicha, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabOpFichas)

        self.retranslateUi(Dialog)
        self.tabOpFichas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Filtrar por", None))
        self.rbCategoria.setText(_translate("Dialog", "Categoria", None))
        self.rbPedidos.setText(_translate("Dialog", "Pedidos", None))
        self.rbEtiqueta.setText(_translate("Dialog", "Etiqueta", None))
        self.rbCliente.setText(_translate("Dialog", "Cliente", None))
        self.pbMostrarFicha.setText(_translate("Dialog", "Mostrar Ficha", None))
        self.tabOpFichas.setTabText(self.tabOpFichas.indexOf(self.tabConsultarFicha), _translate("Dialog", "Consultar Ficha", None))

