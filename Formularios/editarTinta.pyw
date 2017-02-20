# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarTinta.ui'
#
# Created: Mon Jan 16 17:06:41 2017
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
        Dialog.resize(455, 292)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 435, 272))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.lblTinta = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblTinta.setObjectName(_fromUtf8("lblTinta"))
        self.verticalLayout_19.addWidget(self.lblTinta)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_43 = QtGui.QHBoxLayout()
        self.horizontalLayout_43.setObjectName(_fromUtf8("horizontalLayout_43"))
        self.lblColor = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblColor.setObjectName(_fromUtf8("lblColor"))
        self.horizontalLayout_43.addWidget(self.lblColor)
        self.leColorTinta = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leColorTinta.setObjectName(_fromUtf8("leColorTinta"))
        self.horizontalLayout_43.addWidget(self.leColorTinta)
        self.verticalLayout_4.addLayout(self.horizontalLayout_43)
        self.horizontalLayout_44 = QtGui.QHBoxLayout()
        self.horizontalLayout_44.setObjectName(_fromUtf8("horizontalLayout_44"))
        self.lblTipoTinta = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblTipoTinta.setObjectName(_fromUtf8("lblTipoTinta"))
        self.horizontalLayout_44.addWidget(self.lblTipoTinta)
        self.leTipoTinta = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leTipoTinta.setObjectName(_fromUtf8("leTipoTinta"))
        self.horizontalLayout_44.addWidget(self.leTipoTinta)
        self.verticalLayout_4.addLayout(self.horizontalLayout_44)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_45 = QtGui.QHBoxLayout()
        self.horizontalLayout_45.setObjectName(_fromUtf8("horizontalLayout_45"))
        self.lblAniloxTinta = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblAniloxTinta.setObjectName(_fromUtf8("lblAniloxTinta"))
        self.horizontalLayout_45.addWidget(self.lblAniloxTinta)
        self.leAniloxTinta = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leAniloxTinta.setObjectName(_fromUtf8("leAniloxTinta"))
        self.horizontalLayout_45.addWidget(self.leAniloxTinta)
        self.verticalLayout_3.addLayout(self.horizontalLayout_45)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_46 = QtGui.QHBoxLayout()
        self.horizontalLayout_46.setObjectName(_fromUtf8("horizontalLayout_46"))
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_47 = QtGui.QHBoxLayout()
        self.horizontalLayout_47.setObjectName(_fromUtf8("horizontalLayout_47"))
        self.lblProveedor = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblProveedor.setObjectName(_fromUtf8("lblProveedor"))
        self.horizontalLayout_47.addWidget(self.lblProveedor)
        self.leProveedorTinta = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leProveedorTinta.setObjectName(_fromUtf8("leProveedorTinta"))
        self.horizontalLayout_47.addWidget(self.leProveedorTinta)
        self.verticalLayout_21.addLayout(self.horizontalLayout_47)
        self.horizontalLayout_48 = QtGui.QHBoxLayout()
        self.horizontalLayout_48.setObjectName(_fromUtf8("horizontalLayout_48"))
        self.lblProveedor_2 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblProveedor_2.setObjectName(_fromUtf8("lblProveedor_2"))
        self.horizontalLayout_48.addWidget(self.lblProveedor_2)
        self.leProveedorTinta2 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leProveedorTinta2.setObjectName(_fromUtf8("leProveedorTinta2"))
        self.horizontalLayout_48.addWidget(self.leProveedorTinta2)
        self.verticalLayout_21.addLayout(self.horizontalLayout_48)
        self.horizontalLayout_49 = QtGui.QHBoxLayout()
        self.horizontalLayout_49.setObjectName(_fromUtf8("horizontalLayout_49"))
        self.lblProveedor3 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.lblProveedor3.setObjectName(_fromUtf8("lblProveedor3"))
        self.horizontalLayout_49.addWidget(self.lblProveedor3)
        self.leProveedorTinta3 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.leProveedorTinta3.setObjectName(_fromUtf8("leProveedorTinta3"))
        self.horizontalLayout_49.addWidget(self.leProveedorTinta3)
        self.verticalLayout_21.addLayout(self.horizontalLayout_49)
        self.horizontalLayout_46.addLayout(self.verticalLayout_21)
        self.verticalLayout_4.addLayout(self.horizontalLayout_46)
        self.verticalLayout_19.addLayout(self.verticalLayout_4)
        self.horizontalLayout_50 = QtGui.QHBoxLayout()
        self.horizontalLayout_50.setObjectName(_fromUtf8("horizontalLayout_50"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbEditar = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pbEditar.setObjectName(_fromUtf8("pbEditar"))
        self.horizontalLayout.addWidget(self.pbEditar)
        self.pbCancelar = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pbCancelar.setObjectName(_fromUtf8("pbCancelar"))
        self.horizontalLayout.addWidget(self.pbCancelar)
        self.horizontalLayout_50.addLayout(self.horizontalLayout)
        self.verticalLayout_19.addLayout(self.horizontalLayout_50)
        self.verticalLayout_2.addLayout(self.verticalLayout_19)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblTinta.setText(_translate("Dialog", "Tinta", None))
        self.lblColor.setText(_translate("Dialog", "Color", None))
        self.lblTipoTinta.setText(_translate("Dialog", "Tipo", None))
        self.lblAniloxTinta.setText(_translate("Dialog", "Anilox", None))
        self.lblProveedor.setText(_translate("Dialog", "Proveedor ", None))
        self.lblProveedor_2.setText(_translate("Dialog", "Proveedor 2", None))
        self.lblProveedor3.setText(_translate("Dialog", "Proveedor  3", None))
        self.pbEditar.setText(_translate("Dialog", "Editar", None))
        self.pbCancelar.setText(_translate("Dialog", "Cancelar", None))

