# -*- coding:iso-8859-2 -*-from PyQt4 import QtCore, QtGui,QtSql
import MySQLdb
import sys
def conexion():
    try:
        conn = MySQLdb.connect(host="192.168.0.201", user="practica", passwd="admin", db="practica")
    except MySQLdb.Error:
        print("Error al establecer conexion")
        sys.exit(1)
    else:
        return conn
def Conexion(db):
    db.setHostName("192.168.0.201")
    db.setDatabaseName("practica")
    db.setUserName("practica")
    db.setPassword("admin")
    if (db.open() == False):
        QtGui.QMessageBox.critical(None, "Database Error",
                                   db.lastError().text())

