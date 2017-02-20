# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarAdhCF.ui'
#
# Created: Mon Feb 13 15:50:24 2017
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
        self.horizontalLayout_5 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 280))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fAdhLam = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.fAdhLam.setEnabled(True)
        self.fAdhLam.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fAdhLam.setFrameShadow(QtGui.QFrame.Raised)
        self.fAdhLam.setObjectName(_fromUtf8("fAdhLam"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.fAdhLam)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblAdhCofo = QtGui.QLabel(self.fAdhLam)
        self.lblAdhCofo.setObjectName(_fromUtf8("lblAdhCofo"))
        self.verticalLayout_5.addWidget(self.lblAdhCofo)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProveedorAdhCoFo = QtGui.QLabel(self.fAdhLam)
        self.lblProveedorAdhCoFo.setObjectName(_fromUtf8("lblProveedorAdhCoFo"))
        self.horizontalLayout.addWidget(self.lblProveedorAdhCoFo)
        self.leProveedorAdhCoFo = QtGui.QLineEdit(self.fAdhLam)
        self.leProveedorAdhCoFo.setObjectName(_fromUtf8("leProveedorAdhCoFo"))
        self.horizontalLayout.addWidget(self.leProveedorAdhCoFo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblAnchoAdhCoFo = QtGui.QLabel(self.fAdhLam)
        self.lblAnchoAdhCoFo.setObjectName(_fromUtf8("lblAnchoAdhCoFo"))
        self.horizontalLayout_2.addWidget(self.lblAnchoAdhCoFo)
        self.leAniloxAdhCoFo = QtGui.QLineEdit(self.fAdhLam)
        self.leAniloxAdhCoFo.setObjectName(_fromUtf8("leAniloxAdhCoFo"))
        self.horizontalLayout_2.addWidget(self.leAniloxAdhCoFo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbEditar = QtGui.QPushButton(self.fAdhLam)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_3.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.fAdhLam)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_3.addWidget(self.pbCancelar)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.fAdhLam, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblAdhCofo.setText(_translate("Dialog", "Adhesivo Cold Foil", None))
        self.lblProveedorAdhCoFo.setText(_translate("Dialog", "Proveedor", None))
        self.lblAnchoAdhCoFo.setText(_translate("Dialog", "Anilox", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

