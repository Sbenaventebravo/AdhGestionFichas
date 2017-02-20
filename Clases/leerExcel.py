# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import DTO, DAO

import datetime


def agregarFichadesdeExcel(archivo,idCategoria,idCliente):
    nombre_archivo = u'{0}'.format(archivo) + '.xlsx'
    wb = load_workbook(filename=nombre_archivo)
    sheet = wb.get_sheet_by_name(u'Hoja1')
    "Construccion de Datos de la ficha"
    ficha = DTO.FichaTecnica()
    ficha.setEtiqueta(str(sheet['B2'].value).decode(encoding= "cp1252"))
    if sheet['B3'].value == None:
        pedido = "SIN PEDIDO"
    else:
        pedido = str(sheet['B3'].value)
    ficha.setPedido(pedido)
    fecha = sheet['G2'].value.strftime("%d/%m/%Y")
    ficha.setFecha(fecha)
    velocidad = float(sheet['F40'].value)
    ficha.setVelocidad(velocidad)
    clisse = False
    if sheet['C40'].value != None:
        clisse = True
    ficha.setClisse(clisse)
    maquina = str(sheet['G3'].value).decode(encoding= "cp1252")
    maquinaReal = DTO.Maquina()
    maquinaReal.setCodigo(maquina)
    maquinaReal = DAO.Maquina(maquinaReal)
    maquinaReal.leerMaquina()
    ficha.setIdMaquina(maquinaReal.getMaquina().getIdMaquina())
    ficha.setIdCliente(idCliente)
    ficha.setIdCategoria(idCategoria)
    "Generar lista de materiales"
    listaMateriales = list()
    for i in range(6, 9):
        material = DTO.Material()
        if sheet['A{0}'.format(i)].value == None or sheet['B{0}'.format(i)].value == None:
            break
        else:
            material.setNombre(str(sheet['A{0}'.format(i)].value).decode(encoding= "cp1252"))
            material.setCodigo(str(sheet['B{0}'.format(i)].value).decode(encoding= "cp1252"))
            material.setProveedor(str(sheet['C{0}'.format(i)].value).decode(encoding= "cp1252"))
            material.setAncho(float(sheet['D{0}'.format(i)].value))
            tc = False
            if (sheet['E6'].value == 'SI' or sheet['E6'].value == 'si' or sheet['E6'].value == 'Si'):
                tc = True
            material.setTC(tc)

            listaMateriales.append(material)
    "Generar lista de tintas"
    listaTintas = list()
    for i in range(15, 23):
        if sheet['B{0}'.format(i)].value == None:
            break
        else:
            tinta = DTO.Tinta()
            tinta.setColor(str(sheet['B{0}'.format(i)].value).decode(encoding= "cp1252"))
            tinta.setTipo(str(sheet['C{0}'.format(i)].value).decode(encoding= "cp1252"))
            tinta.setAnilox(str(sheet['D{0}'.format(i)].value).decode(encoding= "cp1252"))
            tinta.setProveedor1(str(sheet['E{0}'.format(i)].value).decode(encoding= "cp1252"))
            tinta.setProveedor2(str(sheet['F{0}'.format(i)].value).decode(encoding= "cp1252"))
            tinta.setProveedor3(str(sheet['G{0}'.format(i)].value).decode(encoding= "cp1252"))
            listaTintas.append(tinta)
    "generar lista de mallas"
    listaMallas = list()
    for i in range(11, 13):
        if sheet['B{0}'.format(i)].value == None:
            break
        else:
            malla = DTO.Malla()
            malla.setTipo(str(sheet['B{0}'.format(i)].value))
            interno = False
            if str(sheet['C{0}'.format(i)].value) == None:
                interno = True

            malla.setInterno(interno)

            listaMallas.append(malla)

        pass
    "generar lista de adhesivos lam"
    listaadlam = list()
    for i in range(25, 27):
        if str(sheet['A{0}'.format(i)].value) == "NO" or sheet['A{0}'.format(i)].value == None :
            break
        else:
            adlam = DTO.AdhesivoLaminacion()
            adlam.setProveedor(str(sheet['B{0}'.format(i)].value))
            adlam.setAnilox(str(sheet['C{0}'.format(i)].value))
            listaadlam.append(adlam)
        pass
    "generar lista de adhesivos cold foil"
    listaadcofo = list()
    for i in range(29, 31):
        if str(sheet['A{0}'.format(i)].value) == "NO" or sheet['A{0}'.format(i)].value == None :
            break
        else:
            adcofo = DTO.AdhesivoColdFoil()
            adcofo.setProveedor(str(sheet['B{0}'.format(i)].value))
            adcofo.setAnilox(str(sheet['C{0}'.format(i)].value))
            listaadcofo.append(adcofo)
        pass
    "generar lista de films de micronaje"
    listafilmi = list()
    for i in range(25, 27):
        if str(sheet['E{0}'.format(i)].value) == "NO" or sheet['E{0}'.format(i)].value == None \
                or str(sheet['E{0}'.format(i)].value) == "no":
            break;
        else:
            filmi = DTO.FilmMicronaje()
            proveedor = str(sheet['E{0}'.format(i)].value) + " " + str(sheet['F{0}'.format(i)].value)
            filmi.setProveedor(proveedor)
            filmi.setAncho(float(sheet['G{0}'.format(i)].value))
            listafilmi.append(filmi)

        pass
    "generar lista de cold foil"
    listacoldfoil = list()
    for i in range(29, 31):
        if str(sheet['E{0}'.format(i)].value) == "NO" or sheet['E{0}'.format(i)].value == None or \
                        sheet['F{0}'.format(i)].value == None or str(sheet['E{0}'.format(i)].value) == "no":
            break;
        else:
            coldfoil = DTO.ColdFoil()
            proveedor = str(sheet['F{0}'.format(i)].value)
            coldfoil.setProveedor(proveedor)
            coldfoil.setAncho(float(sheet['G{0}'.format(i)].value))
            listacoldfoil.append(coldfoil)

        pass
        pass
    "generar lista de tipos de barniz"
    listatbarniz = list()
    for i in range(33, 38):
        if str(sheet['E{0}'.format(i)].value) == "NO" or sheet['E{0}'.format(i)].value == None:
            break
        else:
            tbarniz = DTO.TipoBarniz()
            tbarniz.setTipo(str(sheet['E{0}'.format(i)].value))
            tbarniz.setProveedor(str(sheet['F{0}'.format(i)].value))
            tbarniz.setAnilox(str(sheet['G{0}'.format(i)].value))
            listatbarniz.append(tbarniz)
        pass
    "generar lista de troquel"
    listatroquel = list()
    for i in range(33, 38):
        if str(sheet['A{0}'.format(i)].value) == "NO" or sheet['A{0}'.format(i)].value == None:
            break
        else:
            troquel = DTO.Troquel()

            proveedor = str(sheet['B{0}'.format(i)].value)
            troquel.setProveedor(proveedor)
            observacion = ""
            if sheet['A{0}'.format(i)].value != None:
                observacion += str(sheet['A{0}'.format(i)].value)
            if sheet['C{0}'.format(i)].value != None :
                if str(sheet['C{0}'.format(i)].value).find('/') != -1:
                    observacion += " " + sheet['C{0}'.format(i)].value.strftime("%d/%m/%Y")
                else:
                    observacion += " " + str(sheet['C{0}'.format(i)].value)
            if len(observacion) == 0:
                observacion = "SIN OBSERVACION"
            troquel.setObservacion(observacion)
            listatroquel.append(troquel)
        pass
    if (DAO.FichaTecnica(ficha).insertarFichaTecnica()):
        pass
    else:
        pass
    ficha = DAO.FichaTecnica()
    ultimoId = DAO.FichaTecnica().idUltimaFicha()
    ficha.getFichaTecnica().setIdFicha(ultimoId)
    ficha.leerFichaTecnicaidFicha()
    for mat in listaMateriales:
        if (DAO.Material(mat).insertarMaterial()):
            pass
            referencia = DAO.MaterialFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdMaterial(DAO.Material().idUltimoMaterialInsertada())
            referencia.insertarMaterialFicha()
        else:
            pass
    for tinta in listaTintas:
        if (DAO.Tinta(tinta).ingresarTinta()):
            pass
            referencia = DAO.TintaFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdTinta(DAO.Tinta().idUltimaTinta())
            referencia.insertarTintaFicha()
        else:
            pass
    for malla in listaMallas:
        if (DAO.Malla(malla).ingresarMalla()):
            pass
            referencia = DAO.MallaFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdMalla(DAO.Malla().idUltimaMallaInsertada())
            referencia.insertarMallaFicha()
        else:
            pass
    for adlam in listaadlam:
        if (DAO.AdhesivoLaminacion(adlam).ingresarAdhLam()):
            pass
            referencia = DAO.AdhLamFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdAdhLam(DAO.AdhesivoLaminacion().idUltimoAdhLam())
            referencia.insertarAdhLamFicha()
        else:
            pass
    for adcofo in listaadcofo:
        if (DAO.AdhesivoColdFoil(adcofo).ingresarAdhCoFo()):
            pass
            referencia = DAO.AdhCoFoFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdAdhCoFo(DAO.AdhesivoColdFoil().idUltimoAdhCoFo())
            referencia.insertarAdhCoFoFicha()
        else:
            pass
    for filmi in listafilmi:
        if (DAO.FilmMicronaje(filmi).ingresarFilmMi()):
            pass
            referencia = DAO.FilmMiFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdFilmMi(DAO.FilmMicronaje().idUltimoFilmMi())
            referencia.insertarFilmMiFicha()
        else:
            pass
    for coldfoil in listacoldfoil:
        if (DAO.ColdFoil(coldfoil).ingresarColdFoil()):
            pass
            referencia = DAO.ColdFoilFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdColdFoil(DAO.ColdFoil().idUltimoColdFoil())
            referencia.insertarColdFoilFicha()
        else:
            pass
    for tbarniz in listatbarniz:
        if (DAO.TipoBarniz(tbarniz).ingresarTBarniz()):
            pass
            referencia = DAO.TBarnizFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdTBarniz(DAO.TipoBarniz().idUltimoTBarniz())
            referencia.insertarTBarnizFicha()
        else:
            pass
    for troquel in listatroquel:
        if (DAO.Troquel(troquel).ingresarTroquel()):
            pass
            referencia = DAO.TroquelFicha()
            referencia.setIdFicha(ficha.getFichaTecnica().getIdFicha())
            referencia.setIdTroquel(DAO.Troquel().idUltimoTroquel())
            referencia.insertarTroquelFicha()
        else:
            pass

