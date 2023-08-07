import random
import datetime


class Pelicula:

    def __init__(self, titulo: str, genero: str, productora: str, publicacion: int, duracion: float, retriccion_edad: str, calificacion: int):
        self.titulo = titulo
        self.genero = genero
        self.productora = productora
        self.publicacion = publicacion
        self.duracion = duracion
        self.retriccion_edad = retriccion_edad  
        self.calificacion = calificacion
    
    def __str__(self) -> str:
        return f"Titulo: {self.titulo} \n Genero: {self.genero} \n Productora: {self.productora} \n Publicacion: {self.publicacion} \n Duracion: {self.duracion} \n Restriccion de edad: {self.retriccion_edad} \n Calificacion: {self.calificacion}"

class Sala:

    def __init__(self, num_sala: int, num_asientos: int, pelicula: Pelicula):
        self.num_sala = num_sala
        self.num_asientos = num_asientos
        self.pelicula = pelicula

    def __str__(self) -> str:
        return f"Numero de sala: {self.num_sala}, Numero de asientos: {self.num_asientos}, Pelicula: {self.pelicula}"

    def asiento_disponible(num_asiento: int) -> bool:
        pass

class Ticket:

    def __init__(self, num_ticket: int, fecha: str, num_sala: int, asiento: str, dni_usuario: int, pelicula: Pelicula):
        self.num_ticket = num_ticket
        self.fecha = fecha
        self.num_sala = num_sala
        self.asiento =  asiento
        self.dni_usuario = dni_usuario
        self.pelicula = pelicula

    def __str__(self) -> str:
        return f"Numero de ticket: {self.num_ticket} \n Fecha: {self.fecha} \n Numero de sala: {self.num_sala} \n Asiento: {self.asiento} \n Dni del usuario: {self.dni_usuario} \n Pelicula: {self.pelicula}"

class Usuario:

    def __init__(self, dni: int, nombre: str, edad: int):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.tickets: dict[int: Ticket] = {}
    
    def __str__(self) -> str:
        return f"{self.dni}   {self.nombre}   {self.edad}   {self.tickets}"

    def adquirir_ticket(self, datos_ticket: list):
        num_ticket = datos_ticket[0] 
        fecha = datos_ticket[1]
        num_sala = datos_ticket[2]
        asiento = datos_ticket[3]
        dni_usuario = datos_ticket[4]
        pelicula = datos_ticket[5]
        ticket = Ticket(num_ticket, fecha, num_sala, asiento, dni_usuario, pelicula)
        self.tickets[num_ticket] = ticket

class Cine:

    def __init__(self):
        self.peliculas: dict[str: Pelicula] = {}
        self.salas: dict[int: Sala] = {}
        self.tickets: dict[int: Ticket] = {}
        self.usuarios: dict[int: Usuario] = {}

    def leer_peliculas(self):
        datos_uno = []
        datos_finales = []
        with open("peliculas.txt") as file:
            for lineas in file:
                datos_uno.append(lineas.strip("\n"))
            for lineas in datos_uno:
                datos_finales.append(lineas.split(","))
            for datos in datos_finales:
                pelicula = Pelicula(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
                self.peliculas[pelicula.titulo] = pelicula
        return
    
    def buscar_usuario(self, dni_usuario: int):
        for usuario in self.usuarios.values():
            if usuario.dni == dni_usuario:
                return usuario
        return None
    
    def buscar_pelicula(self, nombre_pelicula):
        for pelicula in self.peliculas.values():
            if pelicula.titulo == nombre_pelicula:
                return pelicula
        return None
    
    def resgistrar_usuario(self, dni: int, nombre: str, edad: str):
        pass

    def reservar_ticket():
        pass

def programa():
    cine_uno = Cine()
    cine_uno.leer_peliculas()
    return
programa()
