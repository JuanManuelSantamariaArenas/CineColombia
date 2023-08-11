import random
import datetime
import string
import pickle

class Pelicula:

    def __init__(self, titulo: str, genero: str, productora: str, publicacion: int, duracion: float, retriccion_edad: str, calificacion: int, hora_transmision: datetime):
        self.titulo = titulo
        self.genero = genero
        self.productora = productora
        self.publicacion = publicacion
        self.duracion = duracion
        self.retriccion_edad = retriccion_edad  
        self.calificacion = calificacion
        self.hora_transmision = hora_transmision
    
    def __str__(self) -> str:
        return f"Titulo: {self.titulo} \n Genero: {self.genero} \n Productora: {self.productora} \n Publicacion: {self.publicacion} \n Duracion: {self.duracion} \n Restriccion de edad: {self.retriccion_edad} \n Calificacion: {self.calificacion} \n Hora de transmisión: {self.hora_transmision}"

class Sala:

    def __init__(self, num_sala: int, num_asientos: int, pelicula: Pelicula):
        self.num_sala = num_sala
        self.num_asientos = num_asientos
        self.asientos: list = []
        self.codigos_asientos: dict[str:int] = {} # Value: dni usuario
        self.pelicula = pelicula

    def __str__(self) -> str:
        return f"Numero de sala: {self.num_sala}, Numero de asientos: {self.num_asientos}, Pelicula: {self.pelicula}"

    def generar_asientos(self):
        alfabeto = list(string.ascii_uppercase)
        alfabeto = alfabeto[:-16]
        alfabeto.reverse()
        num_filas = len(alfabeto)
        num_asientos_por_fila = self.num_asientos // num_filas # num de columnas
        for filas in range(0, num_filas):
            self.asientos.append([" "]*num_asientos_por_fila)
        contador = 0
        for letra in alfabeto:
            for numero in range(1, num_asientos_por_fila + 1):
                codigo_asiento =  letra + str(numero)
                self.codigos_asientos[codigo_asiento] = ""
                self.asientos[contador][numero - 1] = codigo_asiento
            contador += 1
        return

    def asientos_disponibles(self):
        asientos_disponibles = []
        for asiento, ocupante in self.codigos_asientos.items():
            if ocupante == "":
                asientos_disponibles.append(asiento)
        return asientos_disponibles

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
        self.autenticacion: bool = None

    def leer_peliculas(self):
        datos_uno = []
        datos_finales = []
        with open("peliculas.txt") as file:
            for lineas in file:
                datos_uno.append(lineas.strip("\n"))
            for lineas in datos_uno:
                datos_finales.append(lineas.split(","))
            for datos in datos_finales:
                pelicula = Pelicula(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])
                self.peliculas[pelicula.titulo] = pelicula
        return
    
    def pista_contraseña(self):
        fecha_actual = datetime.date.today()
        print(f"PISTA: {fecha_actual}")
        fragmento_uno = int(fecha_actual.day) * int(fecha_actual.month) + int(fecha_actual.day)
        fragmento_dos = int(fecha_actual.day) * int(fecha_actual.month) - int(fecha_actual.day)
        fragmento_tres = int(fecha_actual.day) * int(fecha_actual.day) - int(fecha_actual.day)
        fragmento_cuatro = int(fecha_actual.month) * int(fecha_actual.month) + int(fecha_actual.month)       
        contraseña = str(fragmento_uno) + str(fragmento_dos) + str(fragmento_tres) + str(fragmento_cuatro) + "001"
        return contraseña
    
    def crear_salas(self, num_salas_crear: int):
        for num_sala in range(0, num_salas_crear):
            print(f"\nCREACIÓN DE LA SALA # {num_sala + 1}")
            num_asientos = int(input("\n-- Ingrese el número de asientos: "))
            if num_asientos % 10 == 0 and num_asientos >=100:
                pelicula = ""
                sala = Sala(num_sala + 1, num_asientos, pelicula)
                sala.generar_asientos()
                self.salas[sala.num_sala] = sala
                print(f"\n * INFO: SE CREO LA SALA # {num_sala + 1} EXITOSAMENTE")
            else:
                print("\n * INFO: DEBE CUMPLIR DOS CONDICIONES: # ASIENTOS >= 100  Y SER / POR 10\n") 
        return

    def asignar_peli_sala(self):
        num_sala = int(input("-- Ingrese el número de la sala: "))
        sala = self.buscar_sala(num_sala)
        if sala != False:
            nombre_pelicula = input("-- Ingrese el nombre de la pelicula: ")
            pelicula = self.buscar_pelicula(nombre_pelicula)
            if  pelicula.titulo == nombre_pelicula:
                sala.pelicula = nombre_pelicula
                print(f" * INFO: SE ASIGNO LA PELICULA {nombre_pelicula} A LA SALA # {num_sala} EXITOSAMENTE")
            else:
                print(f" * INFO: LA PELICULA {nombre_pelicula} NO EXISTE") 
        else:
            print(f" * INFO: LA SALA # {num_sala} NO EXISTE")
        return
        

    def eliminar_sala(self):
        num_sala = int(input("-- Ingrese el número de la sala: "))
        sala = self.buscar_sala(num_sala)
        if sala != False:
            del self.salas[sala.num_sala]
        else:
            print(f" * INFO: LA SALA # {num_sala} NO EXISTE")
        return

    def resgistrar_usuario(self, dni: int, nombre: str, edad: str):
        if dni != "" and nombre != "" and edad != "":
            if not self.buscar_usuario(dni):
                usuario = Usuario(dni, nombre, edad)
                self.usuarios[dni] = usuario
                print(" * INFO: SE REALIZO EL REGISTRO EXITOSAMENTE")
            else:
                print(" * INFO: NO ES POSIBLE REALIZAR EL REGISTRO")
        else:
            print("DEBES DE INGRESAR LOS DATOS SOLICITADOS")
        return
    
    def buscar_usuario(self, dni_usuario: int):
        for usuario in self.usuarios.values():
            if usuario.dni == dni_usuario:
                return usuario
        return False
    
    def buscar_sala(self, num_sala: int):
        for sala_actual in self.salas.values():
            if sala_actual.num_sala == num_sala:
                return sala_actual
        return False

    def buscar_pelicula(self, nombre_pelicula):
        for pelicula in self.peliculas.values():
            if pelicula.titulo == nombre_pelicula:
                for sala in self.salas.values():
                    if sala.pelicula == nombre_pelicula:
                        return [pelicula, sala]
                return pelicula
        return False
    
    def asignar_asiento(self, sala: Sala, usuario: Usuario):
        asientos_disponibles = sala.asientos_disponibles()
        if len(usuario.tickets) > 0:
            log_dni = str(usuario.dni)
            log_dni = len(log_dni)
            asiento = list(usuario.tickets.keys()) 
            asiento = asiento[0]
            columna = int(asiento[1:-log_dni])
            fila = asiento[0]
            for asiento_libre in asientos_disponibles:
                 if asiento_libre[0] == fila:
                    num_asiento = asiento_libre[1:]
                    num_asiento = int(num_asiento)
                    for salto in range(1, 5):
                        if num_asiento == columna - salto or num_asiento == columna + salto:
                            asiento_adquirido = asiento_libre
                            return asiento_adquirido
        else:
            asiento_adquirido = random.choice(asientos_disponibles)
            return asiento_adquirido

    def habilitar_asiento(self, sala: Sala, asiento: str):
        function = "Habilitar"
        for asiento_actual in sala.codigos_asientos.keys():
            if asiento_actual == asiento:
                sala.codigos_asientos[asiento_actual] = ""
                # self.colorear_asiento(sala, asiento_actual, function)
        return

    def deshabilitar_asiento(self, sala: Sala, asiento: str, dni: int):
        function = "Deshabilitar"
        for asiento_actual in sala.codigos_asientos.keys():
            if asiento_actual == asiento:
                sala.codigos_asientos[asiento_actual] = dni
                # self.colorear_asiento(sala, asiento_actual, function)
        return
    
    def colorear_asiento(self, sala: Sala, asiento: str, hab_des: str):
        funcion = ["Habilitar", "Deshabilitar"]
        if funcion[0] == hab_des:
            for fila in range(0, len(sala.asientos)):
                for columna in range(0, len(sala.asientos[0])):
                    if sala.asientos[fila][columna] == asiento:
                        sala.asientos[fila][columna] == asiento
        elif funcion[1] ==  hab_des:
            for fila in range(0, len(sala.asientos)):
                for columna in range(0, len(sala.asientos[0])):
                    if sala.asientos[fila][columna] == asiento:
                        sala.asientos[fila][columna] == asiento
        return

    def reservar_ticket(self, dni: int, pelicula: str):
        usuario = self.buscar_usuario(dni)
        fecha = datetime.date.today()
        sala = self.buscar_pelicula(pelicula)
        sala = sala[1]
        asiento = self.asignar_asiento(sala, usuario)
        num_ticket = asiento + str(dni)
        print(num_ticket)
        datos_ticket = [num_ticket, fecha, sala.num_sala, asiento, dni, pelicula]
        usuario.adquirir_ticket(datos_ticket)
        self.deshabilitar_asiento(sala, asiento, dni)
        print(f"\n * INFO: SE RESERVO EL TICKET {num_ticket} EXITOSAMENTE")
        return
    
    def cancelar_ticket(self, num_ticket: str, dni: int):
        usuario = self.buscar_usuario(dni)
        tickets = usuario.tickets
        log_dni = str(usuario.dni)
        log_dni = len(log_dni)
        datos_ticket = [[cod_ticket[:-log_dni], ticket] for cod_ticket, ticket in tickets.items() if cod_ticket == num_ticket]
        sala = datos_ticket[0][1].num_sala
        for sala_usuario in self.salas.values():
            if sala_usuario.num_sala == sala:
                sala = sala_usuario
        self.habilitar_asiento(sala, datos_ticket[0][0])
        del datos_ticket[0][1]
        print(f"\n * INFO: SE CANCELO EL TICKET {num_ticket} EXITOSAMENTE")
        return

    def guardar(self):
        with open("historial.txt", "wb") as file:
            pickle.dump(self, file)
    
    def cargar(self):
        with open("historial.txt", "rb") as file:
            cine = pickle.load(file)
            cine.leer_peliculas()
            self.usuarios = cine.usuarios
            #self.salas = cine.salas
            self.peliculas = cine.peliculas
"""
    print(sala_uno.codigos_asientos)
    num_ticket = input("-- Ingrese tick: ")
    dni = int(input("-- Ingrese dni: "))
    cine_uno.cancelar_ticket(num_ticket, dni)
    print(sala_uno.codigos_asientos)
    return
programa()"""