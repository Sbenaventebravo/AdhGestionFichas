
# -*- coding: utf-8 -*-

from Conexion import conexion
import DTO
import MySQLdb
import sys


class Categoria():
    def __init__(self,categoria=""):
        self.__conn = conexion()
        self.__categoria = categoria
    def getConn(self):
        return self.__conn
    def getCategoria(self):
        return self.__categoria
        pass
    def setCategoria(self, categoria):
        if categoria is None or categoria.getNombre() is " ":
            raise Exception("La categoria no puede ser nula")
        else:
            self.__categoria = categoria
        pass
    def insertarCategoria(self):
        cursor = self.getConn().cursor()
        try:
            sql ="INSERT INTO categoria (nombre) VALUES('{0}')".format(self.getCategoria().getNombre())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerCategoria(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idCategoria,nombre FROM categoria WHERE nombre ='{0}'".format(
                                                                               self.getCategoria().getNombre())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getCategoria().setIdCategoria(int(row[0]))
                self.getCategoria().setNombre(str(row[1]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerCategoriaId(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idCategoria,nombre FROM categoria WHERE idCategoria ={0}".format(
                                                                               self.getCategoria().getIdCategoria())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getCategoria().setIdCategoria(int(row[0]))
                self.getCategoria().setNombre(str(row[1]))

        except Exception as e:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerTodo(self):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT * FROM categoria"
            cursor.execute(sql)
            row = cursor.fetchall()
        except Exception:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def modificarCategoria(self,idCategoria):
        cursor = self.getConn().cursor()
        try:
            sql ="UPDATE categoria SET nombre='{0}' WHERE idCategoria={1}".format(self.getCategoria().getNombre(),
                                                                                idCategoria)
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def eliminarCategoria(self):
        cursor = self.getConn().cursor()
        try:
            sql ="DELETE FROM categoria WHERE idCategoria={0}".format(self.getCategoria().getIdCategoria())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

class Cliente():
    def __init__(self, cliente=""):
        self.__conn = conexion()
        self.__cliente = cliente
    def getConn(self):
        return self.__conn
    def getCliente(self):
        return self.__cliente
        pass
    def setCliente(self, cliente):
        if cliente is None or cliente.getRut() is " ":
            raise Exception("El cliente no puede ser nulo")
        else:
            self.__cliente = cliente
        pass
    def insertarCliente(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO cliente (rutCliente,nombreCliente) VALUES ('{0}','{1}')".\
                format(self.getCliente().getRut(),
                       self.getCliente().getNombre())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerClientePorRut(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idCliente,rutCliente,nombreCliente FROM cliente WHERE rutCliente ='{0}'".\
                format(self.getCliente().getRut())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("El Cliente buscado no existe")
            else:
                self.getCliente().setIdCliente(int(row[0]))
                self.getCliente().setRut(str(row[1]))
                self.getCliente().setNombre(str(row[2]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerCliente(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idCliente,rutCliente,nombreCliente FROM cliente WHERE rutCliente ='{0}'".\
                format(self.getCliente().getRut())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("El Cliente buscado no existe")
            else:
                self.getCliente().setIdCliente(int(row[0]))
                self.getCliente().setRut(str(row[1]))
                self.getCliente().setNombre(str(row[2]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerClienteNombre(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idCliente,rutCliente,nombreCliente FROM cliente WHERE nombreCliente ='{0}'".\
                format(self.getCliente().getNombre())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("El Cliente buscado no existe")
            else:
                self.getCliente().setIdCliente(int(row[0]))
                self.getCliente().setRut(str(row[1]))
                self.getCliente().setNombre(str(row[2]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerClienteId(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idCliente,rutCliente,nombreCliente FROM cliente WHERE idCliente ={0}".\
                format(self.getCliente().getIdCliente())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("El Cliente buscado no existe")
            else:
                self.getCliente().setIdCliente(int(row[0]))
                self.getCliente().setRut(str(row[1]))
                self.getCliente().setNombre(str(row[2]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerTodo(self):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT * FROM cliente"
            cursor.execute(sql)
            row = cursor.fetchall()
        except Exception:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def modificarCliente(self,idCliente):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE cliente SET rutCliente='{0}',nombreCliente='{1}' WHERE idCliente={2}".\
                format(self.getCliente().getRut(),
                       self.getCliente().getNombre(),
                       idCliente)
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarCliente(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM cliente WHERE idCliente={0}".format(self.getCliente().getIdCliente())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

class Maquina():
    def __init__(self, maquina=""):
        self.__conn = conexion()
        self.__maquina = maquina
    def getConn(self):
        return self.__conn
    def getMaquina(self):
        return self.__maquina
    def setMaquina(self, maquina):
        if maquina is None or maquina.getCodigo() is " ":
            raise Exception("El codigo de maquina no puede ser nulo")
        else:
            self.__maquina = maquina
    def insertarMaquina(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO maquina (codigo) VALUES ('{0}')". \
                format(self.getMaquina().getCodigo())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def leerMaquina(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMaquina,codigo FROM maquina WHERE codigo ='{0}'". \
                format(self.getMaquina().getCodigo())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La Maquina buscada no existe")
            else:
                self.getMaquina().setIdMaquina(int(row[0]))
                self.getMaquina().setCodigo(str(row[1]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerMaquinaId(self):
        cursor = self.getConn().cursor()

        try:
            sql = "SELECT idMaquina,codigo FROM maquina WHERE idMaquina ={0}". \
                format(self.getMaquina().getIdMaquina())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La Maquina buscada no existe")
            else:
                self.getMaquina().setIdMaquina(int(row[0]))
                self.getMaquina().setCodigo(str(row[1]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True

    def leerTodo(self):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT * FROM maquina"
            cursor.execute(sql)
            row = cursor.fetchall()
        except Exception:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def modificarMaquina(self,idMaquina):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE maquina SET codigo='{0}' WHERE idMaquina={1}". \
                format(self.getMaquina().getCodigo(),
                       idMaquina)
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def eliminarMaquina(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM maquina WHERE idMaquina={0}".format(self.getMaquina().getIdMaquina())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def idUltimaMaquinaInsertada(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMaquina FROM Maquina ORDER BY idMaquina DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay maquinas registradas")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
            return idUltima

class FichaTecnica:
    def __init__(self, fichaTecnica = DTO.FichaTecnica()):
        self.__conn = conexion()
        self.__fichaTecnica = fichaTecnica
    def getConn(self):
        return self.__conn
    def getFichaTecnica(self):
        return self.__fichaTecnica
    def setFichaTecnica(self, fichaTecnica):
        if fichaTecnica is None or fichaTecnica.getPedido() is " ":
            raise Exception("El pedido de la ficha no puede ser nulo")
        else:
            self.__fichaTecnica = fichaTecnica
    def insertarFichaTecnica(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO ficha_tecnica_etiqueta (pedido,etiqueta,fecha,clisses,velocidad,idCategoria,idCliente,idMaquina) " \
                  "VALUES ('{0}','{1}','{2}',{3},{4},{5},{6},{7})". \
                format(self.getFichaTecnica().getPedido(),
                       self.getFichaTecnica().getEtiqueta(),
                       self.getFichaTecnica().getFecha(),
                       self.getFichaTecnica().getClisse(),
                       self.getFichaTecnica().getVelocidad(),
                       self.getFichaTecnica().getIdCategoria(),
                       self.getFichaTecnica().getIdCliente(),
                       self.getFichaTecnica().getIdMaquina())
            cursor.execute(sql)
        except Exception as e:

            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerFichaTecnica(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idFicha,pedido,etiqueta,fecha,clisses,velocidad,idCategoria,idCliente,idMaquina FROM ficha_tecnica_etiqueta WHERE pedido ='{0}'". \
                format(self.getFichaTecnica().getPedido())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La Ficha Tecnica buscada no existe")
            else:
                self.getFichaTecnica().setIdFicha(int(row[0]))
                self.getFichaTecnica().setPedido(str(row[1]))
                self.getFichaTecnica().setEtiqueta(str(row[2]))
                fecha = str(row[3]).split('-')
                fecha = "{0}/{1}/{2}".format(fecha[2], fecha[1], fecha[0])
                self.getFichaTecnica().setFecha(fecha)
                self.getFichaTecnica().setClisse(bool(row[4]))
                self.getFichaTecnica().setVelocidad(float(row[5]))
                self.getFichaTecnica().setIdCategoria(int(row[6]))
                self.getFichaTecnica().setIdCliente(int(row[7]))
                self.getFichaTecnica().setIdMaquina(int(row[8]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerFichaTecnicaPedMaq(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idFicha,pedido,etiqueta,fecha,clisses,velocidad,idCategoria,idCliente,idMaquina " \
                  "FROM ficha_tecnica_etiqueta WHERE pedido ='{0}' and etiqueta='{1}' and idMaquina ='{2}'". \
                format(self.getFichaTecnica().getPedido(),
                       self.getFichaTecnica().getEtiqueta(),
                       self.getFichaTecnica().getIdMaquina())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La Ficha Tecnica buscada no existe")
            else:
                self.getFichaTecnica().setIdFicha(int(row[0]))
                self.getFichaTecnica().setPedido(str(row[1]))
                self.getFichaTecnica().setEtiqueta(str(row[2]))
                fecha = str(row[3]).split('-')
                fecha = "{0}/{1}/{2}".format(fecha[2], fecha[1], fecha[0])
                self.getFichaTecnica().setFecha(fecha)
                self.getFichaTecnica().setClisse(bool(row[4]))
                self.getFichaTecnica().setVelocidad(float(row[5]))
                self.getFichaTecnica().setIdCategoria(int(row[6]))
                self.getFichaTecnica().setIdCliente(int(row[7]))
                self.getFichaTecnica().setIdMaquina(int(row[8]))

        except Exception as e:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def leerFichaTecnicaidFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idFicha,pedido,etiqueta,fecha,clisses,velocidad,idCategoria,idCliente,idMaquina FROM ficha_tecnica_etiqueta WHERE idFicha ={0}". \
                format(self.getFichaTecnica().getIdFicha())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La Ficha Tecnica buscada no existe")
            else:
                self.getFichaTecnica().setIdFicha(int(row[0]))
                self.getFichaTecnica().setPedido(str(row[1]))
                self.getFichaTecnica().setEtiqueta(str(row[2]))
                fecha = str(row[3]).split('-')
                fecha = "{0}/{1}/{2}".format(fecha[2], fecha[1], fecha[0])
                self.getFichaTecnica().setFecha(fecha)
                self.getFichaTecnica().setClisse(bool(row[4]))
                self.getFichaTecnica().setVelocidad(float(row[5]))
                self.getFichaTecnica().setIdCategoria(int(row[6]))
                self.getFichaTecnica().setIdCliente(int(row[7]))
                self.getFichaTecnica().setIdMaquina(int(row[8]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def recuperarFichaTecnica(self,pedido):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT cli.nombreCliente as Cliente,fte.pedido as Pedido,fte.etiqueta as Etiqueta," \
                    " m.codigo as Maquina  "\
                    "FROM ficha_tecnica_etiqueta as fte "\
                    "LEFT JOIN categoria as c " \
                    "ON (c.idCategoria = fte.idCategoria) "\
                    "LEFT JOIN cliente as cli "\
                    "ON (cli.idCliente = fte.idCliente)" \
                    "LEFT JOIN maquina as m " \
                    "ON (m.idMaquina = fte.idMaquina)"\
                    "WHERE fte.pedido = '{0}'".format(pedido)
            cursor.execute(sql)
            row = cursor.fetchall()

        except Exception:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def leerTodo(self):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT * FROM ficha_tecnica_etiqueta"
            cursor.execute(sql)
            row = cursor.fetchall()
        except Exception:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def leerPorCatergoria(self, nombre):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT cli.nombreCliente as Cliente,fte.pedido as Pedido,fte.etiqueta as Etiqueta," \
                    " m.codigo as Maquina  "\
                    "FROM ficha_tecnica_etiqueta as fte "\
                    "LEFT JOIN categoria as c " \
                    "ON (c.idCategoria = fte.idCategoria) "\
                    "LEFT JOIN cliente as cli "\
                    "ON (cli.idCliente = fte.idCliente)" \
                    "LEFT JOIN maquina as m " \
                    "ON (m.idMaquina = fte.idMaquina)"\
                    "WHERE nombre = %s"
            cursor.execute(sql, nombre)
            row = cursor.fetchall()
        except Exception:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def recuperarFichaTecnicaEtiqueta(self, etiqueta):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT cli.nombreCliente as Cliente,fte.pedido as Pedido,fte.etiqueta as Etiqueta," \
                    " m.codigo as Maquina  "\
                    "FROM ficha_tecnica_etiqueta as fte "\
                    "LEFT JOIN categoria as c " \
                    "ON (c.idCategoria = fte.idCategoria) "\
                    "LEFT JOIN cliente as cli "\
                    "ON (cli.idCliente = fte.idCliente)" \
                    "LEFT JOIN maquina as m " \
                    "ON (m.idMaquina = fte.idMaquina)"\
                    "WHERE fte.etiqueta = '{0}'".format(etiqueta)
            cursor.execute(sql)
            row = cursor.fetchall()

        except Exception as e:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def recuperarFichaTecnicaCliente(self, cliente):
        cursor = self.getConn().cursor(MySQLdb.cursors.DictCursor)
        row = None
        try:
            sql = "SELECT cli.nombreCliente as Cliente,fte.pedido as Pedido,fte.etiqueta as Etiqueta," \
                    " m.codigo as Maquina  "\
                    "FROM ficha_tecnica_etiqueta as fte "\
                    "LEFT JOIN categoria as c " \
                    "ON (c.idCategoria = fte.idCategoria) "\
                    "LEFT JOIN cliente as cli "\
                    "ON (cli.idCliente = fte.idCliente)" \
                    "LEFT JOIN maquina as m " \
                    "ON (m.idMaquina = fte.idMaquina)"\
                    "WHERE cli.nombreCliente = %s"
            cursor.execute(sql, cliente)
            row = cursor.fetchall()

        except Exception as e:
            cursor.close()
            self.getConn().close()
            return row
        else:
            cursor.close()
            self.getConn().close()
            return row
    def modificarFichaTecnica(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE ficha_tecnica_etiqueta SET pedido='{0}',etiqueta='{1}', fecha='{2}'" \
                  ", clisses={3} ,velocidad={4}, " \
                  "idCategoria = {5}, " \
                  "idCliente = {6}, idMaquina = {7}" \
                  " WHERE idFicha={8}". \
                format(self.getFichaTecnica().getPedido(),
                       self.getFichaTecnica().getEtiqueta(),
                       self.getFichaTecnica().getFecha(),
                       self.getFichaTecnica().getClisse(),
                       self.getFichaTecnica().getVelocidad(),
                       self.getFichaTecnica().getIdCategoria(),
                       self.getFichaTecnica().getIdCliente(),
                       self.getFichaTecnica().getIdMaquina(),
                       self.getFichaTecnica().getIdFicha())

            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def eliminarFichaTecnica(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM ficha_tecnica_etiqueta WHERE idFicha={0}".format(self.getFichaTecnica().getIdFicha())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def idUltimaFicha(self):
        cursor = self.getConn().cursor()
        idUltima = -1
        try:
            sql = "SELECT idFicha FROM ficha_tecnica_etiqueta ORDER BY idFicha DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("No hay Fichas Tecnicas registrados")
            else:
                idUltima = int(row[0])
        except Exception as e:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima
    pass

"Caracteristicas Obligatorias"
class Material:
    def __init__(self, material = ""):
        self.__conn = conexion()
        self.__material = material
    def getConn(self):
        return self.__conn
    def getMaterial(self):
        return self.__material
    def setMaterial(self, material):
        self.__material = material
    def insertarMaterial(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO material (codigo,nombre,proveedor,ancho,tc) " \
                  "VALUES ('{0}','{1}','{2}',{3},{4})". \
                format(self.getMaterial().getCodigo(),
                       self.getMaterial().getNombre(),
                       self.getMaterial().getProveedor(),
                       self.getMaterial().getAncho(),
                       self.getMaterial().getTC())

            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerMaterial(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMaterial,codigo,nombre,proveedor,ancho,tc FROM material WHERE codigo ='{0}'". \
                format(self.getMaterial().getCodigo())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("El Material buscado no existe")
            else:
                self.getMaterial().setIdMaterial(int(row[0]))
                self.getMaterial().setCodigo(str(row[1]))
                self.getMaterial().setProveedor(str(row[2]))
                self.getMaterial().setNombre(str(row[3]))
                self.getMaterial().setAncho(float(row[4]))
                self.getMaterial().setTC(bool(row[5]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True

    def leerMaterialPorId(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMaterial,codigo,nombre,proveedor,ancho,tc FROM material WHERE idMaterial ='{0}'". \
                format(self.getMaterial().getIdMaterial())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("El Material buscado no existe")
            else:
                self.getMaterial().setIdMaterial(int(row[0]))
                self.getMaterial().setCodigo(str(row[1]))
                self.getMaterial().setNombre(str(row[2]))
                self.getMaterial().setProveedor(str(row[3]))
                self.getMaterial().setAncho(float(row[4]))
                self.getMaterial().setTC(bool(row[5]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def modificarMaterial(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE material SET codigo='{0}',nombre='{1}', proveedor='{2}', ancho={3}, tc={4} " \
                  " WHERE idMaterial={5}". \
                format(self.getMaterial().getCodigo(),
                       self.getMaterial().getNombre(),
                       self.getMaterial().getProveedor(),
                       self.getMaterial().getAncho(),
                       self.getMaterial().getTC(),
                       self.getMaterial().getIdMaterial())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarMaterial(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM material WHERE idMaterial={0}".format(self.getMaterial().getIdMaterial())
            cursor.execute(sql)

        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def idUltimoMaterialInsertada(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMaterial FROM material ORDER BY idmaterial DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay materiales registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
            return idUltima
class Malla:
    def __init__(self, malla=""):
        self.__conn = conexion()
        self.__malla = malla

    def getConn(self):
        return self.__conn

    def getMalla(self):
        return self.__malla

    def setMalla(self, malla):
        self.__malla = malla
    def ingresarMalla(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO malla (tipo,int_o_ext) VALUES('{0}',{1})".format(
                self.getMalla().getTipo(),
                self.getMalla().getInterno())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerMalla(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMalla,tipo,int_o_ext FROM malla WHERE idMalla ='{0}'".format(
                self.getMalla().getIdMalla())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La malla buscada no existe")
            else:
                self.getMalla().setIdMalla(int(row[0]))
                self.getMalla().setTipo(str(row[1]))
                if row[2] == 1:
                    self.getMalla().setInterno(True)
                else:
                    self.getMalla().setInterno(False)


        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def modificarMalla(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE malla SET tipo='{0}', int_o_ext={1} WHERE idMalla={2}".\
                format(self.getMalla().getTipo(),
                       self.getMalla().getInterno(),
                       self.getMalla().getIdMalla())
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def eliminarMalla(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM malla WHERE idMalla={0}".format(self.getMalla().getIdMalla())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

        pass
    def idUltimaMallaInsertada(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idMalla FROM malla ORDER BY idMalla DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay mallas registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
            return idUltima
class Tinta:
    def __init__(self, tinta=""):
        self.__conn = conexion()
        self.__tinta = tinta

    def getConn(self):
        return self.__conn
    def getTinta(self):
        return self.__tinta
    def setTinta(self, tinta):
        self.__tinta = tinta
    def ingresarTinta(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO tinta (color,tipo,anilox,proveedor,proveedor2,proveedor3) " \
                  "VALUES('{0}','{1}','{2}','{3}','{4}','{5}')".\
                   format(self.getTinta().getColor(),
                          self.getTinta().getTipo(),
                          self.getTinta().getAnilox(),
                          self.getTinta().getProveedor1(),
                          self.getTinta().getProveedor2(),
                          self.getTinta().getProveedor3())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def leerTinta(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idTinta,color,tipo,anilox,proveedor,proveedor2,proveedor3 " \
                  "FROM tinta WHERE idTinta ='{0}'".\
                   format(self.getTinta().getIdTinta())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getTinta().setIdTinta(int(row[0]))
                self.getTinta().setColor(str(row[1]))
                self.getTinta().setTipo(str(row[2]))
                self.getTinta().setAnilox(str(row[3]))
                self.getTinta().setProveedor1(str(row[4]))
                self.getTinta().setProveedor2(str(row[5]))
                self.getTinta().setProveedor3(str(row[6]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
        pass
    def modificarTinta(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE tinta SET color='{0}', tipo='{1}', anilox='{2}', proveedor ='{3}'" \
                  ", proveedor2 = '{4}', proveedor3='{5}' " \
                  "WHERE idTinta={6}".\
                  format(self.getTinta().getColor(),
                         self.getTinta().getTipo(),
                         self.getTinta().getAnilox(),
                         self.getTinta().getProveedor1(),
                         self.getTinta().getProveedor2(),
                         self.getTinta().getProveedor3(),
                         self.getTinta().getIdTinta())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def eliminarTinta(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM tinta WHERE idTinta={0}".\
                format(self.getTinta().getIdTinta())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def idUltimaTinta(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idTinta FROM tinta ORDER BY idTinta DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay Tintas registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
            return idUltima
"Caracteristicas Secundarias"

class AdhesivoColdFoil:
    def __init__(self, adhCoFo=""):
        self.__conn = conexion()
        self.__adhCoFo = adhCoFo

    def getConn(self):
        return self.__conn

    def getAdhCoFo(self):
        return self.__adhCoFo

    def setAdhCoFo(self, adhCoFo):
        self.__adhCoFo = adhCoFo
    def ingresarAdhCoFo(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO adhesivo_coldfoil (proveedor,anilox) " \
                  "VALUES('{0}','{1}')". \
                format(self.getAdhCoFo().getProveedor(),
                       self.getAdhCoFo().getAnilox())
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerAdhCoFo(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idAdhColdFoil,proveedor,anilox " \
                  "FROM adhesivo_coldfoil WHERE idAdhColdFoil ='{0}'". \
                format(self.getAdhCoFo().getIdAdhCoFo())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getAdhCoFo().setProveedor(str(row[1]))
                self.getAdhCoFo().setAnilox(str(row[2]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def modificarAdhCoFo(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE adhesivo_coldfoil SET proveedor='{0}', anilox='{1}' " \
                  "WHERE idAdhColdFoil={2}". \
                format(self.getAdhCoFo().getProveedor(),
                       self.getAdhCoFo().getAnilox(),
                       self.getAdhCoFo().getIdAdhCoFo())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def eliminarAdhCoFo(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM adhesivo_coldfoil WHERE idAdhColdFoil={0}". \
                format(self.getAdhCoFo().getIdAdhCoFo())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def idUltimoAdhCoFo(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idAdhColdFoil FROM adhesivo_coldfoil ORDER BY idAdhColdFoil DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay Adhesivos Cold Foil registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima
        pass

class AdhesivoLaminacion:
    def __init__(self, adhlam=""):
        self.__conn = conexion()
        self.__adhlam = adhlam

    def getConn(self):
        return self.__conn
    def getAdhlam(self):
        return self.__adhlam
    def setAdhlam(self, adhlam):
        self.__adhlam = adhlam
    def ingresarAdhLam(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO adhesivo_laminacion (proveedor,anilox) " \
                  "VALUES('{0}','{1}')". \
                format(self.getAdhlam().getProveedor(),
                       self.getAdhlam().getAnilox())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerAdhLam(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idAdhLam,proveedor,anilox " \
                  "FROM adhesivo_laminacion WHERE idAdhLam ='{0}'". \
                format(self.getAdhlam().getIdAdhLam())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getAdhlam().setProveedor(str(row[1]))
                self.getAdhlam().setAnilox(str(row[2]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def modificarAdhLam(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE adhesivo_laminacion SET proveedor='{0}', anilox='{1}' " \
                  "WHERE idAdhLam={2}". \
                format(self.getAdhlam().getProveedor(),
                       self.getAdhlam().getAnilox(),
                       self.getAdhlam().getIdAdhLam())
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

        pass
    def eliminarAdhLam(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM adhesivo_laminacion WHERE idAdhLam={0}". \
                format(self.getAdhlam().getIdAdhLam())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass

    def idUltimoAdhLam(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idAdhLam FROM adhesivo_laminacion ORDER BY idAdhLam DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay Adhesivos de Laminacion registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima
    pass

class ColdFoil:
    def __init__(self, coldfoil=""):
        self.__conn = conexion()
        self.__coldfoil = coldfoil

    def getConn(self):
        return self.__conn

    def getColdFoil(self):
        return self.__coldfoil

    def setColdFoil(self, coldfoil):
        self.__coldfoil = coldfoil
    def ingresarColdFoil(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO cold_foil (proveedor,ancho,tipo) " \
                  "VALUES('{0}',{1},{2})". \
                format(self.getColdFoil().getProveedor(),
                       self.getColdFoil().getAncho(),
                       self.getColdFoil().getTipo())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerColdFoil(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idColdFoil,proveedor,ancho,tipo " \
                  "FROM cold_foil WHERE idColdFoil ='{0}'". \
                format(self.getColdFoil().getIdColdFoil())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getColdFoil().setProveedor(str(row[1]))
                self.getColdFoil().setAncho(int(row[2]))
                self.getColdFoil().setTipo(bool(row[3]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True

        pass
    def modificarColdFoil(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE cold_foil SET proveedor='{0}', ancho={1}, tipo={2} " \
                  "WHERE idColdFoil={3}". \
                format(self.getColdFoil().getProveedor(),
                       self.getColdFoil().getAncho(),
                       self.getColdFoil().getTipo(),
                       self.getColdFoil().getIdColdFoil())
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def eliminarColdFoil(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM cold_foil WHERE idColdFoil={0}". \
                format(self.getColdFoil().getIdColdFoil())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass

    def idUltimoColdFoil(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idColdFoil FROM cold_foil ORDER BY idColdFoil DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay Cold Foil registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima

    pass

class FilmMicronaje:
    def __init__(self, filmMi=""):
        self.__conn = conexion()
        self.__filmMi = filmMi

    def getConn(self):
        return self.__conn

    def getFilmMi(self):
        return self.__filmMi

    def setFilmMi(self, filmMi):
        self.__filmMi = filmMi
    def ingresarFilmMi(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO film_micronaje (proveedor,ancho) " \
                  "VALUES('{0}',{1})". \
                format(self.getFilmMi().getProveedor(),
                       self.getFilmMi().getAncho())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerFilmMi(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idFilmMi,proveedor,ancho " \
                  "FROM film_micronaje WHERE idFilmMi ='{0}'". \
                format(self.getFilmMi().getIdFilmMi())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getFilmMi().setProveedor(str(row[1]))
                self.getFilmMi().setAncho(int(row[2]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
        pass
    def modificarFilmMi(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE film_micronaje SET proveedor='{0}', ancho={1} " \
                  "WHERE idFilmMi={2}". \
                format(self.getFilmMi().getProveedor(),
                       self.getFilmMi().getAncho(),
                       self.getFilmMi().getIdFilmMi())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarFilmMi(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM film_micronaje WHERE idFilmMi={0}". \
                format(self.getFilmMi().getIdFilmMi())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def idUltimoFilmMi(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idFilmMi FROM film_micronaje ORDER BY idFilmMi DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay Film de Micronaje registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima
class TipoBarniz:
    def __init__(self, tBarniz=""):
        self.__conn = conexion()
        self.__tBarniz = tBarniz

    def getConn(self):
        return self.__conn

    def getTBarniz(self):
        return self.__tBarniz

    def setTBarniz(self, tBarniz):
        self.__tBarniz = tBarniz
    def ingresarTBarniz(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO tipo_barniz (tipo,proveedor,anilox) " \
                  "VALUES('{0}','{1}', '{2}')". \
                format(self.getTBarniz().getTipo(),
                       self.getTBarniz().getProveedor(),
                       self.getTBarniz().getAnilox())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def leerTBarniz(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idTBarniz,tipo,proveedor,anilox " \
                  "FROM tipo_barniz WHERE idTBarniz ='{0}'". \
                format(self.getTBarniz().getIdTBarniz())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La categoria buscada no existe")
            else:
                self.getTBarniz().setTipo(str(row[1]))
                self.getTBarniz().setProveedor(str(row[2]))
                self.getTBarniz().setAnilox(str(row[3]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
        pass
    def modificarTBarniz(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE tipo_barniz SET tipo='{0}', proveedor='{1}', anilox ='{2}' " \
                  "WHERE idTBarniz={3}". \
                format(self.getTBarniz().getTipo(),
                       self.getTBarniz().getProveedor(),
                       self.getTBarniz().getAnilox(),
                       self.getTBarniz().getIdTBarniz())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarTBarniz(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM tipo_barniz WHERE idTBarniz={0}". \
                format(self.getTBarniz().getIdTBarniz())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def idUltimoTBarniz(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idTBarniz FROM tipo_barniz ORDER BY idTBarniz DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay Tipo de barniz registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima
class Troquel:
    def __init__(self, troquel=""):
        self.__conn = conexion()
        self.__troquel = troquel

    def getConn(self):
        return self.__conn

    def getTroquel(self):
        return self.__troquel

    def setTroquel(self, troquel):
        self.__troquel = troquel
    def ingresarTroquel(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO troquel (proveedor,observacion) " \
                  "VALUES ('{0}','{1}')". \
                format(self.getTroquel().getProveedor(),
                       self.getTroquel().getObservacion())

            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerTroquel(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idTroquel,proveedor,observacion FROM troquel WHERE idTroquel ='{0}'". \
                format(self.getTroquel().getIdTroquel())
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                raise Exception("La el troquel buscado no existe")
            else:
                self.getTroquel().setProveedor(str(row[1]))
                self.getTroquel().setObservacion(str(row[2]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return False
        else:
            cursor.close()
            self.getConn().close()
            return True
    def modificarTroquel(self):
        cursor = self.getConn().cursor()
        try:
            sql = "UPDATE troquel SET proveedor='{0}', observacion ='{1}' " \
                  " WHERE idTroquel={2}". \
                format(self.getTroquel().getProveedor(),
                       self.getTroquel().getObservacion(),
                       self.getTroquel().getIdTroquel())
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarTroquel(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM troquel WHERE idTroquel={0}".format(self.getTroquel().getIdTroquel())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def idUltimoTroquel(self):
        cursor = self.getConn().cursor()
        try:
            sql = "SELECT idTroquel FROM troquel ORDER BY idTroquel DESC LIMIT 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            idUltima = -1
            if row is None:
                raise Exception("No hay troquel registrados")
            else:
                idUltima = int(row[0])
        except Exception:
            cursor.close()
            self.getConn().close()
            return idUltima
        else:
            cursor.close()
            self.getConn().close()
        return idUltima

"Tablas intermedias caracteristicas obligatorias"

class MaterialFicha:
    def __init__(self,idMaterial = "", idFicha=""):
        self.__conn = conexion()
        self.__idMaterialFicha = -1
        self.__idMaterial = idMaterial
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn
    def getIdMaterial(self):
        return self.__idMaterial
        pass
    def setIdMaterial(self, value):
        self.__idMaterial = value
        pass
    def getIdFicha(self):
        return self.__idFicha
        pass
    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarMaterialFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO material_ficha" \
                  " (idMaterial, idFicha) VALUES({0},{1})"\
                .format(self.getIdMaterial(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
    def leerMaterialesEnFicha(self,idFicha):
        cursor = self.getConn().cursor()
        listaMateriales = list()
        try:
            sql = "SELECT idMaterial FROM material_ficha" \
                  " WHERE idFicha ={0}"\
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is None:
                raise Exception("La ficha buscada no existe")
            else:
                for reg in row:
                    listaMateriales.append(int(reg[0]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaMateriales
    def eliminarMaterialFichaPorFicha(self, idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM material_ficha idFicha={0}"\
                .format(idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarMaterialFichaPorMaterial(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM material_ficha idMaterial={0}"\
                .format(self.getIdMaterial())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
    def eliminarTodo(self):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE * FROM material_ficha" \
                .format(self.getIdFicha())
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass

    def eliminarreferencia(self,idmaterial,idficha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM material_ficha WHERE idMaterial ={0} and idFicha={1}" \
                .format(idmaterial,idficha)
            cursor.execute(sql)

        except Exception as e:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass

class MallaFicha:
    def __init__(self, idMalla="", idFicha=""):
        self.__conn = conexion()
        self.__idMallaFicha = -1
        self.__idMalla = idMalla
        self.__idFicha = idFicha
    def getConn(self):
        return self.__conn

    def getIdMalla(self):
        return self.__idMalla
        pass

    def setIdMalla(self, value):
        self.__idMalla = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarMallaFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO malla_ficha (idMalla, idFicha) VALUES({0},{1})" \
                .format(self.getIdMalla(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerMallaEnFicha(self, idFicha):
        cursor = self.getConn().cursor()
        listaMalla = list()
        try:
            sql = "SELECT idMalla FROM malla_ficha WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is None:
                raise Exception("La ficha buscada no existe")
            else:
                for row in cursor:
                    listaMalla.append(int(row[1]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaMalla
    def leerMallaEnFicha(self, idFicha):
        cursor = self.getConn().cursor()
        listaMalla = list()
        try:
            sql = "SELECT idMalla FROM malla_ficha WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is None:
                raise Exception("La ficha buscada no existe")
            else:
                for reg in row:
                    listaMalla.append(int(reg[0]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaMalla

    def eliminarReferencia(self,idMalla,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM malla_ficha WHERE idMalla={0} and idFicha={1}" \
                .format(idMalla,idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
class TintaFicha:
    def __init__(self, idTinta="", idFicha=""):
        self.__conn = conexion()
        self.__idTintaFicha = -1
        self.__idTinta = idTinta
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn
    def getIdTinta(self):
        return self.__idTinta
        pass

    def setIdTinta(self, value):
        self.__idTinta = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarTintaFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO tinta_ficha" \
                  " (idTinta, idFicha) VALUES({0},{1})" \
                .format(self.getIdTinta(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerTintaEnFicha(self,idFicha):
        cursor = self.getConn().cursor()
        listaTintas = list()
        try:
            sql = "SELECT idTinta FROM tinta_ficha" \
                  " WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is None:
                raise Exception("La ficha buscada no existe")
            else:
                for reg in row:
                    listaTintas.append(int(reg[0]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaTintas

    def eliminarReferencia(self,idTinta,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM tinta_ficha" \
                  " WHERE idTinta={0} and idFicha={1}" \
                .format(idTinta,
                        idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass

"Tablas intermedias de caracteristicas secundarias"
class AdhLamFicha:
    def __init__(self, idAdhLam="", idFicha=""):
        self.__conn = conexion()
        self.__idAdhLamFicha = -1
        self.__idAdhLam = idAdhLam
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn
    def getIdAdhLam(self):
        return self.__idAdhLam
        pass

    def setIdAdhLam(self, value):
        self.__idAdhLam = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarAdhLamFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO adhlam_ficha" \
                  " (idAdhLam, idFicha) VALUES({0},{1})" \
                .format(self.getIdAdhLam(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerAdhLamFicha(self,idFicha):
        cursor = self.getConn().cursor()
        listaAdhLam = list()
        try:
            sql = "SELECT idAdhLam FROM adhlam_ficha" \
                  " WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is not None:
                for reg in row:
                    listaAdhLam.append(int(reg[0]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaAdhLam

    def eliminarReferencia(self,idAdhlam,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM adhlam_ficha" \
                  " WHERE idAdhLam={0} and idFicha={1}" \
                .format(idAdhlam,
                        idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
class AdhCoFoFicha:
        def __init__(self, idAdhCoFo="", idFicha=""):
            self.__conn = conexion()
            self.__idAdhCoFo_Ficha = -1
            self.__idAdhCoFo = idAdhCoFo
            self.__idFicha = idFicha

        def getConn(self):
            return self.__conn

        def getIdAdhCoFo(self):
            return self.__idAdhCoFo
            pass

        def setIdAdhCoFo(self, value):
            self.__idAdhCoFo = value
            pass

        def getIdFicha(self):
            return self.__idFicha
            pass

        def setIdFicha(self, value):
            self.__idFicha = value
            pass

        def insertarAdhCoFoFicha(self):
            cursor = self.getConn().cursor()
            try:
                sql = "INSERT INTO adhcofo_ficha" \
                      " (idAdhColdFoil, idFicha) VALUES({0},{1})" \
                    .format(self.getIdAdhCoFo(),
                            self.getIdFicha())
                cursor.execute(sql)
            except Exception:

                self.getConn().rollback()
                cursor.close()
                self.getConn().close()
                return False
            else:
                self.getConn().commit()
                cursor.close()
                self.getConn().close()
                return True

        def leerAdhCoFoEnFicha(self, idFicha):
            cursor = self.getConn().cursor()
            listaAdhCoFos = list()
            try:
                sql = "SELECT idAdhColdFoil FROM adhcofo_ficha" \
                      " WHERE idFicha ={0}" \
                    .format(idFicha)
                cursor.execute(sql)
                row = cursor.fetchall()
                if row is not None:
                    for reg in row:
                        listaAdhCoFos.append(int(reg[0]))
            except Exception:

                cursor.close()
                self.getConn().close()
                return None
            else:
                cursor.close()
                self.getConn().close()
                return listaAdhCoFos

        def eliminarReferencia(self,idAdhCofo,idFicha):
            cursor = self.getConn().cursor()
            try:
                sql = "DELETE FROM adhcofo_ficha" \
                      " WHERE idAdhColdFoil={0} and idFicha={1}" \
                    .format(idAdhCofo,
                            idFicha)
                cursor.execute(sql)

            except Exception as e:

                self.getConn().rollback()
                cursor.close()
                self.getConn().close()
                return False
            else:
                self.getConn().commit()
                cursor.close()
                self.getConn().close()
                return True
            pass
class FilmMiFicha:
    def __init__(self, idFilmMi="", idFicha=""):
        self.__conn = conexion()
        self.__idFilmMi_Ficha = -1
        self.__idFilmMi = idFilmMi
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn

    def getIdFilmMi(self):
        return self.__idFilmMi
        pass

    def setIdFilmMi(self, value):
        self.__idFilmMi = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarFilmMiFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO filmmi_ficha" \
                  " (idFilmMi, idFicha) VALUES({0},{1})" \
                .format(self.getIdFilmMi(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerFilmMiEnFicha(self, idFicha):
        cursor = self.getConn().cursor()
        listaFilmMis = list()
        try:
            sql = "SELECT idFilmMi FROM filmmi_ficha" \
                  " WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is not None:
                for reg in row:
                    listaFilmMis.append(int(reg[0]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaFilmMis

    def eliminarReferencia(self,idFilmMi,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM filmmi_ficha" \
                  " WHERE idFilmMi={0} and idFicha={1}" \
                .format(idFilmMi,
                        idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
class ColdFoilFicha:
    def __init__(self, idColdFoil="", idFicha=""):
        self.__conn = conexion()
        self.__idColdFoil_Ficha = -1
        self.__idColdFoil = idColdFoil
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn

    def getIdColdFoil(self):
        return self.__idColdFoil
        pass

    def setIdColdFoil(self, value):
        self.__idColdFoil = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarColdFoilFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO coldfoil_ficha" \
                  " (idColdFoil, idFicha) VALUES({0},{1})" \
                .format(self.getIdColdFoil(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerColdFoilEnFicha(self, idFicha):
        cursor = self.getConn().cursor()
        listaColdFoils = list()
        try:
            sql = "SELECT idColdFoil FROM coldfoil_ficha" \
                  " WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is not None:
                for reg in row:
                    listaColdFoils.append(int(reg[0]))

        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaColdFoils

    def eliminarReferencia(self,idColdFoil,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM coldfoil_ficha" \
                  " WHERE idColdFoil={0} and idFicha={1}" \
                .format(idColdFoil,
                        idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
class TBarnizFicha:
    def __init__(self, idTBarniz="", idFicha=""):
        self.__conn = conexion()
        self.__idTBarniz_Ficha = -1
        self.__idTBarniz = idTBarniz
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn

    def getIdTBarniz(self):
        return self.__idTBarniz
        pass

    def setIdTBarniz(self, value):
        self.__idTBarniz = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarTBarnizFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO tbarniz_ficha" \
                  " (idTBarniz, idFicha) VALUES({0},{1})" \
                .format(self.getIdTBarniz(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerTBarnizEnFicha(self, idFicha):
        cursor = self.getConn().cursor()
        listaTBarnizs = list()
        try:
            sql = "SELECT idTBarniz FROM tbarniz_ficha" \
                  " WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is not None:
                for reg in row:
                    listaTBarnizs.append(int(reg[0]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaTBarnizs

    def eliminarReferencia(self,idTBarniz,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM tbarniz_ficha" \
                  " WHERE idTBarniz={0} and idFicha={1}" \
                .format(idTBarniz,
                        idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass
class TroquelFicha:
    def __init__(self, idTroquel="", idFicha=""):
        self.__conn = conexion()
        self.__idTroquel_Ficha = -1
        self.__idTroquel = idTroquel
        self.__idFicha = idFicha

    def getConn(self):
        return self.__conn

    def getIdTroquel(self):
        return self.__idTroquel
        pass

    def setIdTroquel(self, value):
        self.__idTroquel = value
        pass

    def getIdFicha(self):
        return self.__idFicha
        pass

    def setIdFicha(self, value):
        self.__idFicha = value
        pass

    def insertarTroquelFicha(self):
        cursor = self.getConn().cursor()
        try:
            sql = "INSERT INTO troquel_ficha" \
                  " (idTroquel, idFicha) VALUES({0},{1})" \
                .format(self.getIdTroquel(),
                        self.getIdFicha())
            cursor.execute(sql)
        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True

    def leerTroquelEnFicha(self, idFicha):
        cursor = self.getConn().cursor()
        listaTroquels = list()
        try:
            sql = "SELECT idTroquel FROM troquel_ficha" \
                  " WHERE idFicha ={0}" \
                .format(idFicha)
            cursor.execute(sql)
            row = cursor.fetchall()
            if row is not None:
                for reg in row:
                    listaTroquels.append(int(reg[0]))
        except Exception:
            cursor.close()
            self.getConn().close()
            return None
        else:
            cursor.close()
            self.getConn().close()
            return listaTroquels

    def eliminarReferencia(self,idTroquel,idFicha):
        cursor = self.getConn().cursor()
        try:
            sql = "DELETE FROM troquel_ficha" \
                  " WHERE idTroquel={0} and idFicha={1}" \
                .format(idTroquel,
                        idFicha)
            cursor.execute(sql)

        except Exception:
            self.getConn().rollback()
            cursor.close()
            self.getConn().close()
            return False
        else:
            self.getConn().commit()
            cursor.close()
            self.getConn().close()
            return True
        pass


