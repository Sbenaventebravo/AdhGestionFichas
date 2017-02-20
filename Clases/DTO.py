
# -*- coding: cp1252 -*-
from datetime import datetime, date
import re

def formatoAtributoInforme(cadena,largo):
    listaCandena= list(cadena)
    for i in range(largo - len(cadena)):
        listaCandena.append(" ")
    return "".join(listaCandena)

class Caracteristica(object):
        "Clase que representa una Caracteristica de una etiqueta"
        def __init__(self,proveedor):
            "Constructor de la clase Caracteristica"
            self.__proveedor = str(str(proveedor)).upper()
        def getProveedor(self):
            return self.__proveedor
            pass
        def setProveedor(self,proveedor):
            if len(proveedor) is 0:
                raise Exception('El proveedor no puede estar vacio')
            else:
                self.__proveedor = str(proveedor).upper()


class Categoria:
    def __init__(self,nombre =" "):
        self.__idCategoria = -1
        self.__nombre = nombre

    def getIdCategoria(self):
        return self.__idCategoria
    def setIdCategoria(self, idCategoria):
        self.__idCategoria = idCategoria
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        if(len(nombre) is 0):
            raise Exception("El nombre no puede estar vacio")
        else:
            self.__nombre = str(nombre).upper()
    def __str__(self):
        res  = "Informacion de Categoria\n=================\nNombre:{0}".format(self.getNombre())
        return res

class Cliente:
    def __init__(self, rut = " ", nombre = " "):
        self.__idCliente = -1
        self.__rut = rut
        self.__nombre = nombre
    def getIdCliente(self):
        return self.__idCliente
    def setIdCliente(self,idCliente):
        self.__idCliente  = idCliente
    def getRut(self):
        return  self.__rut
    def setRut(self,rut):
        rut = str(rut).upper()
        if len(rut) is 0:
            raise Exception("El rut no puede estar vacio")
        resultado = re.match("^([0-9]+-[0-9K])",rut)
        if not bool(resultado):
            raise Exception("El rut es invalido, intente nuevamente")
        else:
            self.__rut = rut
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        if(len(nombre) is 0):
            raise Exception("El nombre nos puede estar vacio")
        else:
            self.__nombre = str(nombre).upper()
    def __str__(self):
        res = "Datos Cliente\n"+"=======================\nRut:{0}\nNombre:{1}".format(
            str(self.getRut()),
            str(self.getNombre())
            )
        return res;

class AdhesivoColdFoil(Caracteristica):
        "Clase que representa un tipo de Caracteristica de una etiqueta, Caracteristica Adhesivo Cold Foil"
        def __init__(self,proveedor="",anilox="", hotstamping = False):
            "Constructor de la clase AdhesivoColdFoil"
            Caracteristica.__init__(self, proveedor)
            self.__idAdhCoFo = -1
            self.__anilox = str(anilox)
            pass
        "Encapsulamiento de atributos"
        def getIdAdhCoFo(self):
            return self.__idAdhCoFo
        def setIdAdhCoFo(self, value):
            self.__idAdhCoFo = value
        def getAnilox(self):
            return self.__anilox
            pass
        def setAnilox(self, anilox):
            self.__anilox = str(anilox).upper()
        def __str__(self):
            res = "{0}\t{1}\n\n".format(
                                str(formatoAtributoInforme(self.getProveedor(), 30)),
                                str(formatoAtributoInforme(str(self.getAnilox()), 8)))
            return res


        def listaAdhCoFo(self):
            lista = list()
            lista.append(self.getProveedor())
            lista.append(str(self.getAnilox()))
            return lista

