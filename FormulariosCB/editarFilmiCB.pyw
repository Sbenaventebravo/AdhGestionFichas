import sys
from PyQt4 import QtCore, QtGui
from Formularios import editarFilmMi
from Clases import DTO, DAO
def MostrarError(e):
    errorBox = QtGui.QMessageBox()
    errorBox.setWindowTitle("Error")
    errorBox.setText(e.message.__str__())
    errorBox.exec_()
class vEditarFilmMi(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = editarFilmMi.Ui_Dialog()
        self.ui.setupUi(self)

        flags = QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.aceptar = False

        self.editarFilmMi = None
        QtCore.QObject.connect(self.ui.pbEditar, QtCore.SIGNAL("clicked()"), self.pbEditar_click)
        QtCore.QObject.connect(self.ui.pbCancelar, QtCore.SIGNAL("clicked()"), self.pbCancelar_click)
    def pbEditar_click(self):
        try:
            self.editarFilmMi = DTO.FilmMicronaje()
            self.editarFilmMi.setProveedor(self.ui.leProveedorFilmMi.text())
            self.editarFilmMi.setAncho(self.ui.dsbAnchoFilmMi.value())
        except Exception as e:
            MostrarError(e)
        else:
            self.aceptar = True
            self.accept()

    def pbCancelar_click(self):
        self.reject()

    pass
