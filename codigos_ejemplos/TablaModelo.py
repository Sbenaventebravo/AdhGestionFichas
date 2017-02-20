from PyQt4 import QtGui ,QtCore
from PyQt4 import QtSql
import sys
import Modelo
from Clases import DAO, DTO

def Conexion(db):
    db.setHostName("192.168.0.201")
    db.setDatabaseName("practica")
    db.setUserName("practica")
    db.setPassword("admin")
    if (db.open() == False):
        QtGui.QMessageBox.critical(None, "Database Error",
                                   db.lastError().text())

class vtablamodelo(QtGui.QDialog):
    def __init__(self, parent = None):
        "Constructor de la ventana de gestion de fichas"
        QtGui.QWidget.__init__(self,parent)
        self.ui = Modelo.Ui_Dialog()
        self.ui.setupUi(self)
        db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        Conexion(db)

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("material")

        self.model.setFilter("codigo  in {0}".format((426,439)))
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),self.insertRecords)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.UpdateRecords)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.deleteRecords)
        self.ui.tableView.hideColumn(0)
    def UpdateRecords(self):
        self.model.submitAll()
    def CancelChanges(self):
        self.model.revertAll()
    def insertRecords(self):
        self.model.insertRow(0)

    def deleteRecords(self):
        fila = []
        for col in range(self.model.columnCount()):
            index = self.model.index(self.ui.tableView.currentIndex().row(), col)
            fila.append(str(self.model.data(index).toString()))
        cat = DTO.Categoria()
        cat.setIdCategoria(fila[0])
        cat.setNombre(fila[1])
        DAO.Categoria(cat).eliminarCategoria()

        self.model.submitAll()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = vtablamodelo()
    myWindow.show()
    reload(sys)
    sys.setdefaultencoding('cp1252')
    print "a1".upper()
    sys.exit(app.exec_())