class AdhesivoLaminacion(Caracteristica):
        "Clase que representa un tipo de Caracteristica de una etiqueta, Caracteristica Adhesivo Laminacion"
        def __init__(self,proveedor = "",anilox = ""):
            "Constructor Clase Adhesivo Laminacion"
            Caracteristica.__init__(self,proveedor)
            self.__idAdhLam = -1
            self.__anilox = anilox

        "Encapsulamiento de atributos"  
        def getIdAdhLam(self):
            return self.__idAdhLam
        def setIdAdhLam(self, value):
            self.__idAdhLam = value
        def getAnilox(self):
            return self.__anilox
            pass
        def setAnilox(self, anilox):
            if len(anilox) is 0:
                raise Exception('El anilox no puede estar vacio')
            else:
                self.__anilox = str(anilox).upper()

        def getAdhLam(self):
            return self.__idAdhLam
        def setAdhLam(self, value):
            self.__idAdhLam = value
            pass

        def __str__(self):
                res = "{0}\t{1}\n\n".format(
                                str(formatoAtributoInforme(self.getProveedor(), 30)),
                                str(formatoAtributoInforme(self.getAnilox(), 20)))
                return res
                pass
        def listaAdhLam(self):
            lista = list()
            lista.append(self.getProveedor())
            lista.append(self.getAnilox())
            return lista

class ColdFoil(Caracteristica):
        "Clase que representa un tipo de Caracteristica de una etiqueta, Caracteristica Cold Foil"
        def __init__(self,proveedor = "",ancho = -.1, tipo = False ):
            "Constructor de la clase Cold Foil"
            Caracteristica.__init__(self, proveedor)
            self.__idColdFoil = -1
            self.__ancho = float(ancho)
            self.__tipo = tipo
        "Encapsulamiento de atributos"
        def getIdColdFoil(self):
            return self.__idColdFoil
            pass
        def setIdColdFoil(self, value):
            self.__idColdFoil = value
            pass
        def getAncho(self):
            return self.__ancho
        def setAncho(self, ancho):
            if ancho <= 0:
                raise Exception('El ancho debe ser mayor a 0')
            else:
                self.__ancho = float(ancho)
        def getTipo(self):
            return self.__tipo
        def setTipo(self, tipo):
            self.__tipo = bool(tipo)
        def __str__(self):
            res = "{0}\t{1}\n\n".format(
                            str(formatoAtributoInforme(self.getProveedor(), 30)),
                            str(formatoAtributoInforme(str(self.getAncho()), 8)),
                            str(formatoAtributoInforme(str(self.getTipo(), 8))))
            return res
            pass
        def listaColdFoil(self):
            lista = list()
            lista.append(self.getProveedor())
            lista.append(str(self.getAncho()))
            return lista

class FilmMicronaje(Caracteristica):
        "Clase que representa un tipo de Caracteristica de una etiqueta, Caracteristica Film Micronaje"
        def __init__(self,proveedor = "", ancho = -.1):
            Caracteristica.__init__(self, proveedor)
            self.__idFilmMi = -1
            self.__ancho = float(ancho)
            pass
        "Encapsulamiento de atributos"
        def getIdFilmMi(self):
            return self.__idFilmMi
            pass
        def setIdFilmMi(self, value):
            self.__idFilmMi = value
            pass
        def getAncho(self):
                return self.__ancho 
                pass
        def setAncho(self, ancho):
            if ancho <= 0:
                raise Exception('El ancho debe ser mayor a 0')
            else:
                self.__ancho = float(ancho)

        def __str__(self):
            res = "{0}\t{1}\n\n".format(
                            str(formatoAtributoInforme(self.getProveedor(), 30)),
                            str(formatoAtributoInforme(str(self.getAncho()), 8)))
            return res
            pass
        def listaFilmMi(self):
            lista = list()
            lista.append(self.getProveedor())
            lista.append(str(self.getAncho()))
            return lista

