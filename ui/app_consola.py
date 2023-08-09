from mundo.cine import Cine
from mundo.excepciones import *

class Consola:

    def __init__(self) -> None:
        self.cine = Cine()
        #self.cine.cargar()
        self.opciones = {
            "1": self.registrar_usuario,
            "2": self.buscar_pelicula,
            "3": self.reservar_ticket,
            "4": self.cancelar_ticket,
        }

    def mostrar_menu(self):
        print("""
        \n
        BIENVENIDO A RENTUARIO
        |||||||||||||||||||||||||||||||||||
        Menú de opciones:\n
        1. Registrar usuario
        2. Buscar pelicula
        3. Reservar ticket
        4. Cancelar ticket
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
        print("- REGISTRAR USUARIO -")
        dni = int(input("Ingrese el número de identificación: "))
        nombre = input("Ingrese el nombre completo: ")
        edad = int(input("Ingrese la edad: "))
        self.cine.resgistrar_usuario(dni, nombre, edad)
    
    def buscar_pelicula(self):
        print("- BUSCAR PELICULA -")
        nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
        self.cine.buscar_pelicula(nombre_pelicula)

    def reservar_ticket(self):
        dni = int(input("Ingrese el número de identificación: "))
        nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
        self.cine.reservar_ticket(dni, nombre_pelicula)

    def cancelar_ticket(self):
        num_ticket = input("Ingrese el número del ticket: ")
        dni = int(input("Ingrese el número de identificación: "))
        self.cine.cancelar_ticket(num_ticket, dni)