"Aguas"

agregarFichadesdeExcel('AGUA DE LA MONTANA',2,1)
agregarFichadesdeExcel('AGUA MINERAL VITAL',2,1)
agregarFichadesdeExcel('AGUA TONIC DIUCO',2,1)


"Cesinas-Carnes"

agregarFichadesdeExcel('CARNES PAMPA VERDE',3,1)
agregarFichadesdeExcel('JAMON SERRANO PF',3,1)
agregarFichadesdeExcel('LONGANIZA CECINAS CHILLAN',3,1)
agregarFichadesdeExcel('PANCETA AHUMADA PF',3,1)
agregarFichadesdeExcel('PASTA DE SALAME PF',3,1)
agregarFichadesdeExcel('PATES MODINGER',3,1)
agregarFichadesdeExcel('SALAME AHUMADO LIDER',3,1)
agregarFichadesdeExcel('SALAME ARTESANAL RECETA DEL ABUELO',3,1)

"Cervezas"

agregarFichadesdeExcel('CERVEZA GUAYACAN STOUR',4,1)
agregarFichadesdeExcel('CERVEZA GUAYACAN UNO',4,1)
agregarFichadesdeExcel('CERVEZA KROSS 5 ANOS',4,1)
agregarFichadesdeExcel('CERVEZA KROSS GOLDEN',4,1)

