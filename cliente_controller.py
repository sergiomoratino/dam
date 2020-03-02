# -*- coding: utf-8 *-*
"""Cliente.py: Description of what foobar does."""

__author__      = "Sergio Moratino & Sofian Naimi"
__copyright__   = "Copyright 2020, DAM"
from Cliente import Cliente
from cliente_view import ClienteView


class ClienteController:

    def __init__(self):
        self.vista = ClienteView()
        self.cliente_controller()

    def cliente_controller(self):
        """Controlador general de Cliente"""
        peticion = self.vista.mostrar_menu()
        self.peticion = int(peticion)

        if self.peticion == 1:
            self.crear_cliente_controller()
        elif self.peticion == 2:
            self.listar_clientes_controller()
        elif self.peticion == 3:
            self.editar_clientes_controller()
        elif self.peticion == 4:
            self.eliminar_cliente_controller()

    ##OK##
    def crear_cliente_controller(self):
        """Controlador para creación de nuevo cliente"""
        (cliente_dni, cliente_nombre, cliente_apellidos, cliente_genero, cliente_direccion, cliente_nacimiento, cliente_postal) = self.vista.crear_cliente()
        cliente = Cliente()
        cliente.dni = cliente_dni
        cliente.nombre = cliente_nombre
        cliente.apellidos = cliente_apellidos
        cliente.genero = cliente_genero
        cliente.direccion = cliente_direccion
        cliente.fNacimiento = cliente_nacimiento
        cliente.codPostal = cliente_postal
        cliente.create()
        self.vista.confirmar_creacion()
        self.cliente_controller()

    def traer_clientes(self):
        """Trae una lista de todos los Clientes"""
        cliente = Cliente()
        listado = cliente.read_all()
        return listado

    def listar_clientes_controller(self):
        """Controlador del listado de clientes"""
        listado = self.traer_clientes()
        self.vista.listar_clientes(listado)
        self.cliente_controller()

    def editar_clientes_controller(self):
        """Controlador para editar un cliente"""
        listado = self.traer_clientes
        (dni, nombre, apellidos, genero, direccion, fNacimiento, codPostal) = self.vista.editar_cliente(listado)
        cliente = Cliente()
        cliente.dni = dni
        cliente.nombre = nombre
        cliente.apellidos = apellidos
        cliente.genero = genero
        cliente.direccion = direccion
        cliente.fNacimiento = fNacimiento
        cliente.codPostal = codPostal
        cliente.update()
        self.vista.confirmar_editar_cliente()
        self.cliente_controller()

    def eliminar_cliente_controller(self):
        """Controlador para eliminar un cliente"""
        listado = self.traer_clientes()
        dni = self.vista.eliminar_cliente(listado)        
        cliente = Cliente()
        cliente.dni = dni
        cliente.delete()
        self.vista.confirmar_eliminar_cliente()
        self.cliente_controller()

controller = ClienteController()

