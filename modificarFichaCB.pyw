import sys
from PyQt4 import QtCore, QtGui, QtSql
from Formularios import modificarFicha
from FormulariosCB import editarClienteCB,editarMaterialCB, editarTintaCB, editarMallaCB, editarAdhLamCB
from FormulariosCB import editarAdhCoFoCB, editarFilmiCB, editarColdFoilCB, editarTroquelCB, editarTBarnizCB
from Clases import DTO, DAO, GeneradorPdfAdmin
import datetime
def Conexion(db):
    db.setHostName("localhost")
    db.setDatabaseName("practica")
    db.setUserName("root")
    db.setPassword("")
    if (db.open() == False):
        QtGui.QMessageBox.critical(None, "Database Error",
                                   db.lastError().text())

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

class Vmodificarficha(QtGui.QDialog):
    def __init__(self, parent = None):
        "Constructor de la ventana de gestion de fichas"
        QtGui.QWidget.__init__(self,parent)
        self.ui = modificarFicha.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        self.setWindowFlags(flags)
        self.setWindowTitle("Modificacion de Ficha")
        self.tipoModificar = -1
        self.fichaModificar = -1
        self.edicion = -1
        self.filtroConsulta = -1
        self.activo = False
        self.fichaCargar = -1
        self.cargarCmbCategoriaMod()
        self.cargarCmbClienteMod()
        self.cargarCmbMaquinaMod()
        self.ui.viewMateriales.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewTintas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewMalla.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewAdhLam.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewAdhCofo.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewFilmmi.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewColdFoil.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewTroquel.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.viewTipoBarniz.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
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

        QtCore.QObject.connect(self.ui.pbTerminarModificacion, QtCore.SIGNAL("clicked()"),
                               self.pbTerminarModificacion_click)

    "Conjunto de caracteristicas especiales dependiente de creaicion de ficha"

    "Cargar filtros modificacion"

    def cargarCmbCategoriaMod(self):
        self.ui.cmbCategoriaMod.clear()
        categorias = DAO.Categoria().leerTodo()
        if categorias != tuple():
            for cat in categorias:
                self.ui.cmbCategoriaMod.addItem(cat['nombre'])
            pass

    def cargarCmbClienteMod(self):
        self.ui.cmbClienteMod.clear()
        clientes = DAO.Cliente().leerTodo()
        if clientes != None:
            for cli in clientes:
                self.ui.cmbClienteMod.addItem(cli['nombreCliente'])
            pass

    def cargarCmbMaquinaMod(self):
        self.ui.cmbMaquinaMod.clear()
        maquinas = DAO.Maquina().leerTodo()
        if maquinas != None:
            for maq in maquinas:
                self.ui.cmbMaquinaMod.addItem(maq['codigo'])
            pass

    def cargarPedidosMod(self):
        "se cargan los pedidos para la busqueda"
        self.ui.cmbModificar.clear()
        self.ui.cmbModificar.addItem("---Seleccione Pedidos---")
        pedidos = DAO.FichaTecnica(DTO.FichaTecnica).leerTodo()
        for ped in pedidos:
            self.ui.cmbModificar.addItem(ped['pedido'])
    def cargarEtiquetasMod(self):
        "se carga el nombre de las etiquetas para la busqueda"
        self.ui.cmbModificar.clear()

        self.ui.cmbModificar.addItem("---Seleccione Etiqueta---")
        etiquetas = DAO.FichaTecnica(DTO.FichaTecnica).leerTodo()
        for eti in etiquetas:
            self.ui.cmbModificar.addItem(eti['etiqueta'])

    "Seleccion de registro a modificar"
    def rbModificarEtiqueta_click(self):
        self.cargarEtiquetasMod()
        self.tipoModificar = 1
        pass
    def rbModificarPorPedido_click(self):
        self.cargarPedidosMod()
        self.tipoModificar = 2
        pass
    def cmbModificar_currentIndexChanged(self):
        "Cargar el formulario con los datos de la ficha seleccionada"

        if self.ui.cmbModificar.currentIndex() == 0 or self.ui.cmbModificar.currentIndex() == -1 or str(self.ui.cmbModificar.currentText()).find("---S") > -1:
            self.cargarCmbCategoriaMod()
            self.cargarCmbClienteMod()
            self.cargarCmbMaquinaMod()
            self.limpiarFFichaTecnicaMod()
            pass
        else:
            if self.tipoModificar == 1:
                self.ui.pbModificarFicha.setEnabled(True)

                "Cargar por etiqueta"
                "Recuperar la ficha"
                fichaPedido = DAO.FichaTecnica().recuperarFichaTecnicaEtiqueta(self.ui.cmbModificar.currentText())

                for fic in fichaPedido:
                    f = DTO.FichaTecnica()
                    f.setPedido(fic["Pedido"])
                    f.setEtiqueta(fic["Etiqueta"])
                    ficha = DAO.FichaTecnica(f)
                    ficha.leerFichaTecnicaPedEtMaq()
                    self.cargarFichaModificar(ficha)
                    self.fichaModificar = ficha.getFichaTecnica().getIdFicha()
                    MostrarMensaje("Ficha cargada con exito")

                    break

            elif self.tipoModificar == 2:
                self.ui.pbModificarFicha.setEnabled(True)

                "cargar por pedido"

                fichaPedido = DTO.FichaTecnica()
                fichaPedido.setPedido(self.ui.cmbModificar.currentText())
                ficha = DAO.FichaTecnica(fichaPedido)

                ficha.leerFichaTecnica()

                self.cargarFichaModificar(ficha)
                self.fichaModificar = ficha.getFichaTecnica().getIdFicha()
                MostrarMensaje("Ficha cargada con exito")
        pass

    def cargarFichaModificar(self, ficha):
        "Comenzar a cargar datos"
        self.ui.lePedidoMod.setText(ficha.getFichaTecnica().getPedido())
        self.ui.leEtiquetaMod.setText(ficha.getFichaTecnica().getEtiqueta())
        self.ui.deFechaFichaMod.setDate(ficha.getFichaTecnica().getFecha())
        if ficha.getFichaTecnica().getClisse():
            self.ui.rbConvencionalesMod.setChecked(True)
        else:
            self.ui.rbDigitalesMod.setChecked(True)

        self.ui.dsbVelocidadFichaMod.setValue(float(ficha.getFichaTecnica().getVelocidad()))
        self.edicion = ficha.getFichaTecnica().getIdFicha()

        cat = DTO.Categoria()
        cat.setIdCategoria(ficha.getFichaTecnica().getIdCategoria())
        categoria = DAO.Categoria(cat)
        categoria.leerCategoriaId()

        for i in range(self.ui.cmbCategoriaMod.count()):
            if self.ui.cmbCategoriaMod.itemText(i) == categoria.getCategoria().getNombre():
                self.ui.cmbCategoriaMod.setCurrentIndex(i)

        cli = DTO.Cliente()
        cli.setIdCliente(ficha.getFichaTecnica().getIdCliente())
        cliente = DAO.Cliente(cli)
        cliente.leerClienteId()

        for i in range(self.ui.cmbClienteMod.count()):
            if self.ui.cmbClienteMod.itemText(i) == cliente.getCliente().getNombre():
                self.ui.cmbClienteMod.setCurrentIndex(i)

        maq = DTO.Maquina()
        maq.setIdMaquina(ficha.getFichaTecnica().getIdMaquina())
        maquina = DAO.Maquina(maq)
        maquina.leerMaquinaId()

        for i in range(self.ui.cmbMaquinaMod.count()):
            if self.ui.cmbMaquinaMod.itemText(i) == maquina.getMaquina().getCodigo():
                self.ui.cmbMaquinaMod.setCurrentIndex(i)
        self.cargarviewmateriales()
        self.cargarviewtintas()
        self.cargarviewmallas()
        self.cargarviewadhlam()
        self.cargarviewadhcofo()
        self.cargarviewfilmmi()
        self.cargarviewcoldfoil()
        self.cargarviewtbarniz()
        self.cargarviewtroquel()

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

        self.modelMaterial.setHeaderData(1, QtCore.Qt.Horizontal, 'Codigo')
        self.modelMaterial.setHeaderData(2, QtCore.Qt.Horizontal, 'Nombre')
        self.modelMaterial.setHeaderData(3, QtCore.Qt.Horizontal, 'Proveedor')
        self.modelMaterial.setHeaderData(4, QtCore.Qt.Horizontal, 'Ancho')
        self.modelMaterial.setHeaderData(5, QtCore.Qt.Horizontal, 'TC')
        self.modelMaterial.select()
        self.ui.viewMateriales.setModel(self.modelMaterial)
        self.ui.viewMateriales.setColumnWidth(1,100)
        self.ui.viewMateriales.setColumnWidth(2, 100)
        self.ui.viewMateriales.setColumnWidth(3, 100)
        self.ui.viewMateriales.setColumnWidth(4, 50)
        self.ui.viewMateriales.setColumnWidth(5, 30)
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
            if self.ui.rbTC1Mod.isChecked():
                mat.setTC(True)
            else:
                mat.setTC(False)
            material = DAO.Material(mat)
            material.insertarMaterial()
            "crear referencia de forma inmediata"
            mf = DAO.MaterialFicha()
            mf.setIdFicha(self.edicion)
            mf.setIdMaterial(DAO.Material().idUltimoMaterialInsertada())
            mf.insertarMaterialFicha()

        except Exception as e:
            MostrarError(str(e.message))

        else:
            MostrarMensaje("Material agregado exitosamente")
            self.cargarviewmateriales()
            self.limpiarFMateriales()
    def deleteRecordsMateriales(self):
        try:
            if self.modelMaterial.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewMateriales.selectedIndexes()) < 5:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
            fila = []
            for col in range(self.modelMaterial.columnCount()):
                index = self.modelMaterial.index(self.ui.viewMateriales.currentIndex().row(), col)
                fila.append(str(self.modelMaterial.data(index).toString()))
            mat = DTO.Material()
            mat.setIdMaterial(fila[0])
            DAO.MaterialFicha().eliminarreferencia(fila[0], self.edicion)
            DAO.Material(mat).eliminarMaterial()
        except Exception as e:
            MostrarError(str(e.message))
        else:
            MostrarMensaje("Material eliminado exitosamente")
            self.cargarviewmateriales()
    def updateRecordsMateriales(self):
        try:
            if self.modelMaterial.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewMateriales.selectedIndexes()) < 5:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
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

            dialog = editarMaterialCB.vEditarMaterial()
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
                if (dialog.aceptado):
                    mat.setCodigo(dialog.materialEditado.getCodigo())
                    mat.setNombre(dialog.materialEditado.getNombre())
                    mat.setProveedor(dialog.materialEditado.getProveedor())
                    mat.setAncho(dialog.materialEditado.getAncho())
                    mat.setTC(dialog.materialEditado.getTC())
                    if(DAO.Material(mat).modificarMaterial()):
                        MostrarMensaje("Material editado exitosamente")
                    else:
                        MostrarMensaje("Error al editar material")
                    self.cargarviewmateriales()

        pass
    def limpiarFMateriales(self):
        self.ui.leCodigoMaterialMod.setText("")
        self.ui.leNombreMaterialMod.setText("")
        self.ui.leProveedorMaterialMod.setText("")
        self.ui.dsbAnchoMaterialMod.setValue(0.0)
        self.ui.rbTC1Mod.setChecked(True)

    "Metodos para crud de tintas"

    def cargarviewtintas(self):
        self.modelTinta = QtSql.QSqlTableModel(self)
        self.modelTinta.setTable("tinta")
        listaref = self.cadenadereferencias(DAO.TintaFicha().leerTintaEnFicha(self.edicion))
        self.modelTinta.setFilter("idTinta  in {0}".format(listaref))
        self.modelTinta.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelTinta.setHeaderData(1, QtCore.Qt.Horizontal, 'Color')
        self.modelTinta.setHeaderData(2, QtCore.Qt.Horizontal, 'Tipo')
        self.modelTinta.setHeaderData(3, QtCore.Qt.Horizontal, 'Anilox')
        self.modelTinta.setHeaderData(4, QtCore.Qt.Horizontal, 'Proveedor 1')
        self.modelTinta.setHeaderData(5, QtCore.Qt.Horizontal, 'Proveedor 2')
        self.modelTinta.setHeaderData(6, QtCore.Qt.Horizontal, 'Proveedor 3')
        self.modelTinta.select()
        self.ui.viewTintas.setModel(self.modelTinta)
        self.ui.viewTintas.setColumnWidth(1, 75)
        self.ui.viewTintas.setColumnWidth(2, 75)
        self.ui.viewTintas.setColumnWidth(3, 75)
        self.ui.viewTintas.setColumnWidth(4, 75)
        self.ui.viewTintas.setColumnWidth(5, 75)
        self.ui.viewTintas.setColumnWidth(6, 75)
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
            MostrarMensaje("Exito al agregar tinta")
            self.limpiarFTinta()

            self.modelTinta.submitAll()
    def limpiarFTinta(self):
        self.ui.leColorTintaMod.setText("")
        self.ui.leTipoTintaMod.setText("")
        self.ui.leAniloxTintaMod.setText("")
        self.ui.leProveedorTintaMod.setText("")
        self.ui.leProveedorTintaMod2.setText("")
        self.ui.leProveedorTintaMod3.setText("")
    def deleteRecordsTintas(self):
        try:
            if self.modelTinta.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewTintas.selectedIndexes()) < 6:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar tinta")
            self.modelTinta.submitAll()
    def updateRecordsTintas(self):
        try:
            if self.modelTinta.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewTintas.selectedIndexes()) < 6:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
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

            dialog = editarTintaCB.vEditarTinta()
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
                    if DAO.Tinta(tin).modificarTinta():
                        MostrarMensaje("Exito al modificar tinta")
                    else:
                        MostrarError("Error al modificar tinta")
                    self.modelTinta.submitAll()
        pass
    def limpiarFTinta(self):
        self.ui.leColorTintaMod.setText("")
        self.ui.leTipoTintaMod.setText("")
        self.ui.leAniloxTintaMod.setText("")
        self.ui.leProveedorTintaMod.setText("")
        self.ui.leProveedorTinta2Mod.setText("")
        self.ui.leProveedorTinta3Mod.setText("")


    "Metodos para el crud de mallas"

    def cargarviewmallas(self):
        self.modelMallas = QtSql.QSqlTableModel(self)
        self.modelMallas.setTable("malla")

        listaref = self.cadenadereferencias(DAO.MallaFicha().leerMallaEnFicha(self.edicion))

        self.modelMallas.setFilter("idMalla  in {0}".format(listaref))
        self.modelMallas.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelMallas.setHeaderData(1, QtCore.Qt.Horizontal, 'Tipo')
        self.modelMallas.setHeaderData(2, QtCore.Qt.Horizontal, 'Interna/Externa')
        self.modelMallas.select()
        self.ui.viewMalla.setModel(self.modelMallas)
        self.ui.viewMalla.setColumnWidth(1, 75)
        self.ui.viewMalla.setColumnWidth(2, 100)

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
            MostrarMensaje("Exito al agregar malla")
            self.limpiarFMalla()
            self.cargarviewmallas()
            pass
    def deleteRecordsMallas(self):
        try:
            if self.modelMallas.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewMalla.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar malla")
            self.cargarviewmallas()
            pass
    def updateRecordsMallas(self):
        try:
            if self.modelMallas.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewMalla.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
            fila = []
            for col in range(self.modelMallas.columnCount()):
                index = self.modelMallas.index(self.ui.viewMalla.currentIndex().row(), col)
                fila.append(str(self.modelMallas.data(index).toString()))

            mal = DTO.Malla()
            mal.setIdMalla(fila[0])
            mal.setTipo(str(fila[1]))
            mal.setInterno(bool(fila[2]))

            dialog = editarMallaCB.vEditarMalla()
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
                    if(DAO.Malla(mal).modificarMalla()):
                        MostrarMensaje("Exito al editar malla")
                    else:
                        MostrarError("Error al editar malla")
                    self.cargarviewmallas()
    def limpiarFMalla(self):
        self.ui.leTipoMallaMod.setText("")
        self.ui.rbInterno_2.setChecked(True)

    "metodos para el crud de adhesivos de laminacion"

    def cargarviewadhlam(self):
        self.modeladhlam = QtSql.QSqlTableModel(self)
        self.modeladhlam.setTable("adhesivo_laminacion")
        listaref = self.cadenadereferencias(DAO.AdhLamFicha().leerAdhLamFicha(self.edicion))
        self.modeladhlam.setFilter("idAdhLam  in {0}".format(listaref))
        self.modeladhlam.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeladhlam.setHeaderData(1, QtCore.Qt.Horizontal, 'Proveedor')
        self.modeladhlam.setHeaderData(2, QtCore.Qt.Horizontal, 'Anilox')
        self.modeladhlam.select()
        self.ui.viewAdhLam.setModel(self.modeladhlam)
        self.ui.viewAdhLam.setColumnWidth(1,100)
        self.ui.viewAdhLam.setColumnWidth(2, 100)
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
            self.limpiarFAdhLam()

            MostrarMensaje("Exito al agregar Adhesivo de laminacion")
            self.modeladhlam.submitAll()
    def deleteRecordsAdhlam(self):
        try:
            if self.modeladhlam.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewAdhLam.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar Adhesivo de laminacion")
            self.modeladhlam.submitAll()
    def updateRecordsAdhlam(self):
        try:
            if self.modeladhlam.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewAdhLam.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
            fila = []
            for col in range(self.modeladhlam.columnCount()):
                index = self.modeladhlam.index(self.ui.viewAdhLam.currentIndex().row(), col)
                fila.append(str(self.modeladhlam.data(index).toString()))

            adhlam = DTO.AdhesivoLaminacion()
            adhlam.setIdAdhLam(fila[0])
            adhlam.setProveedor(str(fila[1]))
            adhlam.setAnilox(str(fila[2]))

            dialog = editarAdhLamCB.vEditarAdhLam()
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
                    if DAO.AdhesivoLaminacion(adhlam).modificarAdhLam():
                        MostrarMensaje("Exito al editar Adhesivo de laminacion")
                    else:
                        MostrarError("Error al modificar Adhesivo de laminacion")
                    self.cargarviewadhlam()
    def limpiarFAdhLam(self):
        self.ui.leProveedorAdhLamMod.setText("")
        self.ui.leAniloxAdhLamMod.setText("")


    "metodos para el crud de adhesivo cold foil"

    def cargarviewadhcofo(self):
        self.modeladhcofo = QtSql.QSqlTableModel(self)
        self.modeladhcofo.setTable("adhesivo_coldfoil")
        listaref = self.cadenadereferencias(DAO.AdhCoFoFicha().leerAdhCoFoEnFicha(self.edicion))
        self.modeladhcofo.setFilter("idAdhColdFoil  in {0}".format(listaref))
        self.modeladhcofo.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeladhcofo.setHeaderData(1, QtCore.Qt.Horizontal, 'Proveedor')
        self.modeladhcofo.setHeaderData(2, QtCore.Qt.Horizontal, 'Anilox')
        self.modeladhcofo.select()
        self.ui.viewAdhCofo.setModel(self.modeladhcofo)
        self.ui.viewAdhCofo.setColumnWidth(1, 100)
        self.ui.viewAdhCofo.setColumnWidth(2, 100)
        self.ui.viewAdhCofo.hideColumn(0)
    def insertRecordsdhcofo(self):
        try:
            adhcofo = DTO.AdhesivoColdFoil()
            adhcofo.setProveedor(self.ui.leProveedorAdhCoFoMod.text())
            adhcofo.setAnilox(self.ui.leAniloxAdhCoFoMod.text())

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
            MostrarMensaje("Exito al agregar Adhesivo cold foil")
            self.limpiarFAdhCoFo()
            self.modeladhcofo.submitAll()
    def deleteRecordsdhcofo(self):
        try:
            if self.modeladhcofo.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewAdhCofo.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar Adhesivo cold foil")
            self.modeladhcofo.submitAll()

    def updateRecordsdhcofo(self):
        try:
            if self.modeladhcofo.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewAdhCofo.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder modificar")
            fila = []
            for col in range(self.modeladhcofo.columnCount()):
                index = self.modeladhcofo.index(self.ui.viewAdhCofo.currentIndex().row(), col)
                fila.append(str(self.modeladhcofo.data(index).toString()))

            adhcofo = DTO.AdhesivoColdFoil()
            adhcofo.setIdAdhCoFo(fila[0])
            adhcofo.setProveedor(str(fila[1]))
            adhcofo.setAnilox(str(fila[2]))

            dialog = editarAdhCoFoCB.vEditarAdhCoFo()
            dialog.ui.leProveedorAdhCoFo.setText(adhcofo.getProveedor())
            dialog.ui.leAniloxAdhCoFo.setText(adhcofo.getAnilox())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarAdhCoFo is not None:
                if (dialog.aceptado):
                    adhcofo.setProveedor(dialog.ui.leProveedorAdhCoFo.text())
                    adhcofo.setAnilox(dialog.ui.leAniloxAdhCoFo.text())
                    if (DAO.AdhesivoColdFoil(adhcofo).modificarAdhCoFo()):
                        MostrarMensaje("Exito al editar Adhesivo cold foil")
                    else:
                        MostrarMensaje("Error al editar Adhesivo cold foil")
                    self.cargarviewadhcofo()
    def limpiarFAdhCoFo(self):
        self.ui.leProveedorAdhCoFoMod.setText("")
        self.ui.leAniloxAdhCoFoMod.setText("")

    "metodos para el crud de film micronaje"

    def cargarviewfilmmi(self):
        self.modelfilmi = QtSql.QSqlTableModel(self)
        self.modelfilmi.setTable("film_micronaje")
        listaref = self.cadenadereferencias(DAO.FilmMiFicha().leerFilmMiEnFicha(self.edicion))
        self.modelfilmi.setFilter("idFilmMi  in {0}".format(listaref))
        self.modelfilmi.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelfilmi.setHeaderData(1, QtCore.Qt.Horizontal, 'Proveedor')
        self.modelfilmi.setHeaderData(2, QtCore.Qt.Horizontal, 'Ancho')
        self.modelfilmi.select()
        self.ui.viewFilmmi.setModel(self.modelfilmi)
        self.ui.viewFilmmi.setColumnWidth(1, 100)
        self.ui.viewFilmmi.setColumnWidth(2, 100)
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
            MostrarMensaje("Exito al agregar Film micronaje")
            self.limpiarFFilmmi()
            self.modelfilmi.submitAll()
    def deleteRecordsfilmmi(self):
        try:
            if self.modelfilmi.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewFilmmi.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar Film micronaje")
            self.modelfilmi.submitAll()
    def updateRecordsfilmmi(self):
        try:
            if self.modelfilmi.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewFilmmi.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
            fila = []
            for col in range(self.modelfilmi.columnCount()):
                index = self.modelfilmi.index(self.ui.viewFilmmi.currentIndex().row(), col)
                fila.append(str(self.modelfilmi.data(index).toString()))

            filmi = DTO.FilmMicronaje()
            filmi.setIdFilmMi(fila[0])
            filmi.setProveedor(str(fila[1]))
            filmi.setAncho(float(fila[2]))

            dialog = editarFilmiCB.vEditarFilmMi()
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
                    if DAO.FilmMicronaje(filmi).modificarFilmMi():
                        MostrarMensaje("Exito al editar Film micronaje")
                    else:
                        MostrarMensaje("Error al editar Film micronaje")
                    self.cargarviewfilmmi()
    def limpiarFFilmmi(self):
        self.ui.leProveedorFilmMiMod.setText("")
        self.ui.dsbAnchoFilmMiMod.setValue(0.0)

    "metodos para el crud de cold foil"

    def cargarviewcoldfoil(self):
        self.modelcoldfoil = QtSql.QSqlTableModel(self)
        self.modelcoldfoil.setTable("cold_foil")
        listaref = self.cadenadereferencias(DAO.ColdFoilFicha().leerColdFoilEnFicha(self.edicion))
        self.modelcoldfoil.setFilter("idColdFoil  in {0}".format(listaref))
        self.modelcoldfoil.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modelcoldfoil.setHeaderData(1, QtCore.Qt.Horizontal, 'Proveedor')
        self.modelcoldfoil.setHeaderData(2, QtCore.Qt.Horizontal, 'Ancho')
        self.modelcoldfoil.setHeaderData(3, QtCore.Qt.Horizontal, 'Tipo')
        self.modelcoldfoil.select()
        self.ui.viewColdFoil.setModel(self.modelcoldfoil)
        self.ui.viewColdFoil.setColumnWidth(1, 100)
        self.ui.viewColdFoil.setColumnWidth(2, 100)
        self.ui.viewColdFoil.setColumnWidth(3, 100)
        "Se modifica la presentacion de la informacion para que se entendible"
        for row in range(self.modelcoldfoil.rowCount()):
            index = self.modelcoldfoil.index(row, 3)
            estado = self.modelcoldfoil.data(index).toBool()
            if estado == True:
                self.ui.viewColdFoil.model().setData(index, "COLD FOIL")
            else:
                self.ui.viewColdFoil.model().setData(index, "HOT STAMPING")

        self.ui.viewColdFoil.hideColumn(0)
        pass
    def insertRecordscoldfoil(self):
        try:
            coldfoil = DTO.ColdFoil()
            coldfoil.setProveedor(self.ui.leProveedorColdFoilMod.text())
            coldfoil.setAncho(self.ui.dsbAnchoColdFoilMod.value())
            coldfoil.setTipo(self.ui.rbCF.isChecked())

            quePaso = DAO.ColdFoil(coldfoil).ingresarColdFoil()
            "crear referencia de forma inmediata"
            cff = DAO.ColdFoilFicha()
            cff.setIdFicha(self.edicion)
            cff.setIdColdFoil(DAO.ColdFoil().idUltimoColdFoil())
            cff.insertarColdFoilFicha()
            self.cargarviewcoldfoil()
        except Exception as e:
            MostrarError(str(e.message))

        else:
            MostrarMensaje("Exito al agregar Cold foil")
            self.limpiarFColdFoil()
            self.cargarviewcoldfoil()
    def deleteRecordscoldfoil(self):
        try:
            if self.modelcoldfoil.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewColdFoil.selectedIndexes()) < 3:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar Cold foil")
            self.cargarviewcoldfoil()
    def updateRecordscoldfoil(self):
        try:
            if self.modelcoldfoil.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewColdFoil.selectedIndexes()) < 3:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
            fila = []
            for col in range(self.modelcoldfoil.columnCount()):
                index = self.modelcoldfoil.index(self.ui.viewColdFoil.currentIndex().row(), col)
                fila.append(str(self.modelcoldfoil.data(index).toString()))

            coldfoild = DTO.ColdFoil()
            coldfoild.setIdColdFoil(fila[0])
            coldfoild.setProveedor(str(fila[1]))
            coldfoild.setAncho(float(fila[2]))
            if str(fila[3]) == 'HOT STAMPING':
                coldfoild.setTipo(False)
            else:
                coldfoild.setTipo(True)


            dialog = editarColdFoilCB.vEditarColdFoil()
            dialog.ui.leProveedorColdFoil.setText(coldfoild.getProveedor())
            dialog.ui.dsbAnchoColdFoil.setValue(coldfoild.getAncho())
            dialog.ui.rbCF.setChecked(coldfoild.getTipo())
            if coldfoild.getTipo() is True:
                dialog.ui.rbCF.setChecked(True)

            else:
                dialog.ui.rbHS.setChecked(True)
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarColdFoil is not None:
                if (dialog.aceptado):
                    coldfoild.setProveedor(dialog.ui.leProveedorColdFoil.text())
                    coldfoild.setAncho(dialog.ui.dsbAnchoColdFoil.value())
                    coldfoild.setTipo(dialog.ui.rbCF.isChecked())
                    if(DAO.ColdFoil(coldfoild).modificarColdFoil()):
                        MostrarMensaje("Exito al modificar Cold foil")
                    else:
                        MostrarError("Error al modificar Cold foil")
                    self.cargarviewcoldfoil()
    def limpiarFColdFoil(self):
        self.ui.leProveedorColdFoilMod.setText("")
        self.ui.dsbAnchoColdFoilMod.setValue(0.0)
        self.ui.rbCF.setChecked(True)


    "metodos para el crud de tipos de barniz"

    def cargarviewtbarniz(self):
        self.modeltbarniz = QtSql.QSqlTableModel(self)
        self.modeltbarniz.setTable("tipo_barniz")
        listaref = self.cadenadereferencias(DAO.TBarnizFicha().leerTBarnizEnFicha(self.edicion))
        self.modeltbarniz.setFilter("idTBarniz  in {0}".format(listaref))
        self.modeltbarniz.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeltbarniz.setHeaderData(1, QtCore.Qt.Horizontal, 'Proveedor')
        self.modeltbarniz.setHeaderData(2, QtCore.Qt.Horizontal, 'Tipo')
        self.modeltbarniz.setHeaderData(3, QtCore.Qt.Horizontal, 'Anilox')

        self.modeltbarniz.select()
        self.ui.viewTipoBarniz.setModel(self.modeltbarniz)
        self.ui.viewTipoBarniz.setColumnWidth(1, 100)
        self.ui.viewTipoBarniz.setColumnWidth(2, 100)
        self.ui.viewTipoBarniz.setColumnWidth(3, 100)
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
            MostrarMensaje("Exito al agregar Tipo de barniz")
            self.limpiarFTBarniz()
            self.modeltbarniz.submitAll()
    def deleteRecordsTBarniz(self):
        try:
            if self.modeltbarniz.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewTipoBarniz.selectedIndexes()) < 3:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar Tipo de barniz")
            self.modeltbarniz.submitAll()
    def updateRecordsTBarniz(self):
        try:
            if self.modeltbarniz.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewTipoBarniz.selectedIndexes()) < 3:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
            fila = []
            for col in range(self.modeltbarniz.columnCount()):
                index = self.modeltbarniz.index(self.ui.viewTipoBarniz.currentIndex().row(), col)
                fila.append(str(self.modeltbarniz.data(index).toString()))

            tbarniz = DTO.TipoBarniz()
            tbarniz.setIdTBarniz(fila[0])
            tbarniz.setProveedor(str(fila[1]))
            tbarniz.setTipo(str(fila[2]))
            tbarniz.setAnilox(str(fila[3]))

            dialog = editarTBarnizCB.vEditarTBarniz()
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
                    if DAO.TipoBarniz(tbarniz).modificarTBarniz():
                        MostrarMensaje("Exito al editar Tipo de barniz")
                    else:
                        MostrarError("Error al editar Tipo de barniz")
                    self.cargarviewtbarniz()
    def limpiarFTBarniz(self):
        self.ui.leProveedorTBarnizMod.setText("")
        self.ui.leTipoTBarnizMod.setText("")
        self.ui.leAniloxTBarnizMod.setText("")

    "metodos para el crud de troqueles"

    def cargarviewtroquel(self):
        self.modeltroquel = QtSql.QSqlTableModel(self)
        self.modeltroquel.setTable("troquel")
        listaref = self.cadenadereferencias(DAO.TroquelFicha().leerTroquelEnFicha(self.edicion))
        self.modeltroquel.setFilter("idTroquel  in {0}".format(listaref))
        self.modeltroquel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.modeltroquel.setHeaderData(1, QtCore.Qt.Horizontal, 'Proveedor')
        self.modeltroquel.setHeaderData(2, QtCore.Qt.Horizontal, 'Observacion')
        self.modeltroquel.select()
        self.ui.viewTroquel.setModel(self.modeltroquel)
        self.ui.viewTroquel.setColumnWidth(1, 100)
        self.ui.viewTroquel.setColumnWidth(2, 100)
        self.ui.viewTroquel.hideColumn(0)
        pass
    def insertRecordsTroquel(self):
        try:
            troquel = DTO.Troquel()
            troquel.setProveedor(self.ui.leProveedorTroquelMod.text())
            troquel.setObservacion(self.ui.leObservacionesTroquelMod.text())

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
            MostrarMensaje("Exito al agregar Troquel")
            self.limpiarFTroquel()
            self.modeltroquel.submitAll()
    def deleteRecordsTroquel(self):
        try:
            if self.modeltroquel.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewTroquel.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            MostrarMensaje("Exito al eliminar Troquel")
            self.modeltroquel.submitAll()
    def updateRecordsTroquel(self):
        try:
            if self.modeltroquel.rowCount() == 0:
                raise Exception("No existen registros a editar")
            if len(self.ui.viewTroquel.selectedIndexes()) < 2:
                raise Exception("Debe seleccionar el numero de la fila para poder editar")
            fila = []
            for col in range(self.modeltroquel.columnCount()):
                index = self.modeltroquel.index(self.ui.viewTroquel.currentIndex().row(), col)
                fila.append(str(self.modeltroquel.data(index).toString()))

            troquel = DTO.Troquel()
            troquel.setIdTroquel(fila[0])
            troquel.setProveedor(str(fila[1]))
            troquel.setObservacion(str(fila[2]))

            dialog = editarTroquelCB.vEditarTroquel()
            dialog.ui.leProveedorTroquel.setText(troquel.getProveedor())
            dialog.ui.leObservacionesTroquel.setText(troquel.getObservacion())
            dialog.exec_()

        except Exception as e:
            MostrarError(str(e.message))
        else:
            if dialog.editarTroquel is not None:
                if (dialog.aceptado):
                    troquel.setProveedor(dialog.ui.leProveedorTroquel.text())
                    troquel.setObservacion(dialog.ui.leObservacionesTroquel.text())

                    if DAO.Troquel(troquel).modificarTroquel():
                        MostrarMensaje("Exito al editar Troquel")
                    else:
                        MostrarError("Error al editar Troquel")
                    self.cargarviewtroquel()

        pass
    def limpiarFTroquel(self):
        self.ui.leProveedorTroquelMod.setText("")

    def pbModificarFicha_click(self):
        "Finalizado"
        "Se lee la categoria"
        categoriaBuscar = DTO.Categoria()
        categoriaBuscar.setNombre(str(self.ui.cmbCategoriaMod.currentText()))
        categoriaBuscada = DAO.Categoria(categoriaBuscar)
        categoriaBuscada.leerCategoria()

        "Sel lee el cliente cliente"
        clienteBuscar = DTO.Cliente()
        clienteBuscar.setNombre(str(self.ui.cmbClienteMod.currentText()))
        clienteBuscado = DAO.Cliente(clienteBuscar)
        clienteBuscado.leerClienteNombre()

        "Se lee la maquina"
        maquinaBuscar = DTO.Maquina()
        maquinaBuscar.setCodigo(str(self.ui.cmbMaquinaMod.currentText()))
        maquinaBuscada = DAO.Maquina(maquinaBuscar)
        maquinaBuscada.leerMaquina()

        fichaTecnica = DTO.FichaTecnica()
        fichaTecnica.setIdFicha(self.edicion)
        fichaTecnica.setPedido(str(self.ui.lePedidoMod.text()))
        fichaTecnica.setEtiqueta(str(self.ui.leEtiquetaMod.text()))
        fichaTecnica.setFecha(str(self.ui.deFechaFichaMod.date().toString("dd/MM/yyyy")))
        fichaTecnica.setVelocidad(float(self.ui.dsbVelocidadFichaMod.value()))
        fichaTecnica.setIdCategoria(categoriaBuscada.getCategoria().getIdCategoria())
        fichaTecnica.setIdCliente(clienteBuscado.getCliente().getIdCliente())
        fichaTecnica.setIdMaquina(maquinaBuscada.getMaquina().getIdMaquina())
        if self.ui.rbConvencionalesMod.isChecked():
            fichaTecnica.setClisse(True)
        else:
            fichaTecnica.setClisse(False)
        modificarFicha = DAO.FichaTecnica(fichaTecnica)

        if modificarFicha.modificarFichaTecnica():
            MostrarMensaje("La ficha a sido modificada exitosamente")
        else:
            MostrarError("La ficha no se pudo modificar")
        self.estadoceromodficar()
        pass

    def estadoceromodficar(self):
        "Limpiar Formulario Modificacion"
        self.limpiarFFichaTecnicaMod()

    def limpiarFFichaTecnicaMod(self):
        self.limpiarFMateriales()
        self.limpiarFTinta()
        self.limpiarFMalla()
        self.limpiarFAdhLam()
        self.limpiarFAdhCoFo()
        self.limpiarFFilmmi()
        self.limpiarFColdFoil()
        self.limpiarFTBarniz()
        self.limpiarFTroquel()
        self.ui.lePedidoMod.setText("")
        self.ui.leEtiquetaMod.setText("")
        self.ui.dsbVelocidadFichaMod.setValue(float(0))
        self.edicion = -1
        ficha = DTO.FichaTecnica()
        ficha.setIdFicha(self.edicion)
        self.cargarFichaModificar(DAO.FichaTecnica(ficha))

    def pbTerminarModificacion_click(self):
        "Finalizado"
        "Se lee la categoria"
        categoriaBuscar = DTO.Categoria()
        categoriaBuscar.setNombre(str(self.ui.cmbCategoriaMod.currentText()))
        categoriaBuscada = DAO.Categoria(categoriaBuscar)
        categoriaBuscada.leerCategoria()

        "Sel lee el cliente cliente"
        clienteBuscar = DTO.Cliente()
        clienteBuscar.setNombre(str(self.ui.cmbClienteMod.currentText()))
        clienteBuscado = DAO.Cliente(clienteBuscar)
        clienteBuscado.leerClienteNombre()

        "Se lee la maquina"
        maquinaBuscar = DTO.Maquina()
        maquinaBuscar.setCodigo(str(self.ui.cmbMaquinaMod.currentText()))
        maquinaBuscada = DAO.Maquina(maquinaBuscar)
        maquinaBuscada.leerMaquina()

        fichaTecnica = DTO.FichaTecnica()
        fichaTecnica.setIdFicha(self.edicion)
        fichaTecnica.setPedido(str(self.ui.lePedidoMod.text()))
        fichaTecnica.setEtiqueta(str(self.ui.leEtiquetaMod.text()))
        fichaTecnica.setFecha(str(self.ui.deFechaFichaMod.date().toString("dd/MM/yyyy")))
        fichaTecnica.setVelocidad(float(self.ui.dsbVelocidadFichaMod.value()))
        fichaTecnica.setIdCategoria(categoriaBuscada.getCategoria().getIdCategoria())
        fichaTecnica.setIdCliente(clienteBuscado.getCliente().getIdCliente())
        fichaTecnica.setIdMaquina(maquinaBuscada.getMaquina().getIdMaquina())
        if self.ui.rbConvencionalesMod.isChecked():
            fichaTecnica.setClisse(True)
        else:
            fichaTecnica.setClisse(False)
        modificarFicha = DAO.FichaTecnica(fichaTecnica)

        if modificarFicha.modificarFichaTecnica():
            MostrarMensaje("La ficha a sido modificada exitosamente")
        else:
            MostrarError("La ficha no se pudo modificar")
        self.estadoceromodficar()
        self.accept()
        pass