class Malla:
        "Clase que representa la malla de un etiqueta"
        def __init__(self, tipo = "", interno = False):
            "Constructor de la clase Malla"
            self.__idMalla = -1
            self.__tipo = tipo
            self.__interno = interno
        "Encapsulamiento tipo"
        def getIdMalla(self):
            return self.__idMalla
            pass
        def setIdMalla(self, value):
            self.__idMalla = value
            pass

        def getTipo(self):
                return self.__tipo
        def setTipo(self, tipo):
            if len(tipo) is 0:
                raise Exception('El tipo no puede estar vacio')
            else:
                self.__tipo = str(tipo).upper()
        "Encapsulamiento interno"               
        def getInterno(self):
            return self.__interno
        def setInterno(self, interno):
            self.__interno = interno
        def __str__(self):
            res = "{0}\t{1}\n\n".format(
                        str(formatoAtributoInforme(self.getTipo(), 20)),
                        str(formatoAtributoInforme(self.getInterno(), 20)),
                        )
            return res

        def listaMalla(self):
            lista = list()
            lista.append(self.getTipo())
            interno = "Externo"
            if self.getInterno() == True:
                interno = "Interno"
            lista.append(interno)
            return lista

class Material:
        "Clase que representa un material dentro de una etiqueta"
        def __init__(self,codigo = " ",nombre = "",proveedor = " " ,ancho = -1,TC = False):
            "Constructor dentro de la clase material"
            self.__idMaterial = -1
            self.__codigo = codigo
            self.__nombre = nombre
            self.__proveedor = proveedor
            self.__ancho = float(ancho)
            self.__TC = TC
        #Encapsulamiento para codigo
        def getIdMaterial(self):
            return self.__idMaterial
        def setIdMaterial(self,value):
            self.__idMaterial = value
            pass
        def getCodigo(self):
                return self.__codigo
        def setCodigo(self,codigo):
            if len(codigo) is 0:
                raise Exception('El Codigo no puede estar vacio')
            else:
                self.__codigo = str(codigo).upper()
        def getNombre(self):
            return self.__nombre
        def setNombre(self, nombre):
            if len(nombre) is 0:
                raise Exception('El Nombre no puede estar vacio')
            else:
                self.__nombre = str(nombre).upper()
        #Encapsulamiento para proveedor
        def getProveedor(self):
                return self.__proveedor
        def setProveedor(self,proveedor):
            if len(proveedor) is 0:
                raise Exception('El Proveedor no puede estar vacio')
            else:
                self.__proveedor = str(proveedor).upper()
        #Encapsulamiento para ancho
        def getAncho(self):
                return self.__ancho
        def setAncho(self,ancho):
                if(ancho <= 0):
                    raise Exception('El ancho debe ser mayor a 0')
                else:
                    self.__ancho = float(ancho)
        #Encapsulamiento TC
        def getTC(self):
            return self.__TC
        def setTC(self,TC):
            self.__TC = TC

        def __str__(self):
                res = "{0}\t{1}\t{2}\t{3}\t{4}\n".format(
                        str(formatoAtributoInforme(str(self.getCodigo()), 20)),
                        str(formatoAtributoInforme(str(self.getNombre()), 20)),
                        str(formatoAtributoInforme(str(self.getProveedor()), 30)),
                        str(formatoAtributoInforme(str(self.getAncho()), 8)),
                        str(formatoAtributoInforme(str(self.getTC()), 6)))
                return res
                pass

        def listaMaterial(self):
            lista = list()
            lista.append(self.getCodigo())
            lista.append(self.getNombre())
            lista.append(self.getProveedor())
            lista.append(str(self.getAncho()))
            tc = "NO"
            if self.getTC() == True:
                tc = "SI"
            lista.append(tc)
            return lista

class Maquina:
        "Clase que representa a la maquina que hace la etiqueta"
        def __init__(self,codigo= " ", velocidad = " "):
                self.__idMaquina = -1
                self.__codigo = codigo

        def getIdMaquina(self):
            return self.__idMaquina
            pass
        def setIdMaquina(self, idMaquina):
            self.__idMaquina = idMaquina

        def getCodigo(self):
                return self.__codigo
        def setCodigo(self,codigo):
            if len(codigo) is 0:
                raise Exception("El codigo no puede estar vacio")
            else:
                self.__codigo = str(codigo).upper()

        def __str__(self):
                return "Informacion Maquina\n====================\nCodigo:{0}\n".format(str(self.getCodigo()))

