# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarColdFoil.ui'
#
# Created: Thu Feb 16 10:46:18 2017
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
        Dialog.resize(509, 300)
        self.horizontalLayout_6 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 280))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.fAdhLam = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.fAdhLam.setEnabled(True)
        self.fAdhLam.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fAdhLam.setFrameShadow(QtGui.QFrame.Raised)
        self.fAdhLam.setObjectName(_fromUtf8("fAdhLam"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.fAdhLam)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lblColdFoil = QtGui.QLabel(self.fAdhLam)
        self.lblColdFoil.setObjectName(_fromUtf8("lblColdFoil"))
        self.verticalLayout_2.addWidget(self.lblColdFoil)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.rbCF = QtGui.QRadioButton(self.fAdhLam)
        self.rbCF.setChecked(True)
        self.rbCF.setObjectName(_fromUtf8("rbCF"))
        self.horizontalLayout_7.addWidget(self.rbCF)
        self.rbHS = QtGui.QRadioButton(self.fAdhLam)
        self.rbHS.setObjectName(_fromUtf8("rbHS"))
        self.horizontalLayout_7.addWidget(self.rbHS)
        spacerItem = QtGui.QSpacerItem(320, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProveedorColdFoil = QtGui.QLabel(self.fAdhLam)
        self.lblProveedorColdFoil.setObjectName(_fromUtf8("lblProveedorColdFoil"))
        self.horizontalLayout.addWidget(self.lblProveedorColdFoil)
        self.leProveedorColdFoil = QtGui.QLineEdit(self.fAdhLam)
        self.leProveedorColdFoil.setObjectName(_fromUtf8("leProveedorColdFoil"))
        self.horizontalLayout.addWidget(self.leProveedorColdFoil)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblAnchoColdFoil = QtGui.QLabel(self.fAdhLam)
        self.lblAnchoColdFoil.setObjectName(_fromUtf8("lblAnchoColdFoil"))
        self.horizontalLayout_2.addWidget(self.lblAnchoColdFoil)
        self.dsbAnchoColdFoil = QtGui.QDoubleSpinBox(self.fAdhLam)
        self.dsbAnchoColdFoil.setDecimals(2)
        self.dsbAnchoColdFoil.setObjectName(_fromUtf8("dsbAnchoColdFoil"))
        self.horizontalLayout_2.addWidget(self.dsbAnchoColdFoil)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbEditar = QtGui.QPushButton(self.fAdhLam)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_3.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.fAdhLam)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_3.addWidget(self.pbCancelar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5.addWidget(self.fAdhLam)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblColdFoil.setText(_translate("Dialog", "Cold Foil", None))
        self.rbCF.setText(_translate("Dialog", "Cold Foil", None))
        self.rbHS.setText(_translate("Dialog", "Hot Stamping", None))
        self.lblProveedorColdFoil.setText(_translate("Dialog", "Proveedor", None))
        self.lblAnchoColdFoil.setText(_translate("Dialog", "Ancho", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

