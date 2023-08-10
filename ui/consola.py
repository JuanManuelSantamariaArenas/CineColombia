import sys
from mundo.cine import Cine
from mundo.excepciones import *

class Consola:

    def __init__(self) -> None:
        self.cine = Cine()
        self.cine.cargar()
        self.opciones = {
            "1": self.registrar_usuario,
            "2": self.buscar_pelicula,
            "3": self.reservar_ticket,
            "4": self.cancelar_ticket,
            "5": self.salir_app,
        }

    def mostrar_menu(self):
        print("""
        \n
        BIENVENIDO A CINECOLOMBIA
        |||||||||||||||||||||||||||||||||||
        Menú de opciones:\n
        1. Registrar usuario
        2. Buscar pelicula
        3. Reservar ticket
        4. Cancelar ticket
        5. Salir de la aplicacion
        |||||||||||||||||||||||||||||||||||
        """)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opcion del menu: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"INFO: {opcion} NO ES UNA OPCIÓN VALIDA")
    
    def registrar_usuario(self):
        print("\n- REGISTRAR USUARIO -\n")
        dni = int(input("Ingrese el número de identificación: "))
        nombre = input("Ingrese el nombre completo: ")
        edad = int(input("Ingrese la edad: "))
        self.cine.resgistrar_usuario(dni, nombre, edad)
    
    def buscar_pelicula(self):
        print("\n- BUSCAR PELICULA -\n")
        nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
        pelicula = self.cine.buscar_pelicula(nombre_pelicula)
        if pelicula != False:
            pelicula = pelicula[1]
            print(f"La pelicula {nombre_pelicula} se encuentra disponible en la sala # {pelicula.num_sala}")
        else: 
            print(f"La pelicula {nombre_pelicula} no se encuentra disponible")

    def reservar_ticket(self):
        print("\n- RESERVAR TICKET -\n")
        dni = int(input("Ingrese el número de identificación: "))
        nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
        self.cine.reservar_ticket(dni, nombre_pelicula)

    def cancelar_ticket(self):
        print("\n- CANCELAR TICKET -\n")
        num_ticket = input("Ingrese el número del ticket: ")
        dni = int(input("Ingrese el número de identificación: "))
        self.cine.cancelar_ticket(num_ticket, dni)

    def salir_app(self):
        print("\nMUCHAS GRACIAS POR USAR LA APLICACIÓN")
        self.cine.guardar()
        sys.exit(0)
