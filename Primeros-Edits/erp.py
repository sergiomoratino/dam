#!/usr/bin/python3
import conexion
from clientes import clientes


print(clientes.consultaRegistro("SELECT Nombre from Clientes",1))