class Tinta:
        "Clase que representa una tinta para la elaboracion de una etiqueta"
        def __init__(self,color = "", tipo = "",anilox = "",proveedor1 = "",proveedor2 = "NO" ,proveedor3 = "NO"):
            "Constructor de la clases tinta"
            self.__idTinta = -1
            self.__color = color
            self.__tipo = tipo
            self.__anilox = anilox
            self.__proveedor1 = proveedor1
            self.__proveedor2 = proveedor2
            self.__proveedor3 = proveedor3
        "Encapsulamiento de atributos"
        def getIdTinta(self):
            return self.__idTinta
        def setIdTinta(self, value):
            self.__idTinta = value
        def getColor(self):
                return self.__color;
        def setColor(self,color):
            if len(color) is 0:
                raise Exception('El Color no puede estar vacio')
            else:
                self.__color = str(color).upper()
        def getTipo(self):
                return self.__tipo
        def setTipo(self,tipo):
            if len(tipo)  is 0:
                raise Exception('El tipo no puede estar vacio')
            else:
                self.__tipo = str(tipo).upper()
        def getAnilox(self):
                return self.__anilox
        def setAnilox(self,anilox):
            if len(anilox) is 0:
                raise Exception('El anilox no puede esta vacio')
            else:
                self.__anilox = str(anilox).upper()
        def getProveedor1(self):
                return self.__proveedor1
        def setProveedor1(self, proveedor1):
            if len(proveedor1) is 0:
                raise Exception('El Proveedor 1 no puede estar vacio')
            else:
                self.__proveedor1 = str(proveedor1).upper()
        def getProveedor2(self):
            return self.__proveedor2
        def setProveedor2(self, proveedor2):
            self.__proveedor2 = str(proveedor2).upper()
        def getProveedor3(self):
            return self.__proveedor3
        def setProveedor3(self, proveedor3):
            self.__proveedor3 = str(proveedor3).upper()
        def __str__(self):
            res = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n\n".format(
                str(formatoAtributoInforme(str(self.getColor()), 20)),
                str(formatoAtributoInforme(str(self.getTipo()), 20)),
                str(formatoAtributoInforme(str(self.getAnilox()), 20)),
                str(formatoAtributoInforme(str(self.getProveedor1()), 30)),
                str(formatoAtributoInforme(str(self.getProveedor2()), 30)),
                str(formatoAtributoInforme(str(self.getProveedor3()), 30))
                )
            return res

        def listaTinta(self):
            lista = list()
            lista.append(self.getColor())
            lista.append(self.getTipo())
            lista.append(self.getAnilox())
            lista.append(self.getProveedor1())
            lista.append(self.getProveedor2())
            lista.append(self.getProveedor3())
            return lista

class TipoBarniz(Caracteristica):
        "Clase que representa un tipo de Caracteristica de una etiqueta, Caracteristica Tipo Barniz"
        def __init__(self, tipo = "",proveedor = "",anilox = ""):
            "Constructor de la clase Tipo Barniz",
            Caracteristica.__init__(self, proveedor)
            self.__idTBarniz = -1
            self.__tipo = tipo
            self.__anilox = anilox
            pass
        "Encapsulamiento de atributos"

        def getIdTBarniz(self):
            return self.__idTBarniz
        def setIdTBarniz(self, value):
            self.__idTBarniz = value

        def getTipo(self):
                return self.__tipo
                pass
        def setTipo(self, tipo):
            if len(tipo) is 0:
                raise Exception('El Tipo no puede estar vacio')
            else:
                self.__tipo = str(tipo).upper()
        def getAnilox(self):
                return self.__anilox
                pass
        def setAnilox(self, anilox):
            if len(anilox) is 0:
                raise Exception('El anilox no puede estar vacio')
            else:
                self.__anilox = str(anilox).upper()
        def __str__(self):
            res = "{0}\t{1}\t{2}\n\n".format(
                            str(formatoAtributoInforme(self.getProveedor(), 30)),
                            str(formatoAtributoInforme(self.getTipo(), 8)),
                            str(formatoAtributoInforme(self.getAnilox(), 20)))
            return res
            pass
        def listaTBarniz(self):
            lista = list()
            lista.append(self.getProveedor())
            lista.append(str(self.getTipo()))
            lista.append(str(self.getAnilox()))
            return lista

