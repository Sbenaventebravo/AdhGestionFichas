# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarTipoBarniz.ui'
#
# Created: Fri Jan 13 13:51:50 2017
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
        Dialog.resize(400, 300)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.fAdhLam = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.fAdhLam.setEnabled(True)
        self.fAdhLam.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fAdhLam.setFrameShadow(QtGui.QFrame.Raised)
        self.fAdhLam.setObjectName(_fromUtf8("fAdhLam"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.fAdhLam)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblTBarniz = QtGui.QLabel(self.fAdhLam)
        self.lblTBarniz.setObjectName(_fromUtf8("lblTBarniz"))
        self.verticalLayout.addWidget(self.lblTBarniz)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblTipoTBarniz = QtGui.QLabel(self.fAdhLam)
        self.lblTipoTBarniz.setObjectName(_fromUtf8("lblTipoTBarniz"))
        self.horizontalLayout_5.addWidget(self.lblTipoTBarniz)
        self.leTipoTBarniz = QtGui.QLineEdit(self.fAdhLam)
        self.leTipoTBarniz.setObjectName(_fromUtf8("leTipoTBarniz"))
        self.horizontalLayout_5.addWidget(self.leTipoTBarniz)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProveedorTBarniz = QtGui.QLabel(self.fAdhLam)
        self.lblProveedorTBarniz.setObjectName(_fromUtf8("lblProveedorTBarniz"))
        self.horizontalLayout.addWidget(self.lblProveedorTBarniz)
        self.leProveedorTBarniz = QtGui.QLineEdit(self.fAdhLam)
        self.leProveedorTBarniz.setObjectName(_fromUtf8("leProveedorTBarniz"))
        self.horizontalLayout.addWidget(self.leProveedorTBarniz)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblAniloxTBarniz = QtGui.QLabel(self.fAdhLam)
        self.lblAniloxTBarniz.setObjectName(_fromUtf8("lblAniloxTBarniz"))
        self.horizontalLayout_2.addWidget(self.lblAniloxTBarniz)
        self.leAniloxTBarniz = QtGui.QLineEdit(self.fAdhLam)
        self.leAniloxTBarniz.setObjectName(_fromUtf8("leAniloxTBarniz"))
        self.horizontalLayout_2.addWidget(self.leAniloxTBarniz)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.pbEditar = QtGui.QPushButton(self.fAdhLam)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_18.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.fAdhLam)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_18.addWidget(self.pbCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19.addLayout(self.verticalLayout)
        self.verticalLayout_7.addWidget(self.fAdhLam)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblTBarniz.setText(_translate("Dialog", "Tipo de Barniz", None))
        self.lblTipoTBarniz.setText(_translate("Dialog", "Tipo", None))
        self.lblProveedorTBarniz.setText(_translate("Dialog", "Proveedor", None))
        self.lblAniloxTBarniz.setText(_translate("Dialog", "Anilox", None))
        self.pbEditar.setText(_translate("Dialog", "Editar ", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

