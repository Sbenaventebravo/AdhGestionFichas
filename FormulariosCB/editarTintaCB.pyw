import sys
from PyQt4 import QtCore, QtGui
from Formularios import editarTinta
from Clases import DTO, DAO
def MostrarError(mensaje):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(mensaje)
    errorBox.exec_()
class vEditarTinta(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarTinta.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
        self.tintaEditada = None
        self.aceptado = False

    def pbEditar_click(self):
        try:
            self.tintaEditada = DTO.Tinta()
            self.tintaEditada.setColor(self.ui.leColorTinta.text())
            self.tintaEditada.setTipo(self.ui.leTipoTinta.text())
            self.tintaEditada.setAnilox(self.ui.leAniloxTinta.text())
            self.tintaEditada.setProveedor1(self.ui.leProveedorTinta.text())
            self.tintaEditada.setProveedor2(self.ui.leProveedorTinta2.text())
            self.tintaEditada.setProveedor3(self.ui.leProveedorTinta3.text())
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.aceptado = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()