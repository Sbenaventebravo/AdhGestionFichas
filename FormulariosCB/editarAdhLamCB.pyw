import sys
from Formularios import editarAdhLam
from PyQt4 import QtCore, QtGui
from Clases import DTO, DAO
def MostrarError(mensaje):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(mensaje)
    errorBox.exec_()

class vEditarAdhLam(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarAdhLam.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

        self.editarAdhLam = None
        self.aceptado = False
        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)

    def pbEditar_click(self):
        try:
            self.editarAdhLam = DTO.AdhesivoLaminacion()
            self.editarAdhLam.setProveedor(self.ui.leProveedorAdhLam.text())
            self.editarAdhLam.setAnilox(self.ui.leAniloxAdhLam.text())
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.aceptado = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()

    pass