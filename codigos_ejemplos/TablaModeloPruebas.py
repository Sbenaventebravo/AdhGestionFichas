from PyQt4 import QtGui ,QtCore
from PyQt4 import QtSql
import sys
import Modelo, PruebasModelosDeTablas
import vEditarMaterial, editarTinta, editarMalla, editarAdhLam,editarAdhCoFo
import editarFilmi, editarColdFoil, editarTBarniz, editarTroquel
from Clases import DAO, DTO
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
        self.ui = PruebasModelosDeTablas.Ui_Dialog()
        self.ui.setupUi(self)
        db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        Conexion(db)
        self.edicion = 23
        self.cargarviewmateriales()
        self.cargarviewtintas()
        self.cargarviewmallas()
        self.cargarviewadhlam()
        self.cargarviewadhcofo()
        self.cargarviewfilmmi()
        self.cargarviewcoldfoil()
        self.cargarviewtbarniz()
        self.cargarviewtroquel()

        "Conexion de botones con metodos de Crud de Materiales"
        QtCore.QObject.connect(self.ui.pbAniadirMaterialMod, QtCore.SIGNAL("clicked()"), self.insertRecordsMateriales)
        QtCore.QObject.connect(self.ui.pbEditarMaterialMod, QtCore.SIGNAL("clicked()"), self.updateRecordsMateriales)
        QtCore.QObject.connect(self.ui.pbBorrarMaterialMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsMateriales)

        "Conexion de botones con metodos de Crud de Tintas"
        QtCore.QObject.connect(self.ui.pbAniadirTintaMod, QtCore.SIGNAL("clicked()"), self.insertRecordsTintas)
        QtCore.QObject.connect(self.ui.pbEditarTintaMod, QtCore.SIGNAL("clicked()"), self.updateRecordsTintas)
        QtCore.QObject.connect(self.ui.pbBorrarTintaMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsTintas)

        "Conexion de botones con metodos de Crud de Mallas"
        QtCore.QObject.connect(self.ui.pbAniadirMallaMod, QtCore.SIGNAL("clicked()"), self.insertRecordsMallas)
        QtCore.QObject.connect(self.ui.pbEditarMallaMod, QtCore.SIGNAL("clicked()"), self.updateRecordsMallas)
        QtCore.QObject.connect(self.ui.pbBorrarMallaMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsMallas)

        "Conexion de botones con metodos de Crud de Adhesivos Laminacion"
        QtCore.QObject.connect(self.ui.pbAniadirAdhLamMod, QtCore.SIGNAL("clicked()"), self.insertRecordsAdhlam)
        QtCore.QObject.connect(self.ui.pbEditarAdhLamMod, QtCore.SIGNAL("clicked()"), self.updateRecordsAdhlam)
        QtCore.QObject.connect(self.ui.pbBorrarAdhLamMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsAdhlam)

        "Conexion de botones con metodos de Crud de Adhesivos Cold Foil"
        QtCore.QObject.connect(self.ui.pbAniadirAdhCoFoMod, QtCore.SIGNAL("clicked()"), self.insertRecordsdhcofo)
        QtCore.QObject.connect(self.ui.pbEditarAdhCoFoMod, QtCore.SIGNAL("clicked()"), self.updateRecordsdhcofo)
        QtCore.QObject.connect(self.ui.pbBorrarAdhCoFoMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsdhcofo)

        "Conexion de botones con metodos de Crud de Film Micronaje"
        QtCore.QObject.connect(self.ui.pbAniadirFilmMiMod, QtCore.SIGNAL("clicked()"), self.insertRecordsfilmmi)
        QtCore.QObject.connect(self.ui.pbEditarFilmMiMod, QtCore.SIGNAL("clicked()"), self.updateRecordsfilmmi)
        QtCore.QObject.connect(self.ui.pbBorrarFilmMiMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsfilmmi)

        "Conexion de botones con metodos de Crud de Cold Foil"
        QtCore.QObject.connect(self.ui.pbAniadirColdFoilMod, QtCore.SIGNAL("clicked()"), self.insertRecordscoldfoil)
        QtCore.QObject.connect(self.ui.pbEditarColdFoilMod, QtCore.SIGNAL("clicked()"), self.updateRecordscoldfoil)
        QtCore.QObject.connect(self.ui.pbBorrarColdFoilMod, QtCore.SIGNAL("clicked()"), self.deleteRecordscoldfoil)

        "Conexion de botones con metodos de Crud de Tipos de Barniz"
        QtCore.QObject.connect(self.ui.pbAniadirTBarnizMod, QtCore.SIGNAL("clicked()"), self.insertRecordsTBarniz)
        QtCore.QObject.connect(self.ui.pbEditarTBarnizMod, QtCore.SIGNAL("clicked()"), self.updateRecordsTBarniz)
        QtCore.QObject.connect(self.ui.pbBorrarTBarnizMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsTBarniz)

        "Conexion de botones con metodos de Crud de Troquel"
        QtCore.QObject.connect(self.ui.pbAniadirTroquelMod, QtCore.SIGNAL("clicked()"), self.insertRecordsTroquel)
        QtCore.QObject.connect(self.ui.pbEditarTroquelMod, QtCore.SIGNAL("clicked()"), self.updateRecordsTroquel)
        QtCore.QObject.connect(self.ui.pbBorrarTroquelMod, QtCore.SIGNAL("clicked()"), self.deleteRecordsTroquel)


    def cadenadereferencias(self, listaref):
        string = "("
        for index in listaref:
            string += str(index) + ","
            pass
        string = list(string)
        string[-1] = ")"
        string = "".join(string)
        return string
    "Metodos Para crud de materiales"
    def cargarviewmateriales(self):
        self.modelMaterial = QtSql.QSqlTableModel(self)
        self.modelMaterial.setTable("material")
        listaref = self.cadenadereferencias(DAO.MaterialFicha().leerMaterialesEnFicha(self.edicion))
        self.modelMaterial.setFilter("idMaterial  in {0}".format(listaref))
        self.modelMaterial.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelMaterial.select()
        self.ui.viewMateriales.setModel(self.modelMaterial)
        self.ui.viewMateriales.hideColumn(0)
        "Se modifica la presentacion de la informacion para que se entendible"
        for row in range(self.modelMaterial.rowCount()):
            index = self.modelMaterial.index(row, 5)
            estado = self.modelMaterial.data(index).toBool()
            if estado == True:
                self.ui.viewMateriales.model().setData(index, "SI")
            else:
                self.ui.viewMateriales.model().setData(index, "NO")
            pass

    def insertRecordsMateriales(self):
        try:
            mat = DTO.Material()
            mat.setCodigo(self.ui.leCodigoMaterialMod.text())
            mat.setNombre(self.ui.leNombreMaterialMod.text())
            mat.setProveedor(self.ui.leProveedorMaterialMod.text())
            mat.setAncho(self.ui.dsbAnchoMaterialMod.value())
            if self.ui.rbConvencionalesMod.isChecked():

                mat.setTC(True)
            else:
                mat.setTC(False)
            DAO.Material(mat).insertarMaterial()
            "crear referencia de forma inmediata"
            mf = DAO.MaterialFicha()
            mf.setIdFicha(self.edicion)
            mf.setIdMaterial(DAO.Material().idUltimoMaterialInsertada())
            mf.insertarMaterialFicha()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.cargarviewmateriales()
    def deleteRecordsMateriales(self):
        fila = []
        for col in range(self.modelMaterial.columnCount()):
            index = self.modelMaterial.index(self.ui.viewMateriales.currentIndex().row(), col)
            fila.append(str(self.modelMaterial.data(index).toString()))
        mat = DTO.Material()
        mat.setIdMaterial(fila[0])
        DAO.MaterialFicha().eliminarreferencia(fila[0], self.edicion)
        DAO.Material(mat).eliminarMaterial()

        self.cargarviewmateriales()
    def updateRecordsMateriales(self):
        try:
            fila = []
            for col in range(self.modelMaterial.columnCount()):
                index = self.modelMaterial.index(self.ui.viewMateriales.currentIndex().row(), col)
                fila.append(str(self.modelMaterial.data(index).toString()))

            mat = DTO.Material()
            mat.setIdMaterial(fila[0])
            mat.setCodigo(str(fila[1]))
            mat.setNombre(str(fila[2]))
            mat.setProveedor(str(fila[3]))
            mat.setAncho(float(fila[4]))
            mat.setTC(bool(fila[5]))

            dialog = vEditarMaterial.vEditarMaterial()
            dialog.ui.leCodigoMaterial.setText(mat.getCodigo())
            dialog.ui.leNombreMaterial.setText(mat.getNombre())
            dialog.ui.leProveedorMaterial.setText(mat.getProveedor())
            dialog.ui.dsbAnchoMaterial.setValue(mat.getAncho())
            if mat.getTC() is True:
                dialog.ui.rbTC1.setChecked(True)

            else:
                dialog.ui.rbTC2.setChecked(True)
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.materialEditado is not None:
                if(dialog.aceptado):

                    mat.setCodigo(dialog.materialEditado.getCodigo())
                    mat.setNombre(dialog.materialEditado.getNombre())
                    mat.setProveedor(dialog.materialEditado.getProveedor())
                    mat.setAncho(dialog.materialEditado.getAncho())
                    mat.setTC(dialog.materialEditado.getTC())
                    DAO.Material(mat).modificarMaterial()
                    self.cargarviewmateriales()
        pass
    "Metodos para crud de tintas"
    def cargarviewtintas(self):
        self.modelTinta = QtSql.QSqlTableModel(self)
        self.modelTinta.setTable("tinta")
        listaref = self.cadenadereferencias(DAO.TintaFicha().leerTintaEnFicha(self.edicion))
        self.modelTinta.setFilter("idTinta  in {0}".format(listaref))
        self.modelTinta.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelTinta.select()
        self.ui.viewTintas.setModel(self.modelTinta)
        self.ui.viewTintas.hideColumn(0)
        pass
    def insertRecordsTintas(self):
        try:
            tin = DTO.Tinta()
            tin.setColor(self.ui.leColorTintaMod.text())
            tin.setTipo(self.ui.leTipoTintaMod.text())
            tin.setAnilox(self.ui.leAniloxTintaMod.text())
            tin.setProveedor1(self.ui.leProveedorTintaMod.text())
            tin.setProveedor2(self.ui.leProveedorTinta2Mod.text())
            tin.setProveedor3(self.ui.leProveedorTinta3Mod.text())

            DAO.Tinta(tin).ingresarTinta()
            "crear referencia de forma inmediata"
            tf = DAO.TintaFicha()
            tf.setIdFicha(self.edicion)
            tf.setIdTinta(DAO.Tinta().idUltimaTinta())
            tf.insertarTintaFicha()
            self.cargarviewtintas()
            ""
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modelTinta.submitAll()
            "limpiarFormulario"
    def deleteRecordsTintas(self):
        try:
            fila = []
            for col in range(self.modelTinta.columnCount()):
                index = self.modelTinta.index(self.ui.viewTintas.currentIndex().row(), col)
                fila.append(str(self.modelTinta.data(index).toString()))
            tin = DTO.Tinta()
            tin.setIdTinta(fila[0])
            DAO.TintaFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.Tinta(tin).eliminarTinta()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modelTinta.submitAll()
    def updateRecordsTintas(self):
        try:
            fila = []
            for col in range(self.modelTinta.columnCount()):
                index = self.modelTinta.index(self.ui.viewTintas.currentIndex().row(), col)
                fila.append(str(self.modelTinta.data(index).toString()))

            tin = DTO.Tinta()
            tin.setIdTinta(fila[0])
            tin.setColor(str(fila[1]))
            tin.setTipo(str(fila[2]))
            tin.setAnilox(str(fila[3]))
            tin.setProveedor1(str(fila[4]))
            tin.setProveedor2(str(fila[5]))
            tin.setProveedor3(str(fila[6]))

            dialog = editarTinta.vEditarTinta()
            dialog.ui.leColorTinta.setText(tin.getColor())
            dialog.ui.leTipoTinta.setText(tin.getTipo())
            dialog.ui.leAniloxTinta.setText(tin.getAnilox())
            dialog.ui.leProveedorTinta.setText(tin.getProveedor1())
            dialog.ui.leProveedorTinta2.setText(tin.getProveedor2())
            dialog.ui.leProveedorTinta3.setText(tin.getProveedor3())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.tintaEditada is not None:
                if (dialog.aceptado):
                    tin.setColor(dialog.ui.leColorTinta.text())
                    tin.setTipo(dialog.ui.leTipoTinta.text())
                    tin.setAnilox(dialog.ui.leAniloxTinta.text())
                    tin.setProveedor1(dialog.ui.leProveedorTinta.text())
                    tin.setProveedor2(dialog.ui.leProveedorTinta2.text())
                    tin.setProveedor3(dialog.ui.leProveedorTinta3.text())
                    DAO.Tinta(tin).modificarTinta()
                    self.modelTinta.submitAll()
        pass

    "Metodos para el crud de mallas"
    def cargarviewmallas(self):
        self.modelMallas = QtSql.QSqlTableModel(self)
        self.modelMallas.setTable("malla")
        self.modelMallas.setHeaderData(2, QtCore.Qt.Horizontal,
                                 'Interna/Externa')
        listaref = self.cadenadereferencias(DAO.MallaFicha().leerMallaEnFicha(self.edicion))


        self.modelMallas.setFilter("idMalla  in {0}".format(listaref))
        self.modelMallas.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelMallas.select()
        self.ui.viewMalla.setModel(self.modelMallas)

        self.ui.viewMalla.hideColumn(0)
        "Se modifica la presentacion de la informacion para que se entendible"
        for row in range(self.modelMallas.rowCount()):
            index = self.modelMallas.index(row, 2)
            estado = self.modelMallas.data(index).toBool()
            if estado == True:
                self.ui.viewMalla.model().setData(index, "INTERNA")
            else:
                self.ui.viewMalla.model().setData(index, "EXTERNA")
            pass
    def insertRecordsMallas(self):
        try:
            mal = DTO.Malla()
            mal.setTipo(self.ui.leTipoMallaMod.text())
            if self.ui.rbInterno_2.isChecked():

                mal.setInterno(True)
            else:
                mal.setInterno(False)
            DAO.Malla(mal).ingresarMalla()
            "crear referencia de forma inmediata"
            mf = DAO.MallaFicha()
            mf.setIdFicha(self.edicion)
            mf.setIdMalla(DAO.Malla().idUltimaMallaInsertada())
            mf.insertarMallaFicha()
            self.cargarviewmallas()


        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.cargarviewmallas()
            pass
    def deleteRecordsMallas(self):
        try:
            fila = []
            for col in range(self.modelMallas.columnCount()):
                index = self.modelMallas.index(self.ui.viewMalla.currentIndex().row(), col)
                fila.append(str(self.modelMallas.data(index).toString()))
            mal = DTO.Malla()
            mal.setIdMalla(fila[0])
            DAO.MallaFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.Tinta(mal).eliminarTinta()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.cargarviewmallas()
            pass
    def updateRecordsMallas(self):
        try:
            fila = []
            for col in range(self.modelMallas.columnCount()):
                index = self.modelMallas.index(self.ui.viewMalla.currentIndex().row(), col)
                fila.append(str(self.modelMallas.data(index).toString()))

            mal = DTO.Malla()
            mal.setIdMalla(fila[0])
            mal.setTipo(str(fila[1]))
            mal.setInterno(bool(fila[2]))

            dialog = editarMalla.vEditarMalla()
            dialog.ui.leTipoMalla.setText(mal.getTipo())
            dialog.ui.rbInterno.setChecked(False)
            if mal.getInterno():
                dialog.ui.rbInterno.setChecked(True)
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.mallaEditada is not None:
                if (dialog.aceptado):
                    mal.setTipo(dialog.ui.leTipoMalla.text())
                    mal.setInterno(dialog.ui.rbInterno.isChecked())
                    DAO.Malla(mal).modificarMalla()
                    self.cargarviewmallas()


    "metodos para el crud de adhesivos de laminacion"
    def cargarviewadhlam(self):
        self.modeladhlam = QtSql.QSqlTableModel(self)
        self.modeladhlam.setTable("adhesivo_laminacion")
        listaref = self.cadenadereferencias(DAO.AdhLamFicha().leerAdhLamFicha(self.edicion))
        self.modeladhlam.setFilter("idAdhLam  in {0}".format(listaref))
        self.modeladhlam.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeladhlam.select()
        self.ui.viewAdhLam.setModel(self.modeladhlam)
        self.ui.viewAdhLam.hideColumn(0)
        pass
    def insertRecordsAdhlam(self):
        try:
            adhlam = DTO.AdhesivoLaminacion()
            adhlam.setProveedor(self.ui.leProveedorAdhLamMod.text())
            adhlam.setAnilox(self.ui.leAniloxAdhLamMod.text())

            DAO.AdhesivoLaminacion(adhlam).ingresarAdhLam()
            "crear referencia de forma inmediata"
            alf = DAO.AdhLamFicha()
            alf.setIdFicha(self.edicion)
            alf.setIdAdhLam(DAO.AdhesivoLaminacion().idUltimoAdhLam())
            alf.insertarAdhLamFicha()
            self.cargarviewadhlam()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modeladhlam.submitAll()
    def deleteRecordsAdhlam(self):
        try:
            fila = []
            for col in range(self.modeladhlam.columnCount()):
                index = self.modeladhlam.index(self.ui.viewAdhLam.currentIndex().row(), col)
                fila.append(str(self.modeladhlam.data(index).toString()))
            alf = DTO.AdhesivoLaminacion()
            alf.setIdAdhLam(fila[0])
            DAO.AdhLamFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.AdhesivoLaminacion(alf).eliminarAdhLam()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modeladhlam.submitAll()
    def updateRecordsAdhlam(self):
        try:
            fila = []
            for col in range(self.modeladhlam.columnCount()):
                index = self.modeladhlam.index(self.ui.viewAdhLam.currentIndex().row(), col)
                fila.append(str(self.modeladhlam.data(index).toString()))

            adhlam = DTO.AdhesivoLaminacion()
            adhlam.setIdAdhLam(fila[0])
            adhlam.setProveedor(str(fila[1]))
            adhlam.setAnilox(str(fila[2]))

            dialog = editarAdhLam.vEditarAdhLam()
            dialog.ui.leProveedorAdhLam.setText(adhlam.getProveedor())
            dialog.ui.leAniloxAdhLam.setText(adhlam.getAnilox())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarAdhLam is not None:
                if (dialog.aceptado):
                    adhlam.setProveedor(dialog.ui.leProveedorAdhLam.text())
                    adhlam.setAnilox(dialog.ui.leAniloxAdhLam.text())
                    DAO.AdhesivoLaminacion(adhlam).modificarAdhLam()
                    self.cargarviewadhlam()


    "metodos para el crud de adhesivo cold foil"
    def cargarviewadhcofo(self):
        self.modeladhcofo = QtSql.QSqlTableModel(self)
        self.modeladhcofo.setTable("adhesivo_coldfoil")
        listaref = self.cadenadereferencias(DAO.AdhCoFoFicha().leerAdhCoFoEnFicha(self.edicion))
        self.modeladhcofo.setFilter("idAdhColdFoil  in {0}".format(listaref))
        self.modeladhcofo.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeladhcofo.select()
        self.ui.viewAdhCofo.setModel(self.modeladhcofo)
        self.ui.viewAdhCofo.hideColumn(0)
    def insertRecordsdhcofo(self):
        try:
            adhcofo = DTO.AdhesivoColdFoil()
            adhcofo.setProveedor(self.ui.leProveedorAdhCoFoMod.text())
            adhcofo.setAncho(self.ui.dsbAnchoAdhCoFoMod.value())

            DAO.AdhesivoColdFoil(adhcofo).ingresarAdhCoFo()
            "crear referencia de forma inmediata"
            acf = DAO.AdhCoFoFicha()
            acf.setIdFicha(self.edicion)
            acf.setIdAdhCoFo(DAO.AdhesivoColdFoil().idUltimoAdhCoFo())
            acf.insertarAdhCoFoFicha()
            self.cargarviewadhcofo()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modeladhcofo.submitAll()
    def deleteRecordsdhcofo(self):
        try:
            fila = []
            for col in range(self.modeladhcofo.columnCount()):
                index = self.modeladhcofo.index(self.ui.viewAdhCofo.currentIndex().row(), col)
                fila.append(str(self.modeladhcofo.data(index).toString()))
            acf = DTO.AdhesivoColdFoil()
            acf.setIdAdhCoFo(fila[0])
            DAO.AdhCoFoFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.AdhesivoColdFoil(acf).eliminarAdhCoFo()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modeladhcofo.submitAll()
    def updateRecordsdhcofo(self):
        try:
            fila = []
            for col in range(self.modeladhcofo.columnCount()):
                index = self.modeladhcofo.index(self.ui.viewAdhCofo.currentIndex().row(), col)
                fila.append(str(self.modeladhcofo.data(index).toString()))

            adhcofo = DTO.AdhesivoColdFoil()
            adhcofo.setIdAdhCoFo(fila[0])
            adhcofo.setProveedor(str(fila[1]))
            adhcofo.setAncho(float(fila[2]))

            dialog = editarAdhCoFo.vEditarAdhCoFo()
            dialog.ui.leProveedorAdhCoFo.setText(adhcofo.getProveedor())
            dialog.ui.dsbAnchoAdhCoFo.setValue(adhcofo.getAncho())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarAdhCoFo is not None:
                if (dialog.aceptado):
                    adhcofo.setProveedor(dialog.ui.leProveedorAdhCoFo.text())
                    adhcofo.setAncho(dialog.ui.dsbAnchoAdhCoFo.value())
                    DAO.AdhesivoColdFoil(adhcofo).modificarAdhCoFo()
                    self.cargarviewadhcofo()

    "metodos para el crud de film micronaje"
    def cargarviewfilmmi(self):
        self.modelfilmi = QtSql.QSqlTableModel(self)
        self.modelfilmi.setTable("film_micronaje")
        listaref = self.cadenadereferencias(DAO.FilmMiFicha().leerFilmMiEnFicha(self.edicion))
        self.modelfilmi.setFilter("idFilmMi  in {0}".format(listaref))
        self.modelfilmi.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelfilmi.select()
        self.ui.viewFilmmi.setModel(self.modelfilmi)
        self.ui.viewFilmmi.hideColumn(0)
        pass
    def insertRecordsfilmmi(self):
        try:
            filmi = DTO.FilmMicronaje()
            filmi.setProveedor(self.ui.leProveedorFilmMiMod.text())
            filmi.setAncho(self.ui.dsbAnchoFilmMiMod.value())

            DAO.FilmMicronaje(filmi).ingresarFilmMi()
            "crear referencia de forma inmediata"
            ff = DAO.FilmMiFicha()
            ff.setIdFicha(self.edicion)
            ff.setIdFilmMi(DAO.FilmMicronaje().idUltimoFilmMi())
            ff.insertarFilmMiFicha()
            self.cargarviewfilmmi()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modelfilmi.submitAll()
    def deleteRecordsfilmmi(self):
        try:
            fila = []
            for col in range(self.modelfilmi.columnCount()):
                index = self.modelfilmi.index(self.ui.viewFilmmi.currentIndex().row(), col)
                fila.append(str(self.modelfilmi.data(index).toString()))
            filmi = DTO.FilmMicronaje()
            filmi.setIdFilmMi(fila[0])
            DAO.FilmMiFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.FilmMicronaje(filmi).eliminarFilmMi()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modelfilmi.submitAll()
    def updateRecordsfilmmi(self):
        try:
            fila = []
            for col in range(self.modelfilmi.columnCount()):
                index = self.modelfilmi.index(self.ui.viewFilmmi.currentIndex().row(), col)
                fila.append(str(self.modelfilmi.data(index).toString()))

            filmi = DTO.FilmMicronaje()
            filmi.setIdFilmMi(fila[0])
            filmi.setProveedor(str(fila[1]))
            filmi.setAncho(float(fila[2]))

            dialog = editarFilmi.vEditarFilmMi()
            dialog.ui.leProveedorFilmMi.setText(filmi.getProveedor())
            dialog.ui.dsbAnchoFilmMi.setValue(filmi.getAncho())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarFilmMi is not None:
                if (dialog.aceptar):
                    filmi.setProveedor(dialog.ui.leProveedorFilmMi.text())
                    filmi.setAncho(dialog.ui.dsbAnchoFilmMi.value())
                    DAO.FilmMicronaje(filmi).modificarFilmMi()
                    self.cargarviewfilmmi()

    "metodos para el crud de cold foil"
    def cargarviewcoldfoil(self):
        self.modelcoldfoil = QtSql.QSqlTableModel(self)
        self.modelcoldfoil.setTable("cold_foil")
        listaref = self.cadenadereferencias(DAO.ColdFoilFicha().leerColdFoilEnFicha(self.edicion))
        self.modelcoldfoil.setFilter("idColdFoil  in {0}".format(listaref))
        self.modelcoldfoil.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelcoldfoil.select()
        self.ui.viewColdFoil.setModel(self.modelcoldfoil)
        self.ui.viewColdFoil.hideColumn(0)
        pass
    def insertRecordscoldfoil(self):
        try:
            coldfoil = DTO.ColdFoil()
            coldfoil.setProveedor(self.ui.leProveedorColdFoilMod.text())
            coldfoil.setAncho(self.ui.dsbAnchoColdFoilMod.value())

            DAO.ColdFoil(coldfoil).ingresarColdFoil()
            "crear referencia de forma inmediata"
            cff = DAO.ColdFoilFicha()
            cff.setIdFicha(self.edicion)
            cff.setIdColdFoil(DAO.ColdFoil().idUltimoColdFoil())
            cff.insertarColdFoilFicha()
            self.cargarviewcoldfoil()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modelcoldfoil.submitAll()
    def deleteRecordscoldfoil(self):
        try:
            fila = []
            for col in range(self.modelcoldfoil.columnCount()):
                index = self.modelcoldfoil.index(self.ui.viewColdFoil.currentIndex().row(), col)
                fila.append(str(self.modelcoldfoil.data(index).toString()))
            coldfoil = DTO.ColdFoil()
            coldfoil.setIdColdFoil(fila[0])
            DAO.ColdFoilFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.ColdFoil(coldfoil).eliminarColdFoil()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modelcoldfoil.submitAll()
    def updateRecordscoldfoil(self):
        try:
            fila = []
            for col in range(self.modelcoldfoil.columnCount()):
                index = self.modelcoldfoil.index(self.ui.viewColdFoil.currentIndex().row(), col)
                fila.append(str(self.modelcoldfoil.data(index).toString()))

            coldfoild = DTO.ColdFoil()
            coldfoild.setIdColdFoil(fila[0])
            coldfoild.setProveedor(str(fila[1]))
            coldfoild.setAncho(float(fila[2]))

            dialog = editarColdFoil.vEditarColdFoil()
            dialog.ui.leProveedorColdFoil.setText(coldfoild.getProveedor())
            dialog.ui.dsbAnchoColdFoil.setValue(coldfoild.getAncho())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarColdFoil is not None:
                if (dialog.aceptado):
                    coldfoild.setProveedor(dialog.ui.leProveedorColdFoil.text())
                    coldfoild.setAncho(dialog.ui.dsbAnchoColdFoil.value())
                    DAO.ColdFoil(coldfoild).modificarColdFoil()
                    self.cargarviewcoldfoil()


    "metodos para el crud de tipos de barniz"
    def cargarviewtbarniz(self):
        self.modeltbarniz = QtSql.QSqlTableModel(self)
        self.modeltbarniz.setTable("tipo_barniz")
        listaref = self.cadenadereferencias(DAO.TBarnizFicha().leerTBarnizEnFicha(self.edicion))
        self.modeltbarniz.setFilter("idTBarniz  in {0}".format(listaref))
        self.modeltbarniz.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeltbarniz.select()
        self.ui.viewTipoBarniz.setModel(self.modeltbarniz)
        self.ui.viewTipoBarniz.hideColumn(0)
        pass
    def insertRecordsTBarniz(self):
        try:
            tbarniz = DTO.TipoBarniz()
            tbarniz.setProveedor(self.ui.leProveedorTBarnizMod.text())
            tbarniz.setTipo(self.ui.leTipoTBarnizMod.text())
            tbarniz.setAnilox(self.ui.leAniloxTBarnizMod.text())

            DAO.TipoBarniz(tbarniz).ingresarTBarniz()
            "crear referencia de forma inmediata"
            tbf = DAO.TBarnizFicha()
            tbf.setIdFicha(self.edicion)
            tbf.setIdTBarniz(DAO.TipoBarniz().idUltimoTBarniz())
            tbf.insertarTBarnizFicha()
            self.cargarviewtbarniz()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modeltbarniz.submitAll()
    def deleteRecordsTBarniz(self):
        try:
            fila = []
            for col in range(self.modeltbarniz.columnCount()):
                index = self.modeltbarniz.index(self.ui.viewTipoBarniz.currentIndex().row(), col)
                fila.append(str(self.modeltbarniz.data(index).toString()))
            tbarniz = DTO.TipoBarniz()
            tbarniz.setIdTBarniz(fila[0])
            DAO.TBarnizFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.TipoBarniz(tbarniz).eliminarTBarniz()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modeltbarniz.submitAll()
    def updateRecordsTBarniz(self):
        try:
            fila = []
            for col in range(self.modeltbarniz.columnCount()):
                index = self.modeltbarniz.index(self.ui.viewTipoBarniz.currentIndex().row(), col)
                fila.append(str(self.modeltbarniz.data(index).toString()))

            tbarniz = DTO.TipoBarniz()
            tbarniz.setIdTBarniz(fila[0])
            tbarniz.setProveedor(str(fila[1]))
            tbarniz.setTipo(str(fila[2]))
            tbarniz.setAnilox(str(fila[3]))

            dialog = editarTBarniz.vEditarTBarniz()
            dialog.ui.leProveedorTBarniz.setText(tbarniz.getProveedor())
            dialog.ui.leTipoTBarniz.setText(tbarniz.getTipo())
            dialog.ui.leAniloxTBarniz.setText(tbarniz.getAnilox())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarTBarniz is not None:
                if (dialog.aceptado):
                    tbarniz.setProveedor(dialog.ui.leProveedorTBarniz.text())
                    tbarniz.setTipo(dialog.ui.leTipoTBarniz.text())
                    tbarniz.setAnilox(dialog.ui.leAniloxTBarniz.text())
                    DAO.TipoBarniz(tbarniz).modificarTBarniz()
                    self.cargarviewtbarniz()

    "metodos para el crud de troqueles"
    def cargarviewtroquel(self):
        self.modeltroquel = QtSql.QSqlTableModel(self)
        self.modeltroquel.setTable("troquel")
        listaref = self.cadenadereferencias(DAO.TroquelFicha().leerTroquelEnFicha(self.edicion))
        self.modeltroquel.setFilter("idTroquel  in {0}".format(listaref))
        self.modeltroquel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeltroquel.select()
        self.ui.viewTroquel.setModel(self.modeltroquel)
        self.ui.viewTroquel.hideColumn(0)
        pass
    def insertRecordsTroquel(self):
        try:
            troquel = DTO.Troquel()
            troquel.setProveedor(self.ui.leProveedorTroquelMod.text())

            DAO.Troquel(troquel).ingresarTroquel()
            "crear referencia de forma inmediata"
            trf = DAO.TroquelFicha()
            trf.setIdFicha(self.edicion)
            trf.setIdTroquel(DAO.Troquel().idUltimoTroquel())
            trf.insertarTroquelFicha()
            self.cargarviewtroquel()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            self.modeltroquel.submitAll()
    def deleteRecordsTroquel(self):
        try:
            fila = []
            for col in range(self.modeltroquel.columnCount()):
                index = self.modeltroquel.index(self.ui.viewTroquel.currentIndex().row(), col)
                fila.append(str(self.modeltroquel.data(index).toString()))
            troquel = DTO.Troquel()
            troquel.setIdTroquel(fila[0])
            DAO.TroquelFicha().eliminarReferencia(fila[0], self.edicion)
            DAO.Troquel(troquel).eliminarTroquel()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.modeltroquel.submitAll()
    def updateRecordsTroquel(self):
        try:
            fila = []
            for col in range(self.modeltroquel.columnCount()):
                index = self.modeltroquel.index(self.ui.viewTroquel.currentIndex().row(), col)
                fila.append(str(self.modeltroquel.data(index).toString()))

            troquel = DTO.Troquel()
            troquel.setIdTroquel(fila[0])
            troquel.setProveedor(str(fila[1]))


            dialog = editarTroquel.vEditarTroquel()
            dialog.ui.leProveedorTroquel.setText(troquel.getProveedor())

            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarTroquel is not None:
                if (dialog.aceptado):
                    troquel.setProveedor(dialog.ui.leProveedorTroquel.text())

                    DAO.Troquel(troquel).modificarTroquel()
                    self.cargarviewtroquel()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = vtablamodelo()
    myWindow.show()
    reload(sys)
    sys.setdefaultencoding('cp1252')
    sys.exit(app.exec_())