class Troquel(Caracteristica):
        "Clase que representa un tipo de Caracteristica de una etiqueta, Caracteristica Troquel"
        def __init__(self,proveedor = "",observacion = ""):
            "Constructor de la clase Troquel"
            Caracteristica.__init__(self, proveedor)
            self.__idTroquel = -1
            self.__observacion = observacion
            pass
        "Encapsulamiento de atributos"
        def getIdTroquel(self):
            return self.__idTroquel
        def setIdTroquel(self, value):
            self.__idTroquel = value

        def getTroquel(self):
            return self.__idTroquel
            pass
        def setTroquel(self, value):
            self.__idTroquel = value
            pass
        def getObservacion(self):
            return self.__observacion
            pass
        def setObservacion(self, value):
            self.__observacion = str(value).upper()
            pass
        def __str__(self):
            res = "{0} {1}\n\n".format(
                        str(formatoAtributoInforme(self.getProveedor(), 30))
                        , str(formatoAtributoInforme(self.getObservacion(), 120))
                        )
            return res
            pass
        def listaTroquel(self):
            lista = list()
            lista.append(str(self.getProveedor()))
            lista.append(str(self.getObservacion()))
            return lista

class FichaTecnica:
    "Clase que representa un ficha tecnica de una etiqueta"

    def __init__(self, pedido="", etiqueta=" ", fecha=date.today(), clisse=False, velocidad=-1):
        "Contructor de la clase ficha tecnica"
        self.__idFicha = -1
        self.__pedido = pedido
        self.__etiqueta = etiqueta
        self.__fecha = fecha
        self.__clisse = clisse
        self.__velocidad = velocidad
        self.__idCategoria = -1
        self.__idCliente = -1
        self.__idMaquina = -1

    "Encapsulamiento atributos"

    def getIdFicha(self):
        return self.__idFicha
        pass
    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def getPedido(self):
        return self.__pedido
    def setPedido(self, pedido):
        if len(pedido) is 0:
            raise Exception("El pedido no puede estar vacio")
        else:
            self.__pedido = str(pedido).upper()

    def getEtiqueta(self):
        return self.__etiqueta
    def setEtiqueta(self, etiqueta):
        if len(etiqueta) is 0:
            raise Exception("La etiqueta no puede estar vacia")
        else:
            self.__etiqueta = str(etiqueta).upper()

    def getFecha(self):
        return self.__fecha
    def setFecha(self, fecha):
        fechaf = datetime.strptime(fecha, "%d/%m/%Y").date()
        self.__fecha = fechaf

    def getClisse(self):
        return self.__clisse
    def setClisse(self, value):
        self.__clisse = value

    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self, velocidad):
        if velocidad <= 0.0:
            raise Exception("la velocidad debe ser mayor a 0")
        else:
            self.__velocidad = velocidad

    def getIdCategoria(self):
        return self.__idCategoria
        pass
    def setIdCategoria(self, value):
        self.__idCategoria = value
        pass

    def getIdCliente(self):
        return self.__idCliente
        pass
    def setIdCliente(self,value):
        self.__idCliente = value
        pass

    def getIdMaquina(self):
        return self.__idMaquina
        pass
    def setIdMaquina(self, value):
        self.__idMaquina = value
        pass

    def __str__(self):
        res = "Pedido:{0}\tEtiqueta:'{1}'\tFecha:{2}\tVelocidad Maquina:{3}(m/m)\n".format(
            str(self.getPedido()),
            str(self.getEtiqueta()),
            str(self.getFecha()),
            str(self.getVelocidad()))

        return res


