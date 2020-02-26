from Cliente import Cliente
class ClienteView:


    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3
        self.tab4 = "    " * 4
        self.tab5 = "    " * 5
        self.tab6 = "    " * 6
        self.txt_opt = "%sElija una opción: " % self.tab2
        self.txt_dni = "%sDNI: " % self.tab1
        self.txt_cliente = "%sNombre: " % self.tab2
        self.txt_apellidos = "%sApellidos: " % self.tab3
        self.txt_genero = "%sGénero: " % self.tab4
        self.txt_direccion = "%sDirección: " % self.tab5
        pass

    def mostrar_menu(self):
        """Vista del menú de opciones"""

        menu = """
        Menú del Gestor de Países
            (1) Crear un país
            (2) Ver listado de países
            (3) Editar un país
            (4) Eliminar un país

            (0) Salir

        """
        print (menu)

        opcion =   input()
        return opcion

    def crear_cliente(self):
        """Vista del formulario para crear nuevo país"""

        print ("""
        CREAR UN NUEVO CLIENTE
        """)
        dni = input(self.txt_dni)
        nombre = input(self.txt_cliente)
        apellidos = input(self.txt_apellidos)
        genero = input(self.txt_genero)
        direccion = input(self.txt_direccion)


        return (dni, nombre, apellidos, genero, direccion)

    def confirmar_creacion(self):
        """Vista de confirmación de creación de nuevo país"""

        print( """
        País creado con éxito!
        """)

    def listar_clientes(self, listado):
        """Vista para el listado de países"""

        print ("""
            LISTADO DE PAÍSES:
        """)
        for row in listado:
            id = row[0]
            cliente = row[1]
            apellidos = row[2]
            print ("%s[%s] %s (%s)" % (self.tab3, id, cliente, apellidos))

    def editar_cliente(self, listado):
        """Vista del formulario para editar un país"""

        self.listar_clientes(listado)
        print ("\n\n")
        id = raw_input(self.txt_id)
        print ("\n")
        cliente = raw_input(self.txt_cliente)
        apellidos = raw_input(self.txt_apellidos)
        return (id, cliente, apellidos)

    def confirmar_editar_cliente(self):
        """Vista de confirmación de edición"""

        print ("""
        País editado correctamente.
        """)

    def eliminar_cliente(self, listado):
        """Vista de formulario para eliminar país"""

        self.listar_clientes(listado)
        print ("\n\n")
        id = raw_input(self.txt_id)
        print ("\n")
        return id

    def confirmar_eliminar_cliente(self):
        """Vista de cofirmación eliminar país"""
        print ("""
        País eliminado correctamente.
        """)
