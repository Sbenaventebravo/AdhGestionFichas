import sys
import MySQLdb
def conexion():
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="practica")
    except MySQLdb.Error:
        print("Error al establecer conexion")
        sys.exit(1)
    else:
        return conn

con = conexion()