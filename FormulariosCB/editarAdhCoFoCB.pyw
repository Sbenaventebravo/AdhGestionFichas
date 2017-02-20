import sys
from PyQt4 import QtCore, QtGui
from Formularios import editarAdhCF
from Clases import DTO, DAO

def MostrarError(mensaje):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(mensaje)
    errorBox.exec_()
class vEditarAdhCoFo(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarAdhCF.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

        self.editarAdhCoFo = None
        self.aceptado = False
        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
    def pbEditar_click(self):
        try:
            self.editarAdhCoFo = DTO.AdhesivoColdFoil()
            self.editarAdhCoFo.setProveedor(self.ui.leProveedorAdhCoFo.text())
            self.editarAdhCoFo.setAnilox(self.ui.leProveedorAdhCoFo.text())
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.aceptado = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()
    pass