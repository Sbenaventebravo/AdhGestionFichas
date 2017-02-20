import sys
from PyQt4 import QtCore, QtGui
from Formularios import editarMalla
from Clases import DTO, DAO

def MostrarError(mensaje):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(mensaje)
    errorBox.exec_()
class vEditarMalla(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarMalla.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
        self.mallaEditada = None
        self.aceptado = False

    def pbEditar_click(self):
        try:
            interno = False
            if self.ui.rbInterno.isChecked():
                interno = True
            self.mallaEditada = DTO.Malla()
            self.mallaEditada.setTipo(self.ui.leTipoMalla.text())
            self.mallaEditada.setInterno(interno)
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.aceptado = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()