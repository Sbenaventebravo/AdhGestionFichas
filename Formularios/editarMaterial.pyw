# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarMaterial.ui'
#
# Created: Tue Feb 14 10:23:24 2017
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
        Dialog.resize(432, 263)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 412, 243))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.lblMaterial = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblMaterial.setObjectName(_fromUtf8("lblMaterial"))
        self.verticalLayout_8.addWidget(self.lblMaterial)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.lblCodigoMaterial = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblCodigoMaterial.setObjectName(_fromUtf8("lblCodigoMaterial"))
        self.horizontalLayout_21.addWidget(self.lblCodigoMaterial)
        self.leCodigoMaterial = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leCodigoMaterial.setObjectName(_fromUtf8("leCodigoMaterial"))
        self.horizontalLayout_21.addWidget(self.leCodigoMaterial)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leNombreMaterial = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leNombreMaterial.setObjectName(_fromUtf8("leNombreMaterial"))
        self.horizontalLayout_2.addWidget(self.leNombreMaterial)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.lblProveedorMaterial = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblProveedorMaterial.setObjectName(_fromUtf8("lblProveedorMaterial"))
        self.horizontalLayout_22.addWidget(self.lblProveedorMaterial)
        self.leProveedorMaterial = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leProveedorMaterial.setObjectName(_fromUtf8("leProveedorMaterial"))
        self.horizontalLayout_22.addWidget(self.leProveedorMaterial)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.lblAncho = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblAncho.setObjectName(_fromUtf8("lblAncho"))
        self.horizontalLayout_23.addWidget(self.lblAncho)
        self.dsbAnchoMaterial = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents_2)
        self.dsbAnchoMaterial.setDecimals(2)
        self.dsbAnchoMaterial.setObjectName(_fromUtf8("dsbAnchoMaterial"))
        self.horizontalLayout_23.addWidget(self.dsbAnchoMaterial)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.gbTC = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbTC.setObjectName(_fromUtf8("gbTC"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout(self.gbTC)
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.rbTC1 = QtGui.QRadioButton(self.gbTC)
        self.rbTC1.setChecked(True)
        self.rbTC1.setObjectName(_fromUtf8("rbTC1"))
        self.horizontalLayout_25.addWidget(self.rbTC1)
        self.rbTC2 = QtGui.QRadioButton(self.gbTC)
        self.rbTC2.setObjectName(_fromUtf8("rbTC2"))
        self.horizontalLayout_25.addWidget(self.rbTC2)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)
        self.verticalLayout.addWidget(self.gbTC)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbEditar = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout.addWidget(self.pbCancelar)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblMaterial.setText(_translate("Dialog", "Material", None))
        self.lblCodigoMaterial.setText(_translate("Dialog", "Codigo", None))
        self.label.setText(_translate("Dialog", "Nombre", None))
        self.lblProveedorMaterial.setText(_translate("Dialog", "Proveedor", None))
        self.lblAncho.setText(_translate("Dialog", "Ancho(cm)", None))
        self.gbTC.setTitle(_translate("Dialog", "TC", None))
        self.rbTC1.setText(_translate("Dialog", "Si", None))
        self.rbTC2.setText(_translate("Dialog", "No", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

