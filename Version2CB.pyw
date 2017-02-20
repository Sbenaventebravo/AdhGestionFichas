import sys
from PyQt4 import QtCore, QtGui, QtSql
import modificarFichaCB, agregarCaracteristicas
from Formularios import Version2
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

class VgestionFichas(QtGui.QDialog):

    def __init__(self, parent = None):
        "Constructor de la ventana de gestion de fichas"
        QtGui.QWidget.__init__(self,parent)
        self.ui = Version2.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        self.setWindowFlags(flags)
        self.setWindowTitle("Gestion de fichas tecnicas para etiquetas")
        self.ui.tabPrincipal.setCurrentIndex(0)
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        Conexion(self.db)
        self.ui.tabOpFichas.setCurrentIndex(0)
        self.cargarCmbCliente()
        self.cargarCmbCategoria()
        self.cargarCmbMaquina()
        self.tipoModificar = -1
        self.fichaModificar = -1
        self.edicion = -1
        self.filtroConsulta = -1
        self.activo = False
        self.ultimoIndicePrincipal = 0


        self.estadoceroconsulta()
        self.limpiarFFichaTecnica()

        self.ui.twCatergoria.setColumnWidth(0, 200)

        self.ui.twCliente.setColumnWidth(0, 100)
        self.ui.twCliente.setColumnWidth(1, 400)

        self.ui.twMaquina.setColumnWidth(0, 150)

        self.ui.twCliente.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.twMaquina.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.twCatergoria.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.twFichas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        QtCore.QObject.connect(self.ui.tabPrincipal, QtCore.SIGNAL('currentChanged (int)'),
                               self.tabPrincipal_currentChanged)
        QtCore.QObject.connect(self.ui.tabOpFichas, QtCore.SIGNAL('currentChanged (int)'),
                               self.tabOpFichas_currentChanged)
        QtCore.QObject.connect(self.ui.pbGuardarFicha, QtCore.SIGNAL("clicked()"),
                               self.pbguardarficha_click)
        "Menu para operaciones en categorias"

        QtCore.QObject.connect(self.ui.pbAniadirCategoria, QtCore.SIGNAL('clicked()'),
                               self.pbAniadirCategoria_click)
        QtCore.QObject.connect(self.ui.pbEditarCategoria, QtCore.SIGNAL('clicked()'),
                               self.pbEditarCategoria_click)

        "Menu para operaciones en clientes "
        QtCore.QObject.connect(self.ui.pbAniadirCliente, QtCore.SIGNAL('clicked()'), self.pbAniadirCliente_click)
        QtCore.QObject.connect(self.ui.pbEditarCliente, QtCore.SIGNAL('clicked()'), self.pbEditarCliente_click)

        "Menu operaciones para maquinas"
        self.CargarTwMaquinas()
        QtCore.QObject.connect(self.ui.pbAniadirMaquina, QtCore.SIGNAL('clicked()'), self.pbAniadirMaquina_click)
        QtCore.QObject.connect(self.ui.pbEditarMaquina, QtCore.SIGNAL('clicked()'), self.pbEditarMaquina_click)


        """para el tipo de filtro:
                              ** -1 equivale a que el filtro no esta seleccionado
                              **  1 equivale al filtro de Categorias
                              **  2 equivale al filtro de Pedidos
                              **  3 equivale al filtro de Etiquetas
                              **  4 equivale al filtro de Clientes"""
        self.tipoFiltro = {1: self.mostrarFichasCategoria, 2: self.mostrarFichasPedido,
                           3: self.mostrarFichasEtiqueta, 4: self.mostrarFichasCliente}
        self.filtroSeleccionado = -1

        QtCore.QObject.connect(self.ui.rbCategoria, QtCore.SIGNAL("clicked(bool)"), self.rbCategoria_click)
        QtCore.QObject.connect(self.ui.rbEtiqueta, QtCore.SIGNAL("clicked(bool)"), self.rbEtiqueta_click)
        QtCore.QObject.connect(self.ui.rbCliente, QtCore.SIGNAL("clicked(bool)"), self.rbCliente_click)
        QtCore.QObject.connect(self.ui.rbPedidos, QtCore.SIGNAL("clicked(bool)"), self.rbPedido_click)
        QtCore.QObject.connect(self.ui.cmbBusqueda, QtCore.SIGNAL("currentIndexChanged (int)"),
                               self.cmbBusqueda_indexChange)
        QtCore.QObject.connect(self.ui.pbMostrarFicha, QtCore.SIGNAL("clicked()"),
                               self.generarInforme)
        QtCore.QObject.connect(self.ui.pbModificarFicha, QtCore.SIGNAL("clicked()"), self.pbModificarFicha_click)




    "Conjunto Principal"
    def tabPrincipal_currentChanged(self):

        if self.ui.tabPrincipal.currentIndex() == 0:
            self.ui.tabOpFichas.setCurrentIndex(0)
            self.cargarCmbCliente()
            self.cargarCmbCategoria()
            self.cargarCmbMaquina()
            self.limpiarFFichaTecnica()
            self.limpiarfcliente()
        elif self.ui.tabPrincipal.currentIndex() == 1:
            self.CargarTwCategorias()
            self.estadoceroconsulta()

            self.limpiarFFichaTecnica()
            self.limpiarfcliente()

            self.ultimoIndicePrincipal = 1
        elif self.ui.tabPrincipal.currentIndex() == 2:
            self.CargarTwCliente()
            self.estadoceroconsulta()
            self.limpiarFFichaTecnica()

        elif self.ui.tabPrincipal.currentIndex() == 3:
            self.CargarTwMaquinas()
            self.estadoceroconsulta()
            self.limpiarFFichaTecnica()
            self.limpiarfcliente()
            pass
    "Conjuto de operaciones en la ficha"
    def tabOpFichas_currentChanged(self):
        if self.ui.tabOpFichas.currentIndex() == 0:
            self.estadoceroconsulta()
            pass
        elif self.ui.tabOpFichas.currentIndex() == 1:
            self.estadoceroconsulta()
            self.limpiarFFichaTecnica()
        elif self.ui.tabOpFichas.currentIndex() == 2:
            self.estadoceromodficar()
            self.limpiarFFichaTecnica()

            pass
    "Conjunto de creacion de ficha"
    def tabCreaFicha_currentChanged(self):
        if self.ui.tabCreaFicha.currentIndex() == 1:
            self.ui.twMaterial.setColumnWidth(0, 75)
            self.ui.twMaterial.setColumnWidth(1, 75)
            self.ui.twMaterial.setColumnWidth(2, 75)
            self.ui.twMaterial.setColumnWidth(3, 75)
            self.ui.twMaterial.setColumnWidth(4, 25)
            pass
        elif self.ui.tabCreaFicha.currentIndex() == 2:

            self.ui.twTinta.setColumnWidth(0, 75)
            self.ui.twTinta.setColumnWidth(1, 75)
            self.ui.twTinta.setColumnWidth(2, 75)
            self.ui.twTinta.setColumnWidth(3, 75)
            self.ui.twTinta.setColumnWidth(4, 75)
            self.ui.twTinta.setColumnWidth(4, 75)
            pass
        elif self.ui.tabCreaFicha.currentIndex() == 3:
            "Menu para operaciones de Caracteristicas especiales"
            self.ui.tabCarSec.setCurrentIndex(0)
            pass
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
            if self.ui.cmbCategoria.itemText(i) == categoria.getCategoria().getNombre():
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
            if len(self.ui.viewTintas.selectedIndexes()) < 5:
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
            if len(self.ui.viewTintas.selectedIndexes()) < 5:
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
            if len(self.ui.viewMalla.selectedIndexes()) < 5:
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
            if len(self.ui.viewMalla.selectedIndexes()) < 5:
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
            if len(self.ui.viewAdhLam.selectedIndexes()) < 5:
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
            if len(self.ui.viewAdhLam.selectedIndexes()) < 5:
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
            if len(self.ui.viewAdhCofo.selectedIndexes()) < 5:
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
            if self.modeladhlam.rowCount() == 0:
                raise Exception("No existen registros a eliminar")
            if len(self.ui.viewAdhLam.selectedIndexes()) < 5:
                raise Exception("Debe seleccionar el numero de la fila para poder eliminar")
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
            if len(self.ui.viewFilmmi.selectedIndexes()) < 5:
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
            if len(self.ui.viewFilmmi.selectedIndexes()) < 5:
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
            if len(self.ui.viewColdFoil.selectedIndexes()) < 5:
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
            if len(self.ui.viewTipoBarniz.selectedIndexes()) < 5:
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
            if len(self.ui.viewTipoBarniz.selectedIndexes()) < 5:
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
            if len(self.ui.viewTroquel.selectedIndexes()) < 5:
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
            if len(self.ui.viewTroquel.selectedIndexes()) < 5:
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

    "Operaciones Administrar Categorias"
    def pbAniadirCategoria_click(self):
        "aniade categoria a la base de datos "
        try:
            newCategoria, ok = QtGui.QInputDialog.getText(self, "Agregar",
                                                          "Escriba el nombre de la nueva Categoria")
            if not ok:
                pass
            else:
                if ok and (len(newCategoria) != 0):
                    nuevaCategoria = DTO.Categoria()
                    nuevaCategoria.setNombre(newCategoria)
                    daoCategoria = DAO.Categoria(nuevaCategoria)
                    "Validacion de categoria"
                    if not daoCategoria.leerCategoria():
                        DAO.Categoria(nuevaCategoria).insertarCategoria()
                    else:
                        raise Exception("La categoria ya existe, intente con otro nombre")
                elif not newCategoria:
                    raise Exception("El nombre de la categoria no puede estar vacio, intente de nuevo")

        except Exception as e:
            MostrarError(str(e.message))
        else:

            self.CargarTwCategorias()
            MostrarMensaje("Categoria agregada con exito")
        pass
    def pbEditarCategoria_click(self):
        "modifica la categoria seleccionada"
        try:
            if (self.ui.twCatergoria.rowCount() == 0):
                raise Exception("No existen registros a Editar")
            if (len(self.ui.twCatergoria.selectedItems()) == 0):
                raise Exception("Debe seleccionar un registro")
            newCategoria, ok = QtGui.QInputDialog.getText(self, "Editar",
                                                          "Escriba el nuevo de la Categoria")
            if not ok:
                pass
            else:
                if ok and (len(newCategoria) != 0):
                    nuevaCategoria = DTO.Categoria()
                    nuevaCategoria.setNombre(newCategoria)
                    daoCategoria = DAO.Categoria(nuevaCategoria)
                    "Validacion de categoria"

                    categoriamodificar = DTO.Categoria(self.ui.twCatergoria.selectedItems()[0].text())
                    catVieja = DAO.Categoria(categoriamodificar)
                    catVieja.leerCategoria()
                    DAO.Categoria(nuevaCategoria).modificarCategoria(catVieja.getCategoria().getIdCategoria())
                    self.CargarTwCategorias()
                    MostrarMensaje("Categoria Editada con exito")

                elif not newCategoria:
                    raise Exception("El nombre de la categoria no puede estar vacio, intente de nuevo")
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.CargarTwCategorias()
        pass
    def CargarTwCategorias(self):
        "Carga la tabla de nombres de categorias en un controlador visual"
        self.ui.twCatergoria.setRowCount(0)
        categorias = DAO.Categoria().leerTodo()
        for fila in categorias:
            self.ui.twCatergoria.insertRow(self.ui.twCatergoria.rowCount())

            self.ui.twCatergoria.setItem(self.ui.twCatergoria.rowCount()-1, 0,
                                         QtGui.QTableWidgetItem(fila['nombre']))


    "Operaciones Administrar Clientes"
    def pbAniadirCliente_click(self):
        "Aniade cliente a la base de datos"
        try:
            cliente = DTO.Cliente()
            cliente.setRut(self.ui.leRutCliente.text())
            cliente.setNombre(self.ui.leNombreCliente.text())
            daoCliente = DAO.Cliente(cliente)
            if not daoCliente.leerCliente():
                DAO.Cliente(cliente).insertarCliente()
            else:
                raise Exception("El cliente ya existe, por favor intenete con otro (se sugiere otro rut)")

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.CargarTwCliente()
            MostrarMensaje("Cliente agregado con exito")
            self.limpiarfcliente()
        pass
    def pbEditarCliente_click(self):
        "Modifica un cliente"
        try:
            if self.ui.twCliente.rowCount() is 0:
                raise Exception('No existen registros a Editar')
            if len(self.ui.twCliente.selectedItems()) < self.ui.twCliente.columnCount():
                raise Exception('Debe seleccionar el numero de la fila')
            vEditar = editarClienteCB.vEditarCliente()
            clienteViejo = DTO.Cliente(self.ui.twCliente.selectedItems()[0].text())
            daoBuscarCliente = DAO.Cliente(clienteViejo)
            daoBuscarCliente.leerClientePorRut()
            vEditar.ui.leRut.setText(daoBuscarCliente.getCliente().getRut())
            vEditar.ui.leNombre.setText(daoBuscarCliente.getCliente().getNombre())
            vEditar.exec_()

            pass
        except Exception as e:
            MostrarError(str(e.message))
        else:

            if vEditar.clienteEditado is not None:
                try:

                    modificar = DTO.Cliente(vEditar.ui.leRut.text(), vEditar.ui.leNombre.text())
                    DAO.Cliente(modificar).modificarCliente(daoBuscarCliente.getCliente().getIdCliente())
                    MostrarMensaje("Cliente Editado con exito")

                except Exception as e:
                    MostrarError(str(e.message))
                else:
                    self.CargarTwCliente()
        pass
    def CargarTwCliente(self):
        "Carga el listado de Clientes en la respectiva tabla"
        self.ui.twCliente.setRowCount(0)
        clientes = DAO.Cliente().leerTodo()
        for fila in clientes:
            rowNum = self.ui.twCliente.rowCount()
            self.ui.twCliente.insertRow(rowNum)
            self.ui.twCliente.setItem(rowNum, 0, QtGui.QTableWidgetItem(str(fila['rutCliente'])))
            self.ui.twCliente.setItem(rowNum, 1, QtGui.QTableWidgetItem(str(fila['nombreCliente'])))

    def clientesinguardar(self):
        if len(str(self.ui.leNombreCliente.text())) != 0 or len(str(self.ui.leNombreCliente.text())) != 0:
            return True
        return False

    def limpiarfcliente(self):
        self.ui.leRutCliente.setText("")
        self.ui.leNombreCliente.setText("")
    "Operaciones Administrar Maquina"

    def CargarTwMaquinas(self):
        self.ui.twMaquina.setRowCount(0)
        maquinas = DAO.Maquina().leerTodo()
        for fila in maquinas:
            self.ui.twMaquina.insertRow(self.ui.twMaquina.rowCount())
            self.ui.twMaquina.setItem(self.ui.twMaquina.rowCount()-1,0, QtGui.QTableWidgetItem(fila['codigo']))
    def pbAniadirMaquina_click(self):
        try:
            newMaquina, ok = QtGui.QInputDialog.getText(self, "Agregar",
                                                        "Escriba el nombre de la nueva maqina")
            if not ok:
                pass
            else:
                if ok and (len(newMaquina) != 0):
                    nuevaMaquina = DTO.Maquina(newMaquina)
                    nuevaMaquina.setCodigo(newMaquina)
                    daoMaquina = DAO.Maquina(nuevaMaquina)
                    "validacion para el codigo de la maquina"
                    if not daoMaquina.leerMaquina():
                        DAO.Maquina(nuevaMaquina).insertarMaquina()
                    else:
                        raise Exception("El codigo de la maquina ya esta registrado, por favor intente con otro")
                elif not newMaquina:
                    raise Exception("El codigo de la maquina, no puede estar vacio")
        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.CargarTwMaquinas()
            MostrarMensaje("Maquina agregada con exito")
        pass
    def pbEditarMaquina_click(self):
        try:
            if (self.ui.twMaquina.rowCount() == 0):
                raise Exception("No existen registros a Editar")
            if (len(self.ui.twMaquina.selectedItems()) == 0):
                raise Exception("Debe seleccionar un registro")
            popup =QtGui.QInputDialog()
            newMaquina, ok = popup.getText(self, "Editar",
                                                        "Escriba el nuevo codigo de la maquina")
            if not ok:
               pass
            else:
                if ok and (len(newMaquina) != 0):
                    nuevaMaquina = DTO.Maquina()
                    nuevaMaquina.setCodigo(newMaquina)
                    daoMaquina = DAO.Maquina(nuevaMaquina)
                    if not daoMaquina.leerMaquina():
                        maquinamodificar = DTO.Maquina(self.ui.twMaquina.selectedItems()[0].text())
                        maqVieja = DAO.Maquina(maquinamodificar)
                        maqVieja.leerMaquina()
                        DAO.Maquina(nuevaMaquina).modificarMaquina(maqVieja.getMaquina().getIdMaquina())
                        self.CargarTwMaquinas()
                        MostrarMensaje("Maquina Editada con exito")
                    else:
                        raise Exception("El codigo de la maquina ya esta registrado, por favor intente con otro")
                elif not newMaquina:
                    raise Exception("El codigo de la maquina, no puede estar vacio")

        except Exception as e:
            MostrarError(str(e.message))
        else:
            self.CargarTwMaquinas()

        pass


    "Datos en cmb para creacion de fichas"
    def cargarCmbCategoria(self):
        self.ui.cmbCategoria.clear()
        categorias = DAO.Categoria().leerTodo()
        if categorias != tuple():
            for cat in categorias:
                self.ui.cmbCategoria.addItem(cat['nombre'])
            pass
    def cargarCmbCliente(self):
        self.ui.cmbCliente.clear()
        clientes = DAO.Cliente().leerTodo()
        if clientes != None:
            for cli in clientes:
                self.ui.cmbCliente.addItem(cli['nombreCliente'])
            pass
    def cargarCmbMaquina(self):
        self.ui.cmbMaquina.clear()
        maquinas = DAO.Maquina().leerTodo()
        if maquinas != None:
            for maq in maquinas:
                self.ui.cmbMaquina.addItem(maq['codigo'])
            pass

    "Metodos Modulo de Consulta"
    "se cargan los tipos de busqueda"
    def cargarCategoria(self):
        "se cargan las categorias para la busqueda"
        self.ui.cmbBusqueda.clear()
        self.filtroSeleccionado = 1
        self.ui.cmbBusqueda.addItem("---Seleccione Categoria---")
        categorias = DAO.Categoria(DTO.Categoria).leerTodo()
        for cat in categorias:
            self.ui.cmbBusqueda.addItem(cat['nombre'])
    def cargarPedidos(self):
        "se cargan los pedidos para la busqueda"
        self.ui.cmbBusqueda.clear()
        self.filtroSeleccionado = 2
        self.ui.cmbBusqueda.addItem("---Seleccione Pedidos---")
        pedidos = DAO.FichaTecnica(DTO.FichaTecnica).leerTodo()
        for ped in pedidos:
            self.ui.cmbBusqueda.addItem(ped['pedido'])
    def cargarEtiquetas(self):
        "se carga el nombre de las etiquetas para la busqueda"
        self.ui.cmbBusqueda.clear()
        self.filtroSeleccionado = 3
        self.ui.cmbBusqueda.addItem("---Seleccione Etiqueta---")
        etiquetas = DAO.FichaTecnica(DTO.FichaTecnica).leerTodo()
        for eti in etiquetas:
            self.ui.cmbBusqueda.addItem(eti['etiqueta'])
    def cargarClientes(self):
        "se cargan los clientes para la busqueda"
        self.ui.cmbBusqueda.clear()
        self.filtroSeleccionado = 4
        self.ui.cmbBusqueda.addItem("---Seleccione Clientes---")
        clientes = DAO.Cliente(DTO.Cliente).leerTodo()
        for cli in clientes:
            self.ui.cmbBusqueda.addItem(cli['nombreCliente'])

    "Se selecciona el tipo de busqueda"
    def rbCategoria_click(self):
        "Busqueda por categoria"
        self.cargarCategoria()
        self.limpiarTabla()
    def rbPedido_click(self):
        "Busqueda por pedido"
        self.cargarPedidos()
        self.limpiarTabla()
    def rbEtiqueta_click(self):
        "Busqueda por nombre de etiqueta"
        self.cargarEtiquetas()
        self.limpiarTabla()
    def rbCliente_click(self):
        "Busqueda por Cliente"
        self.cargarClientes()
        self.limpiarTabla()

    def mostrarFichasCategoria(self):
        "se cargan las fichas de la categoria seleccionada"
        fichas = DAO.FichaTecnica().leerPorCatergoria(self.ui.cmbBusqueda.currentText())
        self.ui.twFichas.setColumnCount(4)
        self.ui.twFichas.setHorizontalHeaderLabels(["Pedido", "Cliente", "Etiqueta","Maquina"])
        self.ui.twFichas.setColumnWidth(0, 60)
        self.ui.twFichas.setColumnWidth(1, 200)
        self.ui.twFichas.setColumnWidth(2, 200)
        self.ui.twFichas.setColumnWidth(3, 60)
        rownum = 0
        for fic in fichas:
            self.ui.twFichas.insertRow(rownum)
            self.ui.twFichas.setItem(rownum, 0, QtGui.QTableWidgetItem(fic['Pedido']))
            self.ui.twFichas.setItem(rownum, 1, QtGui.QTableWidgetItem(fic['Cliente']))
            self.ui.twFichas.setItem(rownum, 2, QtGui.QTableWidgetItem(fic['Etiqueta']))
            self.ui.twFichas.setItem(rownum, 3, QtGui.QTableWidgetItem(fic['Maquina']))
            rownum =+ 1
        self.filtroConsulta = 0

    def mostrarFichasPedido(self):
        "se cargan las fichas del pedido seleccionado"
        fichas = DAO.FichaTecnica().recuperarFichaTecnica(self.ui.cmbBusqueda.currentText())
        self.ui.twFichas.setColumnCount(4)
        self.ui.twFichas.setHorizontalHeaderLabels(["Pedido", "Cliente", "Etiqueta","Maquina"])
        self.ui.twFichas.setColumnWidth(0, 60)
        self.ui.twFichas.setColumnWidth(1, 200)
        self.ui.twFichas.setColumnWidth(2, 200)
        self.ui.twFichas.setColumnWidth(3, 60)
        self.ui.twFichas.hideColumn(0)
        rownum = 0

        for fic in fichas:
            self.ui.twFichas.insertRow(rownum)
            self.ui.twFichas.setItem(rownum, 0, QtGui.QTableWidgetItem(fic['Pedido']))
            self.ui.twFichas.setItem(rownum, 1, QtGui.QTableWidgetItem(fic['Cliente']))
            self.ui.twFichas.setItem(rownum, 2, QtGui.QTableWidgetItem(fic['Etiqueta']))
            self.ui.twFichas.setItem(rownum, 3, QtGui.QTableWidgetItem(fic['Maquina']))
            rownum = + 1
        self.filtroConsulta = 1

    def mostrarFichasEtiqueta(self):
        "se cargan las fichas de la etiqueta seleccionada"
        fichas = DAO.FichaTecnica().recuperarFichaTecnicaEtiqueta(self.ui.cmbBusqueda.currentText())
        self.ui.twFichas.setColumnCount(4)
        self.ui.twFichas.setHorizontalHeaderLabels(["Pedido", "Cliente","Etiqueta","Maquina"])
        self.ui.twFichas.hideColumn(2)
        self.ui.twFichas.setColumnWidth(0, 60)
        self.ui.twFichas.setColumnWidth(1, 200)
        self.ui.twFichas.setColumnWidth(2, 200)
        self.ui.twFichas.setColumnWidth(3, 60)
        rownum = 0
        for fic in fichas:
            self.ui.twFichas.insertRow(rownum)
            self.ui.twFichas.setItem(rownum, 0, QtGui.QTableWidgetItem(fic['Pedido']))
            self.ui.twFichas.setItem(rownum, 1, QtGui.QTableWidgetItem(fic['Cliente']))
            self.ui.twFichas.setItem(rownum, 2, QtGui.QTableWidgetItem(fic['Etiqueta']))
            self.ui.twFichas.setItem(rownum, 3, QtGui.QTableWidgetItem(fic['Maquina']))

            rownum = + 1
        self.filtroConsulta = 2

    def mostrarFichasCliente(self):
        "se cargan las fichas del cliente seleccionado"
        fichas = DAO.FichaTecnica().recuperarFichaTecnicaCliente(self.ui.cmbBusqueda.currentText())
        self.ui.twFichas.setColumnCount(4)
        self.ui.twFichas.hideColumn(1)
        self.ui.twFichas.setHorizontalHeaderLabels(["Pedido","Cliente", "Etiqueta","Maquina"])
        self.ui.twFichas.setColumnWidth(0, 60)
        self.ui.twFichas.setColumnWidth(1, 200)
        self.ui.twFichas.setColumnWidth(2, 200)
        self.ui.twFichas.setColumnWidth(3, 60)
        rownum = 0
        for fic in fichas:
            self.ui.twFichas.insertRow(rownum)
            self.ui.twFichas.setItem(rownum, 0, QtGui.QTableWidgetItem(fic['Pedido']))
            self.ui.twFichas.setItem(rownum, 1, QtGui.QTableWidgetItem(fic['Cliente']))
            self.ui.twFichas.setItem(rownum, 2, QtGui.QTableWidgetItem(fic['Etiqueta']))
            self.ui.twFichas.setItem(rownum, 3, QtGui.QTableWidgetItem(fic['Maquina']))
            rownum = + 1
        self.filtroConsulta = 3

    def cmbBusqueda_indexChange(self):
        "se genera la carga al cambiar el indice"
        self.limpiarTabla()
        if (self.ui.cmbBusqueda.currentIndex() > 0):
            self.tipoFiltro[self.filtroSeleccionado]()

    def generarInforme(self):
        "se genera el informe de la ficha seleccionada"
        datos = self.ui.twFichas.selectedItems()

        if self.ui.twFichas.rowCount() != 0:
            ccount = self.ui.twFichas.columnCount()
            if self.ui.twFichas.rowCount() != 0:
                ccount = self.ui.twFichas.columnCount()
                if self.filtroConsulta == 0:
                    pedido = str(datos[0].text())
                    fichaBuscar = DTO.FichaTecnica()
                    fichaBuscar.setPedido(pedido)
                    fichaBuscar.setEtiqueta(datos[2].text())
                    maq = DTO.Maquina()
                    maq.setCodigo(str(datos[3].text()))
                    maquinaBuscar = DAO.Maquina(maq)
                    maquinaBuscar.leerMaquina()
                    fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                    ficha = DAO.FichaTecnica(fichaBuscar)

                    pass
                elif self.filtroConsulta == 1:
                    pedido = str(self.ui.cmbBusqueda.currentText())
                    fichaBuscar = DTO.FichaTecnica()
                    fichaBuscar.setPedido(pedido)
                    fichaBuscar.setEtiqueta(datos[1].text())
                    maq = DTO.Maquina()
                    maq.setCodigo(str(datos[2].text()))
                    maquinaBuscar = DAO.Maquina(maq)
                    maquinaBuscar.leerMaquina()
                    fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                    ficha = DAO.FichaTecnica(fichaBuscar)

                elif self.filtroConsulta == 2:
                    pedido = str(datos[0].text())
                    fichaBuscar = DTO.FichaTecnica()
                    fichaBuscar.setPedido(pedido)
                    fichaBuscar.setEtiqueta(self.ui.cmbBusqueda.currentText())
                    maq = DTO.Maquina()
                    maq.setCodigo(str(datos[2].text()))
                    maquinaBuscar = DAO.Maquina(maq)
                    maquinaBuscar.leerMaquina()
                    fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                    ficha = DAO.FichaTecnica(fichaBuscar)

                    pass
                elif self.filtroConsulta == 3:
                    pedido = str(datos[0].text())
                    fichaBuscar = DTO.FichaTecnica()
                    fichaBuscar.setPedido(pedido)
                    fichaBuscar.setEtiqueta(datos[1].text())
                    maq = DTO.Maquina()
                    maq.setCodigo(str(datos[2].text()))
                    maquinaBuscar = DAO.Maquina(maq)
                    maquinaBuscar.leerMaquina()
                    fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                    ficha = DAO.FichaTecnica(fichaBuscar)

                ficha.leerFichaTecnicaPedMaq()
                "Escribir Datos de la Ficha"
                buscarMaquina = DTO.Maquina()
                buscarMaquina.setIdMaquina(ficha.getFichaTecnica().getIdMaquina())
                maquina = DAO.Maquina(buscarMaquina)

                maquina.leerMaquinaId()

                listaMateriales = DAO.MaterialFicha().leerMaterialesEnFicha(
                    ficha.getFichaTecnica().getIdFicha())
                listaConMateriales = list()

                for indice in listaMateriales:
                    material = DTO.Material()
                    material.setIdMaterial(indice)
                    buscarMaterial = DAO.Material(material)
                    buscarMaterial.leerMaterialPorId()
                    listaConMateriales.append(buscarMaterial.getMaterial())

                "Escribir mallas de la ficha"
                listaMallas = DAO.MallaFicha().leerMallaEnFicha(
                    ficha.getFichaTecnica().getIdFicha())
                listaConMallas = list()
                for indice in listaMallas:
                    malla = DTO.Malla()
                    malla.setIdMalla(indice)
                    buscarMalla = DAO.Malla(malla)
                    buscarMalla.leerMalla()
                    listaConMallas.append(buscarMalla.getMalla())

                "Escribir Tintas de la ficha"

                listaTintas = DAO.TintaFicha().leerTintaEnFicha(
                    ficha.getFichaTecnica().getIdFicha())
                listaConTintas = list()
                for indice in listaTintas:
                    tinta = DTO.Tinta()
                    tinta.setIdTinta(indice)
                    buscarTinta = DAO.Tinta(tinta)
                    buscarTinta.leerTinta()
                    listaConTintas.append(buscarTinta.getTinta())

                "Escribir Adhesivo de laminacion"

                listaAdhLaminacion = DAO.AdhLamFicha().leerAdhLamFicha(
                    ficha.getFichaTecnica().getIdFicha())

                listaConAdhLam = list()
                for indice in listaAdhLaminacion:
                    adhlam = DTO.AdhesivoLaminacion()
                    adhlam.setAdhLam(indice)
                    buscarAdhLam = DAO.AdhesivoLaminacion(adhlam)
                    buscarAdhLam.leerAdhLam()
                    listaConAdhLam.append(buscarAdhLam.getAdhlam())

                "Escribir Adhesivo Cold Foil"

                listaAdhColdFoil = DAO.AdhCoFoFicha().leerAdhCoFoEnFicha(
                    ficha.getFichaTecnica().getIdFicha())

                listaConAdhColdFoil = list()
                for indice in listaAdhColdFoil:
                    adhcofo = DTO.AdhesivoColdFoil()
                    adhcofo.setIdAdhCoFo(indice)
                    buscarAdhCofo = DAO.AdhesivoColdFoil(adhcofo)
                    buscarAdhCofo.leerAdhCoFo()
                    listaConAdhColdFoil.append(buscarAdhCofo.getAdhCoFo())

                "Escribir Film Micronaje"

                listaFilmi = DAO.FilmMiFicha().leerFilmMiEnFicha(
                    ficha.getFichaTecnica().getIdFicha())

                listaConFilmMi = list()
                for indice in listaFilmi:
                    filmmi = DTO.FilmMicronaje()
                    filmmi.setIdFilmMi(indice)
                    buscarFilmMi = DAO.FilmMicronaje(filmmi)
                    buscarFilmMi.leerFilmMi()
                    listaConFilmMi.append(buscarFilmMi.getFilmMi())

                "Escribir Cold Foil"

                listaColdFoil = DAO.ColdFoilFicha().leerColdFoilEnFicha(
                    ficha.getFichaTecnica().getIdFicha())
                listaConColdFoil = list()
                for indice in listaColdFoil:
                    coldfoil = DTO.ColdFoil()
                    coldfoil.setIdColdFoil(indice)
                    buscarColdFoil = DAO.ColdFoil(coldfoil)
                    buscarColdFoil.leerColdFoil()
                    listaConColdFoil.append(buscarColdFoil.getColdFoil())

                "Escribir Tipo Barniz"
                listaTBarniz = DAO.TBarnizFicha().leerTBarnizEnFicha(
                    ficha.getFichaTecnica().getIdFicha())

                listaConTBarniz = list()
                for indice in listaTBarniz:
                    tbarniz = DTO.TipoBarniz()
                    tbarniz.setIdTBarniz(indice)
                    buscarTBarniz = DAO.TipoBarniz(tbarniz)
                    buscarTBarniz.leerTBarniz()
                    listaConTBarniz.append(buscarTBarniz.getTBarniz())

                "Escribir Troquel"
                listaTroquel = DAO.TroquelFicha().leerTroquelEnFicha(
                    ficha.getFichaTecnica().getIdFicha())

                listaConTroquel = list()
                for indice in listaTroquel:
                    troquel = DTO.Troquel()
                    troquel.setIdTroquel(indice)
                    buscarTroquel = DAO.Troquel(troquel)
                    buscarTroquel.leerTroquel()
                    listaConTroquel.append(buscarTroquel.getTroquel())


                GeneradorPdfAdmin.FormatoInformePDF(ficha.getFichaTecnica(),maquina.getMaquina(),listaConMateriales,listaConMallas,
                                                   listaConTintas,listaConAdhLam,listaConAdhColdFoil,
                                                   listaConFilmMi,listaConColdFoil,
                                                   listaConTBarniz,listaConTroquel)
            else:
                MostrarMensaje("Debe seleccionar el numero de fila, para poder mostrar la ficha")
        else:
            MostrarMensaje("No existen registros que mostrar")

    def limpiarTabla(self):
        "limpia los datos de la tabla"
        self.ui.twFichas.setColumnCount(0)
        self.ui.twFichas.setRowCount(0)

    def estadoceroconsulta(self):

        self.ui.cmbBusqueda.clear()
        self.ui.cmbBusqueda.addItem("Seleccione filtro")
        self.limpiarTabla()

        self.ui.rbEtiqueta.setAutoExclusive(False)
        self.ui.rbPedidos.setAutoExclusive(False)
        self.ui.rbCliente.setAutoExclusive(False)
        self.ui.rbCategoria.setAutoExclusive(False)

        self.ui.rbEtiqueta.setChecked(False)
        self.ui.rbPedidos.setChecked(False)
        self.ui.rbCliente.setChecked(False)
        self.ui.rbCategoria.setChecked(False)

        self.ui.rbEtiqueta.setAutoExclusive(True)
        self.ui.rbPedidos.setAutoExclusive(True)
        self.ui.rbCliente.setAutoExclusive(True)
        self.ui.rbCategoria.setAutoExclusive(True)

    "Operaciones dentro de la Creacion de fichas"
    def pbguardarficha_click(self):
        try:

            "Se lee la categoria"
            categoriaBuscar = DTO.Categoria()
            categoriaBuscar.setNombre(str(self.ui.cmbCategoria.currentText()))
            categoriaBuscada = DAO.Categoria(categoriaBuscar)
            categoriaBuscada.leerCategoria()


            "Sel lee el cliente cliente"
            clienteBuscar = DTO.Cliente()
            clienteBuscar.setNombre(str(self.ui.cmbCliente.currentText()))
            clienteBuscado = DAO.Cliente(clienteBuscar)
            clienteBuscado.leerClienteNombre()

            "Se lee la maquina"
            maquinaBuscar = DTO.Maquina()
            maquinaBuscar.setCodigo(str(self.ui.cmbMaquina.currentText()))
            maquinaBuscada = DAO.Maquina(maquinaBuscar)
            maquinaBuscada.leerMaquina()


            fichaTecnica = DTO.FichaTecnica()
            fichaTecnica.setPedido(str(self.ui.lePedido.text()))
            fichaTecnica.setEtiqueta(str(self.ui.leEtiqueta.text()))
            fichaTecnica.setFecha(str(self.ui.deFechaFicha.date().toString("dd/MM/yyyy")))
            fichaTecnica.setVelocidad(float(self.ui.dsbVelocidadFicha.value()))
            fichaTecnica.setIdCategoria(categoriaBuscada.getCategoria().getIdCategoria())
            fichaTecnica.setIdCliente(clienteBuscado.getCliente().getIdCliente())
            fichaTecnica.setIdMaquina(maquinaBuscada.getMaquina().getIdMaquina())
            if self.ui.rbConvencionales.isChecked():
                fichaTecnica.setClisse(True)
            else:
                fichaTecnica.setClisse(False)
            insertarFicha = DAO.FichaTecnica(fichaTecnica)

            if (insertarFicha.insertarFichaTecnica()):
                MostrarMensaje("La ficha a sido agregada exitosamente")
                vAgregar = agregarCaracteristicas.Vagregarcaracteristicas()
                ficha = DAO.FichaTecnica()
                ficha.getFichaTecnica().setIdFicha(DAO.FichaTecnica().idUltimaFicha())
                ficha.leerFichaTecnicaidFicha()
                vAgregar.cargarFichaModificar(ficha)

                vAgregar.exec_()
            else:
                MostrarError("La ficha no se pudo agregar")



        except Exception as e:
            MostrarError(str(e.message))
        else:

            self.limpiarFFichaTecnica()
            pass

    def pbModificarFicha_click(self):
        datos = self.ui.twFichas.selectedItems()

        if self.ui.twFichas.rowCount() != 0:
            ccount = self.ui.twFichas.columnCount()
            if self.filtroConsulta == 0:
                pedido = str(datos[0].text())
                fichaBuscar = DTO.FichaTecnica()
                fichaBuscar.setPedido(pedido)
                fichaBuscar.setEtiqueta(str(datos[2].text()))
                maq = DTO.Maquina()
                maq.setCodigo(str(datos[3].text()))
                maquinaBuscar = DAO.Maquina(maq)
                maquinaBuscar.leerMaquina()
                fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                ficha = DAO.FichaTecnica(fichaBuscar)

                pass
            elif self.filtroConsulta == 1:
                pedido = str(self.ui.cmbBusqueda.currentText())
                fichaBuscar = DTO.FichaTecnica()
                fichaBuscar.setPedido(pedido)
                fichaBuscar.setEtiqueta(str(datos[1].text()))
                maq = DTO.Maquina()
                maq.setCodigo(str(datos[2].text()))
                maquinaBuscar = DAO.Maquina(maq)
                maquinaBuscar.leerMaquina()
                fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                ficha = DAO.FichaTecnica(fichaBuscar)

            elif self.filtroConsulta == 2:
                pedido = str(datos[0].text())
                fichaBuscar = DTO.FichaTecnica()
                fichaBuscar.setPedido(pedido)
                fichaBuscar.setEtiqueta(self.ui.cmbBusqueda.currentText())
                maq = DTO.Maquina()
                maq.setCodigo(str(datos[2].text()))
                maquinaBuscar = DAO.Maquina(maq)
                maquinaBuscar.leerMaquina()
                fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                ficha = DAO.FichaTecnica(fichaBuscar)

                pass
            elif self.filtroConsulta == 3:
                pedido = str(datos[0].text())
                fichaBuscar = DTO.FichaTecnica()
                fichaBuscar.setPedido(pedido)
                fichaBuscar.setEtiqueta(str(datos[1].text()))
                maq = DTO.Maquina()
                maq.setCodigo(str(datos[2].text()))
                maquinaBuscar = DAO.Maquina(maq)
                maquinaBuscar.leerMaquina()
                fichaBuscar.setIdMaquina(maquinaBuscar.getMaquina().getIdMaquina())
                ficha = DAO.FichaTecnica(fichaBuscar)


            ficha.leerFichaTecnicaPedMaq()
            vMod = modificarFichaCB.Vmodificarficha()
            vMod.cargarFichaModificar(ficha)
            vMod.exec_()
            self.ui.twFichas.setRowCount(0)
            self.tipoFiltro[self.filtroSeleccionado]()



    def limpiarFFichaTecnica(self):
        self.ui.lePedido.setText("")
        self.ui.leEtiqueta.setText("")
        self.ui.dsbVelocidadFicha.setValue(float(0))
        self.ui.deFechaFicha.setDate(datetime.date.today())
        self.ui.rbConvencionales.setChecked(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = VgestionFichas()
    myWindow.show()
    reload(sys)
    sys.setdefaultencoding('cp1252')
    sys.exit(app.exec_())
