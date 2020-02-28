# -*- coding: utf-8 *-*
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

    def crear_cliente_controller(self):
        """Controlador para creación de nuevo país"""
        (cliente_dni, cliente_nombre, cliente_apellidos, cliente_genero, cliente_direccion, cliente_nacimiento) = self.vista.crear_cliente()
        cliente = Cliente()
        cliente.dni = cliente_dni
        cliente.nombre = cliente_nombre
        cliente.apellidos = cliente_apellidos
        cliente.genero = cliente_genero
        cliente.direccion = cliente_direccion
        cliente.fNacimiento = cliente_nacimiento
        cliente.create()
        self.vista.confirmar_creacion()
        self.cliente_controller()

    def traer_clientes(self):
        """Trae una lista de todos los países"""
        cliente = Cliente()
        listado = cliente.read_all()
        return listado

    def listar_clientes_controller(self):
        """Controlador del listado de países"""
        listado = self.traer_clientes()
        self.vista.listar_clientes(listado)
        self.cliente_controller()

    def editar_clientes_controller(self):
        """Controlador para editar un país"""
        listado = self.traer_clientes
        (id, nombre, abbr) = self.vista.editar_cliente(listado)
        cliente = Cliente()
        cliente.dNI = dNi
        cliente.nombre = nombre
        cliente.apellidos = apellidos
        cliente.update()
        self.vista.confirmar_editar_cliente()
        self.cliente_controller()

    def eliminar_cliente_controller(self):
        """Controlador para eliminar un país"""
        listado = self.traer_clientes()
        id = self.vista.eliminar_cliente(listado)
        id = int(id)
        cliente = Cliente()
        cliente.dNI = dNi
        cliente.delete()
        self.vista.confirmar_eliminar_cliente()
        self.cliente_controller()


controller = ClienteController()