"Espumantes"

agregarFichadesdeExcel('ESPUMANTE SENSUS',5,1)

"Jugos"

agregarFichadesdeExcel('JUGO A CUENTA MIX',6,1)
agregarFichadesdeExcel('JUGO DE LIMON TRAVERSO',6,1)
agregarFichadesdeExcel('JUGOS FRUGO',6,1)
agregarFichadesdeExcel('JUGOS WATTS',6,1)

"Licores"

agregarFichadesdeExcel('BRANDY DOMECQ',7,1)

"Limpiadores"

agregarFichadesdeExcel('CERA AUTOBRILLO VIRGINIA',8,1)
agregarFichadesdeExcel('LAVALOZAS FULL',8,1)
agregarFichadesdeExcel('LAVALOZAS VALOR 2 LITROS',8,1)
agregarFichadesdeExcel('LIMPIADOR LONGLASTING VIRGINIA',8,1)
agregarFichadesdeExcel('LIMPIAPISOS FULL PRIMAVERA',8,1)
agregarFichadesdeExcel('LIMPIAPISOS VALOR PRIMAVERA',8,1)
agregarFichadesdeExcel('LUSTRAMUEBLES VIRGINIA NUEVO DISENO LAVANDA',8,1)

"MANTEQUILLAS-MERMELADAS"

