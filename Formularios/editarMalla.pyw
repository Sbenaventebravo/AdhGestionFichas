# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarMalla.ui'
#
# Created: Tue Feb 14 10:19:51 2017
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
        Dialog.resize(410, 219)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 390, 199))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lblMalla = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblMalla.setObjectName(_fromUtf8("lblMalla"))
        self.verticalLayout_3.addWidget(self.lblMalla)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.lblTipo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblTipo.setObjectName(_fromUtf8("lblTipo"))
        self.horizontalLayout_13.addWidget(self.lblTipo)
        self.leTipoMalla = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.leTipoMalla.setObjectName(_fromUtf8("leTipoMalla"))
        self.horizontalLayout_13.addWidget(self.leTipoMalla)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.gbSelIntExt = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gbSelIntExt.setObjectName(_fromUtf8("gbSelIntExt"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.gbSelIntExt)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.rbInterno = QtGui.QRadioButton(self.gbSelIntExt)
        self.rbInterno.setChecked(True)
        self.rbInterno.setObjectName(_fromUtf8("rbInterno"))
        self.horizontalLayout_14.addWidget(self.rbInterno)
        self.rbExterno = QtGui.QRadioButton(self.gbSelIntExt)
        self.rbExterno.setObjectName(_fromUtf8("rbExterno"))
        self.horizontalLayout_14.addWidget(self.rbExterno)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_17.addWidget(self.gbSelIntExt)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pbEditar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_2.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_2.addWidget(self.pbCancelar)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblMalla.setText(_translate("Dialog", "Malla", None))
        self.lblTipo.setText(_translate("Dialog", "Tipo", None))
        self.gbSelIntExt.setTitle(_translate("Dialog", "Interno/Externo", None))
        self.rbInterno.setText(_translate("Dialog", "Interno", None))
        self.rbExterno.setText(_translate("Dialog", "Externo", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

