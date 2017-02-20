# -*- coding: iso-8859-2 -*-
import os

#Importamos algunas librerias: SimpleDocTemplate, es una plantilla de documento
#predefinida; getSampleStyleSheet, contiene una hoja de estilos de ejemplo;
#inch es una pulgada

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import datetime
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

from reportlab.lib.units import inch


class MCLine(Flowable):
    """
    Line flowable --- draws a line in a flowable
    http://two.pairlist.net/pipermail/reportlab-users/2005-February/003695.html
    """

    # ----------------------------------------------------------------------
    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    # ----------------------------------------------------------------------
    def __repr__(self):
        return "Line(w=%s)" % self.width

    # ----------------------------------------------------------------------
    def draw(self):
        """
        draw the line
        """
        self.canv.line(0, self.height, self.width, self.height)
PAGE_WIDTH = letter[0]
PAGE_HEIGHT = letter[1]

styles = getSampleStyleSheet()

#Definimos las caracteristicas fijas de la primera página
def myFirstPage(canvas, doc):
    canvas.saveState()
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
             9: 'Septiembre',
             10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    hoy = datetime.date.today()
    logo = ImageReader('Informe.jpg')

    canvas.setLineWidth(.3)

    canvas.setFont('Helvetica', 12)
    canvas.drawImage(logo, 50, 775, width=100, height=100, mask="transparent", preserveAspectRatio=True, anchor='c')
    canvas.drawString(30, 800, 'FICHA TECNICA DE ETIQUETA')
    canvas.drawString(30, 780, 'ADHESOL LTDA.')
    canvas.drawString(470, 800, str(hoy.day) + " de " + meses[hoy.month] + ", " + str(hoy.year))
    canvas.restoreState()

#Definimos disposiciones alternas para las caracteristicas de las otras páginas
def myLaterPages(canvas, doc):
    canvas.saveState()
    logo = ImageReader('Informe.jpg')
    canvas.drawImage(logo, 50, 775, width=100, height=100, mask="transparent", preserveAspectRatio=True, anchor='c')
    canvas.setFont('Helvetica', 9)
    canvas.restoreState()

