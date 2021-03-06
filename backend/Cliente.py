# -*- coding: utf-8 *-*
#!/usr/bin/env python

"""Cliente.py: Description of what foobar does."""

__author__      = "Sergio Moratino & Sofian Naimi"
__copyright__   = "Copyright 2020, DAM"
from db_conn import DBConn


class Cliente:

    def __init__(self):
        self.dni = ''
        self.nombre = ''
        self.apellidos = ''
        self.genero = ''
        self.direccion = ''
        self.fNacimiento = ''
        self.codPostal = ''
        self.db = DBConn()

    ##OK##
    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO Clientes (DNI, Nombre, Apellidos, Género, Dirección, FNacimiento, CódigoPostal) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.dni, self.nombre, self.apellidos, self.genero, self.direccion, self.fNacimiento, self.codPostal)
        self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE Clientes SET Nombre = %s, Apellidos = %s, Género = %s, Dirección = %s, FNacimiento = %s, CódigoPostal = %s WHERE DNI = %s"
        values = ( self.nombre, self.apellidos, self.genero, self.direccion, self.fNacimiento, self.codPostal, self.dni)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT DNI, Nombre, Apellidos, Género, Dirección, FNacimiento, CódigoPostal FROM Clientes"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT DNI"
        values = (self.dni)
        return self.db.ejecutar(query, values)

    def delete(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM Clientes WHERE DNI = %s"
        values = self.dni
        return self.db.ejecutar(query, values)
