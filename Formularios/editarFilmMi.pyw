# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarFilmMi.ui'
#
# Created: Tue Feb 14 10:20:36 2017
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
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.fAdhLam)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblFilmMi = QtGui.QLabel(self.fAdhLam)
        self.lblFilmMi.setObjectName(_fromUtf8("lblFilmMi"))
        self.verticalLayout_5.addWidget(self.lblFilmMi)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProveedorFilmMi = QtGui.QLabel(self.fAdhLam)
        self.lblProveedorFilmMi.setObjectName(_fromUtf8("lblProveedorFilmMi"))
        self.horizontalLayout.addWidget(self.lblProveedorFilmMi)
        self.leProveedorFilmMi = QtGui.QLineEdit(self.fAdhLam)
        self.leProveedorFilmMi.setObjectName(_fromUtf8("leProveedorFilmMi"))
        self.horizontalLayout.addWidget(self.leProveedorFilmMi)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblAnchoFilmMi = QtGui.QLabel(self.fAdhLam)
        self.lblAnchoFilmMi.setObjectName(_fromUtf8("lblAnchoFilmMi"))
        self.horizontalLayout_2.addWidget(self.lblAnchoFilmMi)
        self.dsbAnchoFilmMi = QtGui.QDoubleSpinBox(self.fAdhLam)
        self.dsbAnchoFilmMi.setDecimals(2)
        self.dsbAnchoFilmMi.setObjectName(_fromUtf8("dsbAnchoFilmMi"))
        self.horizontalLayout_2.addWidget(self.dsbAnchoFilmMi)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbEditar = QtGui.QPushButton(self.fAdhLam)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout_3.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.fAdhLam)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout_3.addWidget(self.pbCancelar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.fAdhLam)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblFilmMi.setText(_translate("Dialog", "Film Micronaje", None))
        self.lblProveedorFilmMi.setText(_translate("Dialog", "Proveedor", None))
        self.lblAnchoFilmMi.setText(_translate("Dialog", "Ancho", None))
        self.pbEditar.setText(_translate("Dialog", "Editar ", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

