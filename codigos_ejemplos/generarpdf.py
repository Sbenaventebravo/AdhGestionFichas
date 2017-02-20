# -*- coding: iso-8859-2 -*-

import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import winshell
import os
import datetime
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
meses ={1:'Enero',2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre',
         10:'Octbre', 11:'Noviembre', 12:'Diciembre'}
hoy =  datetime.date.today()


ruta = str(os.getcwd())+"/form.pdf"
canvas = canvas.Canvas(ruta, pagesize=letter)
canvas.setLineWidth(.3)

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 750, 'ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ')
canvas.drawString(30, 740, 'ADHESOL LTDA.')

canvas.drawString(30, 700, 'Descripcion de la ficha:')

"Cabezera de los datos"
canvas.setFont('Helvetica', 10)
canvas.drawString(30, 680, 'Pedido:')
canvas.drawString(30, 670, 'Etiqueta:')
canvas.drawString(30, 660, 'Fecha de la ficha:')
canvas.drawString(30, 650, 'Maquina:')
"Datos"

"Titulo"
canvas.setFont('Helvetica', 12)
"cabezera"
canvas.drawString(30, 620, 'Materiales')
canvas.setFont('Helvetica', 10)
canvas.drawString(30, 610, 'Codigo')
canvas.drawString(100, 610, 'Nombre')
canvas.drawString(170, 610, 'Proveedor')
canvas.drawString(240, 610, 'Ancho')
canvas.drawString(310, 610, 'TC')



canvas.setFont('Helvetica', 12)
canvas.drawString(30, 430, 'Mallas:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 330, 'Tintas:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 230, 'Adhesivo de Laminacion:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 130, 'Adhesivo Cold Foil:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 80, 'Film de Micronaje:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 60, 'Cold Foil:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 40, 'Tipo de Barniz:')

canvas.setFont('Helvetica', 12)
canvas.drawString(30, 20, 'Troquel:')





canvas.showPage()
canvas.save()

os.system(ruta + " &")
