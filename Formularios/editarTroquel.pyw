# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarTroquel.ui'
#
# Created: Mon Feb 13 16:19:46 2017
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
        Dialog.resize(506, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 486, 280))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.fAdhLam = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.fAdhLam.setEnabled(True)
        self.fAdhLam.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fAdhLam.setFrameShadow(QtGui.QFrame.Raised)
        self.fAdhLam.setObjectName(_fromUtf8("fAdhLam"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.fAdhLam)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblTroquel = QtGui.QLabel(self.fAdhLam)
        self.lblTroquel.setObjectName(_fromUtf8("lblTroquel"))
        self.verticalLayout_5.addWidget(self.lblTroquel)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProveedorTroquel = QtGui.QLabel(self.fAdhLam)
        self.lblProveedorTroquel.setObjectName(_fromUtf8("lblProveedorTroquel"))
        self.horizontalLayout.addWidget(self.lblProveedorTroquel)
        self.leProveedorTroquel = QtGui.QLineEdit(self.fAdhLam)
        self.leProveedorTroquel.setObjectName(_fromUtf8("leProveedorTroquel"))
        self.horizontalLayout.addWidget(self.leProveedorTroquel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblFechaTroquel = QtGui.QLabel(self.fAdhLam)
        self.lblFechaTroquel.setObjectName(_fromUtf8("lblFechaTroquel"))
        self.horizontalLayout_2.addWidget(self.lblFechaTroquel)
        self.leObservacionesTroquel = QtGui.QLineEdit(self.fAdhLam)
        self.leObservacionesTroquel.setObjectName(_fromUtf8("leObservacionesTroquel"))
        self.horizontalLayout_2.addWidget(self.leObservacionesTroquel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbEditar = QtGui.QPushButton(self.fAdhLam)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_4.addWidget(self.pbEditar)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbCancelar = QtGui.QPushButton(self.fAdhLam)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_3.addWidget(self.pbCancelar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.fAdhLam, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblTroquel.setText(_translate("Dialog", "Troquel", None))
        self.lblProveedorTroquel.setText(_translate("Dialog", "Proveedor", None))
        self.lblFechaTroquel.setText(_translate("Dialog", "Observaciones", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