def FormatoInformePDF(ficha,maquina,listaMateriales,listaMallas,listaTintas,listaAdhLam,listaAdhCofo,listaFilmMi,
                      listaColdFoil, listaTBarniz, listaTroquel):
    Title = "Fichas Tecnicas"
    pageinfo = "Ficha Tecnica Etiquetas"
    #Creamos un documento basándonos en una plantilla
    doc = SimpleDocTemplate("VistaFicha.pdf")
    #Iniciamos el story para los registros
    story = [Spacer(0, 40)]
    estiloHoja = getSampleStyleSheet()
    #Definimos un estilo
    estilo = styles['Normal']
    cabezera = estiloHoja['Heading2']
    cuerpo = estiloHoja['BodyText']
    cabezeraSec = estiloHoja['Heading4']

    #Se añaden los datos de la ficha
    texto = "Descripcion de la Etiqueta:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezera)
    story.append(p)
    story.append(Spacer(0,5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0,5))

    "Agregar Informacion de la ficha"

    texto = "<u><strong>Fecha de la ficha:</strong></u>  {0}".format(ficha.getFecha().strftime("%d-%m-%Y"))
    p = Paragraph(texto.decode(encoding= "cp1252"),cuerpo)
    story.append(p)
    story.append(Spacer(0,3))
    texto = "<u><strong>Pedido:</strong></u>   {0}".format(ficha.getPedido())
    p = Paragraph(texto.decode(encoding= "cp1252"),cuerpo)
    story.append(p)
    story.append(Spacer(0,3))
    texto = "<u><strong>Etiqueta:</strong></u>   {0}".format(str(ficha.getEtiqueta()))
    p = Paragraph(texto.decode(encoding= "cp1252"),cuerpo)
    story.append(p)
    story.append(Spacer(0,3))
    clisse = "Convencionales"
    if ficha.getClisse() == False:
        clisse = "Digitales"
    texto = "<u><strong>Clisses:</strong></u>   {0}".format(clisse.upper())
    p = Paragraph(texto.decode(encoding= "cp1252"), cuerpo)
    story.append(p)
    story.append(Spacer(0, 3))
    texto = "<u><strong>Maquina:</strong></u>   {0}".format(maquina.getCodigo())
    p = Paragraph(texto.decode(encoding= "cp1252"),cuerpo)
    story.append(p)
    story.append(Spacer(0, 3))
    texto = "<u><strong>Velocidad Maquina(m/m):</strong></u>   {0}".format(ficha.getVelocidad())
    p = Paragraph(texto.decode(encoding= "cp1252"), cuerpo)
    story.append(p)
    story.append(Spacer(0,10))
    "Agregar informacion de los materiales de la ficha"
    texto = "Materiales:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))

    dataMateriales = [['Codigo','Nombre','Proveedor','Ancho','TC']]
    for material in listaMateriales:
        dataMateriales.append(material.listaMaterial())
    t = Table(dataMateriales,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])
    story.append(t)
    story.append(Spacer(0,10))

    "Agregar la informacion de las mallas en las fichas"
    texto = "Mallas:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))
    dataMallas = [['Tipo','Externa o Interna']]
    if(len(listaMallas) != 0):

        for malla in listaMallas:
            dataMallas.append(malla.listaMalla())
        t = Table(dataMallas,style = [
                           ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                           ('BOX',(0,0),(-1,-1),2,colors.black),
                           ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                           ])

        story.append(t)
        story.append(Spacer(0, 10))
    else:
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))


    "Agregar la informacion de las tintas en las fichas"
    texto = "Tintas:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))

    dataTintas = [['Color','Tipo','Anilox','Proveedor 1', 'Proveedor 2', 'Proveedor 3']]
    for tinta in listaTintas:
        dataTintas.append(tinta.listaTinta())
    t = Table(dataTintas,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])

    story.append(t)
    story.append(Spacer(0,10))

    "Agregar la informacion de los adhesivos de laminacion en las fichas"
    texto = "Adhesivo Laminacion:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))
    if (len(listaAdhLam) == 0):
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))
    else:
        dataAdhLam =[['Proveedor','Anilox']]
        for adhlam in listaAdhLam:
            dataAdhLam.append(adhlam.listaAdhLam())
        t = Table(dataAdhLam,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])

        story.append(t)
        story.append(Spacer(0,10))

    "Agregar la informacion de los adhesivos cold foil en las fichas"
    texto = "Adhesivo Cold Foil:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))
    if (len(listaAdhCofo) == 0):
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))
    else:

        dataAdhCofo = [['Proveedor','Anilox']]
        for adhcofo in listaAdhCofo:
            dataAdhCofo.append(adhcofo.listaAdhCoFo())

        t = Table(dataAdhCofo,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])

        story.append(t)
        story.append(Spacer(0,10))

    "Agregar la informacion de film micronaje en las fichas"
    texto = "Film Micronaje:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))
    if (len(listaFilmMi) == 0):
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))
    else:

        dataFilmMi = [['Proveedor','Ancho']]
        for filmmi in listaFilmMi:
            dataFilmMi.append(filmmi.listaFilmMi())
        t = Table(dataFilmMi,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])

        story.append(t)
        story.append(Spacer(0,10))

    "Agregar la informacion de los cold foil en las fichas"
    texto = "Cold Foil:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))
    if (len(listaColdFoil) == 0):
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))
    else:
        dataColdFoil = [['Proveedor','Ancho']]
        for coldfoil in listaColdFoil:
            dataColdFoil.append(coldfoil.listaColdFoil())
        t = Table(dataColdFoil,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])
        story.append(t)
        story.append(Spacer(0,10))

    texto = "Tipo de Barniz:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))

    "Agregar la informacion de los tipos de barniz en las fichas"
    if (len(listaTBarniz) == 0):
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))
    else:
        dataTBarniz = [['Tipo', 'Proveedor', 'Anilox']]
        for tbarniz in listaTBarniz:
            dataTBarniz.append(tbarniz.listaTBarniz())
        t = Table(dataTBarniz,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])

        story.append(t)
        story.append(Spacer(0,10))

    "Agregar la informacion de Troquel en las fichas"
    texto = "Troquel:"
    p = Paragraph(texto.decode(encoding= "cp1252"),cabezeraSec)
    story.append(p)
    story.append(Spacer(0, 5))

    line = MCLine(500)
    story.append(line)
    story.append(Spacer(0, 5))

    if (len(listaTroquel) == 0):
        texto = "NO UTILIZA"
        p = Paragraph(texto.decode(encoding= "cp1252"), estilo)
        story.append(p)
        story.append(Spacer(0, 10))
    else:

        dataTroquel = [['Proveedor']]
        for troquel in listaTroquel:
            dataTroquel.append(troquel.listaTroquel())
        t = Table(dataTroquel,style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                       ])

        story.append(t)
        story.append(Spacer(0,10))



    #Construimos el documento a partir de los argumentos definidos
    doc.build(story, onFirstPage = myFirstPage, onLaterPages = myLaterPages)

    os.system("VistaFicha.pdf")
    os.remove("VistaFicha.pdf")

