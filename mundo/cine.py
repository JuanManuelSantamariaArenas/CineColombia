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
        return

class Ticket:

    def __init__(self, fecha: str, num_sala: int, asiento: str, dni_usuario: int, pelicula: Pelicula):
        self.fecha = fecha
        self.num_sala = num_sala
        self.asiento =  asiento
        self.dni_usuario = dni_usuario
        self.pelicula = pelicula

    def __str__(self) -> str:
        pass

class Usuario:

    def __init__(self, dni: int, nombre: str, edad: int, ticket: Ticket):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.ticket = ticket
    
    def __str__(self) -> str:
        return f"{self.dni}   {self.nombre}   {self.edad}   {self.numero_ticket}"

class Cine:

    def __init__(self) -> None:
        pass
