
# -*- coding: cp1252 -*-
import sys
from PyQt4 import QtCore, QtGui, QtSql
from Formularios import AdminClientes, editarCliente
from Clases import DAO, DTO
def MostrarError(mensaje):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(mensaje)
    errorBox.exec_()
def MostrarMensaje(mensaje):
    msjBox = QtGui.QMessageBox()
    msjBox.setWindowTitle("Mensaje")
    msjBox.setText(mensaje)
    msjBox.exec_()
class vEditarCliente(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarCliente.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setWindowTitle("Editar")

        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
        self.clienteEditado = None

    def pbEditar_click(self):
        try:
            self.clienteEditado = DTO.Cliente()
            self.clienteEditado.setRut(self.ui.leRut.text())
            self.clienteEditado.setNombre(self.ui.leNombre.text())

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.accept()
    def pbCancelar_click(self):
        self.reject()