"""Cliente.py: Description of what foobar does."""

__author__      = "Sergio Moratino & Sofian Naimi"
__copyright__   = "Copyright 2020, DAM"
from Cliente import Cliente
class ClienteView:


    def __init__(self):

        #self.txt_opt = "%sElija una opción: " % self.tab2
        self.txt_dni = "        DNI: "
        self.txt_cliente = "        Nombre: "
        self.txt_apellidos = "      Apellidos: " 
        self.txt_genero = "         Género: " 
        self.txt_direccion = "      Dirección: " 
        self.txt_nacimiento = "      Fecha de Nacimiento: "
        self.txt_postal = "      Cóidgo Postal: "
        pass
   
    ##OK##
    def mostrar_menu(self):
        """Vista del menú de opciones"""

        menu = """
        Menú del Gestor de Clientes
            (1) Crear un cliente
            (2) Ver listado de clientes
            (3) Editar un cliente
            (4) Eliminar un cliente

            (0) Salir

        """
        print (menu)

        opcion =   input()
        return opcion
    
    ##OK##
    def crear_cliente(self):
        """Vista del formulario para crear nuevo cliente"""

        print ("""
        CREAR UN NUEVO CLIENTE
        """)
        dni = input(self.txt_dni)
        nombre = input(self.txt_cliente)
        apellidos = input(self.txt_apellidos)
        genero = input(self.txt_genero)
        direccion = input(self.txt_direccion)
        nacimiento = input(self.txt_nacimiento)
        postal = input(self.txt_postal)



        return (dni, nombre, apellidos, genero, direccion, nacimiento, postal)

    def confirmar_creacion(self):
        """Vista de confirmación de creación de nuevo cliente"""

        print( """
        Cliente creado con éxito!
        """)
    ##OK##
    def listar_clientes(self, listado):
        """Vista para el listado de clientes"""

        print ("""
            LISTADO DE CLIENTES:
        """)
        for row in listado:
            dni = row[0]
            cliente = row[1]
            apellidos = row[2]
            genero = row[3]
            direccion = row[4]
            fNacimiento = row[5]
            codPostal = row[6]
            
            print ("[%s] %s %s | Género:%s | Dirección:%s | Nacimiento:%s | Código Postal:%s" % (dni, cliente, apellidos, genero, direccion, fNacimiento, codPostal))

    def editar_cliente(self, listado):
        """Vista del formulario para editar un cliente"""

        print ("\n\n")
        dni = input(self.txt_dni)
        print ("\n")
        cliente = input(self.txt_cliente)
        apellidos = input(self.txt_apellidos)
        genero = input(self.txt_genero)
        direccion = input(self.txt_direccion)
        fNacimiento = input(self.txt_nacimiento)
        codPostal = input(self.txt_postal)
        return (dni, cliente, apellidos, genero, direccion, fNacimiento, codPostal)

    def confirmar_editar_cliente(self):
        """Vista de confirmación de edición"""

        print ("""
        Cliente editado correctamente.
        """)

    def eliminar_cliente(self, listado):
        """Vista de formulario para eliminar cliente"""

        self.listar_clientes(listado)
        print ("\n\n")
        dni = input(self.txt_dni)
        print ("\n")
        return dni

    def confirmar_eliminar_cliente(self):
        """Vista de cofirmación eliminar cliente"""
        print ("""
        Cliente eliminado correctamente.
        """)
