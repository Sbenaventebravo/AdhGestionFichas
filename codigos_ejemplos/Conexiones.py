def Conexion(db):
    db.setHostName("192.168.0.201")
    db.setDatabaseName("practica")
    db.setUserName("practica")
    db.setPassword("admin")
    if (db.open() == False):
        QtGui.QMessageBox.critical(None, "Database Error",
                                   db.lastError().text())