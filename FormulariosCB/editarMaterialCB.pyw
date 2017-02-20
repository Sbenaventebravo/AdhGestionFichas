from Formularios import editarMaterial
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
class vEditarMaterial(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarMaterial.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.aceptado = False

        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
        self.materialEditado = None

    def pbEditar_click(self):
        try:
            self.materialEditado = DTO.Material()
            TC = False
            if self.ui.rbTC1.isChecked():
                TC = True
            self.materialEditado.setCodigo(self.ui.leCodigoMaterial.text())
            self.materialEditado.setNombre(self.ui.leNombreMaterial.text())
            self.materialEditado.setProveedor(self.ui.leProveedorMaterial.text())
            self.materialEditado.setAncho(self.ui.dsbAnchoMaterial.value())
            self.materialEditado.setTC(TC)
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.aceptado = True
            self.accept()
    def pbCancelar_click(self):
        self.reject()
