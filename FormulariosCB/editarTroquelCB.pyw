from Formularios import editarTroquel
from PyQt4 import QtCore, QtGui
from Clases import DTO, DAO
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
class vEditarTroquel(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarTroquel.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.aceptado = False

        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
        self.editarTroquel = None

    def pbEditar_click(self):
        try:
            self.editarTroquel = DTO.Troquel()

            self.editarTroquel.setProveedor(self.ui.leProveedorTroquel.text())
            self.editarTroquel.setObservacion(self.ui.leObservacionesTroquel.text())

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.aceptado = True
            self.accept()
    def pbCancelar_click(self):
        self.reject()
