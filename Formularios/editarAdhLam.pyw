# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarAdhLam.ui'
#
# Created: Fri Jan 13 13:48:32 2017
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
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 280))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fAdhLam = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.fAdhLam.setEnabled(True)
        self.fAdhLam.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fAdhLam.setFrameShadow(QtGui.QFrame.Raised)
        self.fAdhLam.setObjectName(_fromUtf8("fAdhLam"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.fAdhLam)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblAdhLam = QtGui.QLabel(self.fAdhLam)
        self.lblAdhLam.setObjectName(_fromUtf8("lblAdhLam"))
        self.verticalLayout_5.addWidget(self.lblAdhLam)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProveedorAdhLam = QtGui.QLabel(self.fAdhLam)
        self.lblProveedorAdhLam.setObjectName(_fromUtf8("lblProveedorAdhLam"))
        self.horizontalLayout.addWidget(self.lblProveedorAdhLam)
        self.leProveedorAdhLam = QtGui.QLineEdit(self.fAdhLam)
        self.leProveedorAdhLam.setObjectName(_fromUtf8("leProveedorAdhLam"))
        self.horizontalLayout.addWidget(self.leProveedorAdhLam)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblAniloxAdhLam = QtGui.QLabel(self.fAdhLam)
        self.lblAniloxAdhLam.setObjectName(_fromUtf8("lblAniloxAdhLam"))
        self.horizontalLayout_2.addWidget(self.lblAniloxAdhLam)
        self.leAniloxAdhLam = QtGui.QLineEdit(self.fAdhLam)
        self.leAniloxAdhLam.setObjectName(_fromUtf8("leAniloxAdhLam"))
        self.horizontalLayout_2.addWidget(self.leAniloxAdhLam)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pbEditar = QtGui.QPushButton(self.fAdhLam)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_5.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.fAdhLam)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_5.addWidget(self.pbCancelar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.fAdhLam)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblAdhLam.setText(_translate("Dialog", "Adhesivo Laminacion", None))
        self.lblProveedorAdhLam.setText(_translate("Dialog", "Proveedor", None))
        self.lblAniloxAdhLam.setText(_translate("Dialog", "Anilox", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

