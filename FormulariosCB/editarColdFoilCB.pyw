import sys
from PyQt4 import QtCore, QtGui
from Formularios import editarColdFoil
from Clases import DTO, DAO

"Muestar el error pertinente"


def MostrarError(e):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(e.message.__str__())
    errorBox.exec_()

class vEditarColdFoil(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarColdFoil.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.aceptado = False
        self.editarColdFoil = None

        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)

    def pbEditar_click(self):
        try:
            self.editarColdFoil = DTO.ColdFoil()
            self.editarColdFoil.setProveedor(self.ui.leProveedorColdFoil.text())
            self.editarColdFoil.setAncho(self.ui.dsbAnchoColdFoil.value())
            self.editarColdFoil.setTipo(self.ui.rbCF.isChecked())
        except Exception as e:
            MostrarError(e)
        else:
            self.aceptado = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()

    pass