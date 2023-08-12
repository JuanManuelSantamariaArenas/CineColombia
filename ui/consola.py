import sys
from mundo.cine import Cine
from mundo.excepciones import *

class Consola:

    def __init__(self) -> None:
        self.cine = Cine()
        self.cine.cargar()
        self.opciones_admon = {
            "1": self.autentificar_admon,
            "2": self.crear_salas,
            "3": self.asignar_peli_sala,
            "4": self.eliminar_sala,
            "5": self.actualizar_peliculas,
            "6": self.salir_menu_admon,
        }
        self.opciones_usuario = {
            "1": self.registrar_usuario,
            "2": self.buscar_pelicula,
            "3": self.reservar_ticket,
            "4": self.cancelar_ticket,
            "5": self.actualizar_peliculas,
            "6": self.salir_app,
        }

    def mostrar_menu_admon(self):
        print("""
        \n
        BIENVENIDO A CINECOLOMBIA
        |||||||||||||||||||||||||||||||||||
        Menú de opciones para administrador:\n
        1. Autenticar admon
        2. Crear salas
        3. Asignar pelicula a una sala
        4. Eliminar sala
        5. Actualizar peliculas
        6. Salir del menu del administrador
        
        NOTA: ANTES QUE TODO DEBES AUTENTICARTE COMO ADMON
        |||||||||||||||||||||||||||||||||||
        """)

    def mostrar_menu_usuario(self):
        print("""
        \n
        BIENVENIDO A CINECOLOMBIA
        |||||||||||||||||||||||||||||||||||
        Menú de opciones para usuario:\n
        1. Registrar usuario
        2. Buscar pelicula
        3. Reservar ticket
        4. Cancelar ticket
        5. Actualizar peliculas
        6. Salir de la aplicacion
        |||||||||||||||||||||||||||||||||||
        """)

    def ejecutar_admon(self):
        while True:
            self.mostrar_menu_admon()
            opcion = input("Seleccione una opcion del menu: ")
            accion = self.opciones_admon.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f" * INFO: {opcion} NO ES UNA OPCIÓN VALIDA")

    def autentificar_admon(self):
        print("\n- AUTENTICAR ADMINISTRADOR -\n")
        usuario_admon = input("Usuario: ")
        if usuario_admon == "artlee":
            contraseña_admon = self.cine.pista_contraseña()
            contraseña = input("Contraseña: ")
            if contraseña == contraseña_admon:
                self.cine.autenticacion = True
                print(" * INFO: SE AUTENTIFICO EL ADMON CORRECTAMENTE")
                return
            else:
                print(" * INFO: CONTRASEÑA INCORRECTA")
        else: 
            print(f" * INFO: EL USUARIO {usuario_admon} NO CORRESPONDE AL DEL ADMINISTRADOR")
            self.cine.autenticacion = False
            return
    
    def crear_salas(self):
        print("\n- CREAR SALAS -\n") 
        if self.cine.autenticacion:
            num_salas_crear = int(input("-- Ingrese el número de salas que desea crear: "))
            self.cine.crear_salas(num_salas_crear)
        else:
            print(" * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR")

    def asignar_peli_sala(self):
        print("\n- ASIGNACION DE PELICULA A UNA SALA -\n") 
        if self.cine.autenticacion:
            if len(self.cine.salas) > 0:
                self.cine.asignar_peli_sala()
            else:
                print(" * INFO: PRIMERO DEBES CREAR LAS SALAS DEL CINE")
        else:
            print(" * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR")

    def eliminar_sala(self):
        print("\n- ELIMINAR SALA -\n")
        if self.cine.autenticacion:
            self.cine.eliminar_sala()
        else:
            print(" * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR") 
    
    def salir_menu_admon(self):
        if len(self.cine.salas) > 0:
            print("\nGRACIAS POR ADMINISTRAR EL CINE, HAS CERRADO SESION COMO ADMON\n")
            self.ejecutar_usuario()
        else:
            print(" * INFO: PRIMERO DEBES CREAR LAS SALAS DEL CINE")

    def actualizar_peliculas(self):
        self.cine.actualizar_peliculas()

    def ejecutar_usuario(self):
        while True:
            self.mostrar_menu_usuario()
            opcion = input("Seleccione una opcion del menu: ")
            accion = self.opciones_usuario.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f" * INFO: {opcion} NO ES UNA OPCIÓN VALIDA")
    
    def registrar_usuario(self):
        print("\n- REGISTRAR USUARIO -\n")
        dni = int(input("-- Ingrese el número de identificación: "))
        nombre = input("-- Ingrese el nombre completo: ")
        edad = int(input("-- Ingrese la edad: "))
        self.cine.resgistrar_usuario(dni, nombre, edad)
    
    def buscar_pelicula(self):
        print("\n- BUSCAR PELICULA -\n")
        nombre_pelicula = input("-- Ingrese el nombre de la pelicula: ")
        datos = self.cine.buscar_pelicula(nombre_pelicula)
        if datos != False:
            pelicula = datos[0]
            sala = datos[1]
            print(f" * INFO: LA PELICULA {nombre_pelicula} SE ENCUENTRA DISPONIBLE EN LA SALA # {sala.num_sala} Y INICIA A LAS {pelicula.hora_transmision}")
        else: 
            print(f" * INFO: LA PELICULA {nombre_pelicula} NO SE ENCUENTRA DISPONIBLE")

    def reservar_ticket(self):
        print("\n- RESERVAR TICKET -\n")
        dni = int(input("-- Ingrese el número de identificación: "))
        nombre_pelicula = input("-- Ingrese el nombre de la pelicula: ")
        self.cine.reservar_ticket(dni, nombre_pelicula)

    def cancelar_ticket(self):
        print("\n- CANCELAR TICKET -\n")
        num_ticket = input("-- Ingrese el número del ticket: ")
        dni = int(input("-- Ingrese el número de identificación: "))
        self.cine.cancelar_ticket(num_ticket, dni)

    def salir_app(self):
        print("\nMUCHAS GRACIAS POR USAR LA APLICACIÓN 👏🏻👍👏🏻")
        self.cine.guardar()
        sys.exit(0)