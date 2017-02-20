import sys
from PyQt4 import QtCore, QtGui, QtSql
from Formularios import ModuloConsultas
from FormulariosCB import editarClienteCB,editarMaterialCB, editarTintaCB, editarMallaCB, editarAdhLamCB
from FormulariosCB import editarAdhCoFoCB, editarFilmiCB, editarColdFoilCB, editarTroquelCB, editarTBarnizCB
from Clases import DTO, DAO, GeneradorPdf
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
class VConsultas(QtGui.QDialog):

    def __init__(self, parent = None):
        "Constructor de la ventana de gestion de fichas"
        QtGui.QWidget.__init__(self,parent)
        self.ui = ModuloConsultas.Ui_Dialog()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint
        self.setWindowFlags(flags)
        self.setWindowTitle("Gestion de fichas tecnicas para etiquetas")

        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        Conexion(self.db)

        self.estadoceroconsulta()

        self.ui.twFichas.setColumnWidth(0,100)
        self.ui.twFichas.setColumnWidth(1, 100)
        self.ui.twFichas.setColumnWidth(2, 100)
        self.ui.twFichas.setColumnWidth(3, 100)

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
        self.ui.twFichas.hideColumn(0)
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
            if self.filtroConsulta != 0:
                ccount = ccount -1
            if len(datos) == ccount:
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
                    ficha.leerFichaTecnicaPedMaq()
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
                    ficha.leerFichaTecnicaPedMaq()
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
                    ficha.leerFichaTecnicaPedMaq()
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


                GeneradorPdf.FormatoInformePDF(ficha.getFichaTecnica(),maquina.getMaquina(),listaConMateriales,listaConMallas,
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



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = VConsultas()
    myWindow.show()
    reload(sys)
    sys.setdefaultencoding('cp1252')
    sys.exit(app.exec_())
