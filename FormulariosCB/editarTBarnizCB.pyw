import sys
from PyQt4 import QtCore, QtGui
from Formularios import editarTipoBarniz
from Clases import DTO, DAO
def MostrarError(e):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(e.message.__str__())
    errorBox.exec_()
class vEditarTBarniz(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarTipoBarniz.Ui_Dialog()
        self.ui.setupUi(self)

        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

        self.editarTBarniz = None
        self.aceptado = False
        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)

    def pbEditar_click(self):
        try:
            self.editarTBarniz = DTO.TipoBarniz()
            self.editarTBarniz.setTipo(self.ui.leTipoTBarniz.text())
            self.editarTBarniz.setProveedor(self.ui.leProveedorTBarniz.text())
            self.editarTBarniz.setAnilox(self.ui.leAniloxTBarniz.text())
        except Exception as e:
            MostrarError(e)
        else:
            self.aceptado = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()

    pass