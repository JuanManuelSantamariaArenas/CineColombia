import random


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

class Ticket:

    def __init__(self, fecha: str, num_sala: int, asiento: str, dni_usuario: int, pelicula: Pelicula):
        self.fecha = fecha
        self.num_sala = num_sala
        self.asiento =  asiento
        self.dni_usuario = dni_usuario
        self.pelicula = pelicula

    def __str__(self) -> str:
        return f"Fecha: {self.fecha} \n Numero de sala: {self.num_sala} \n Asiento: {self.asiento} \n Dni del usuario: {self.dni_usuario} \n Pelicula: {self.pelicula}"

class Usuario:

    def __init__(self, dni: int, nombre: str, edad: int, ticket: Ticket):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.ticket = ticket
    
    def __str__(self) -> str:
        return f"{self.dni}   {self.nombre}   {self.edad}   {self.numero_ticket}"

class Cine:

    def __init__(self):
        self.peliculas: dict[str: Pelicula] = {}
        self.salas: dict[int: Sala] = {}
        self.usuarios: dict[int: Usuario] = {}

    def leer_peliculas(self):
        datos_uno = []
        datos_finales = []
        with open("peliculas.txt") as file:
            for lineas in file:
                datos_uno.append(lineas.strip("\n"))
            for lineas in file:
                datos_finales.append(lineas.split(","))
            for datos in datos_finales:
                pelicula = Pelicula(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
                self.peliculas[pelicula.titulo] = pelicula
        return

def programa():
    cine_uno = Cine()
    cine_uno.leer_peliculas()
    print(cine_uno.peliculas)
    return
programa()