agregarFichadesdeExcel('MANTEQUILLA NEXT',9,1)
agregarFichadesdeExcel('MANTEQUILLAS SURENA',9,1)
agregarFichadesdeExcel('MARGARINA SOPROLE LIGHT TAPA',9,1)
agregarFichadesdeExcel('MARGARINA SOPROLE MIX',9,1)
agregarFichadesdeExcel('MARGARINA SOPROLE TAPA',9,1)
agregarFichadesdeExcel('MARGARINA SURENA STANDARD POTE KILO',9,1)
agregarFichadesdeExcel('MARGARINA SURENA STANDARD TAPA',9,1)
agregarFichadesdeExcel('MERMELADAS REGIMEL',9,1)
agregarFichadesdeExcel('MERMELADAS WATTS',9,1)

"PISCOS"

agregarFichadesdeExcel('PISCO ALTO DEL CARMEN',10,1)
agregarFichadesdeExcel('PISCO ARTESANOS COCHIGUAZ',10,1)
agregarFichadesdeExcel('PISCO LA SERENA',10,1)
agregarFichadesdeExcel('PISCO MISTRAL ESPECIAL (AZUL)',10,1)
agregarFichadesdeExcel('PISCO MISTRAL ICE',10,1)
agregarFichadesdeExcel('PISCO MISTRAL NOBEL 40',10,1)
agregarFichadesdeExcel('PISCO MISTRAL NOBEL 46',10,1)
agregarFichadesdeExcel('PISCO TRES ERRES MOAI',10,1)


"QUESOS"

agregarFichadesdeExcel('QUESO BRIE QUILLAYES',11,1)


"RON"

agregarFichadesdeExcel('RON CABO VIEJO',12,1)
agregarFichadesdeExcel('RON DIPLOMATICO BOTUCAL',12,1)
agregarFichadesdeExcel('RON DORADO PACIFICO',12,1)
agregarFichadesdeExcel('RON MEDELLIN',12,1)
agregarFichadesdeExcel('RON MOJITO ICE GINGER',12,1)
agregarFichadesdeExcel('RON SIERRA MORENA',12,1)


"Talcos"

agregarFichadesdeExcel('TALCO BROOKS 42 K COBRE',13,1)
agregarFichadesdeExcel('TALCO BROOKS SILVERTECK 80',13,1)
agregarFichadesdeExcel('TALCO BROOKS SILVERTECK 220',13,1)
agregarFichadesdeExcel('TALCO BROOKS ZAPATILLAS',13,1)

"Vodka"

agregarFichadesdeExcel('VODKA ERISTOFF INFERIOR',14,1)
agregarFichadesdeExcel('VODKA ERISTOFF',14,1)






