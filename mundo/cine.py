import random
import datetime
import string
import pickle
from nltk.tokenize import word_tokenize
import numpy as np

class Pelicula:

    def __init__(self, titulo: str, genero: str, productora: str, publicacion: int, duracion: int, retriccion_edad: str, calificacion: int, hora_transmision: datetime):
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
        self.salas_eliminadas: list[int] = []
        self.tickets: dict[int: Ticket] = {}
        self.usuarios: dict[int: Usuario] = {}
        self.autenticacion: bool = None

    def leer_peliculas(self):
        with open("peliculas.txt") as file:
            datos_uno = [lineas.strip("\n") for lineas in file]
            datos_finales = [lineas.split(",") for lineas in datos_uno]
            for datos in datos_finales:
                existe_pelicula = self.buscar_pelicula(datos[0])
                if not isinstance(existe_pelicula, list):
                    if existe_pelicula == False:
                        pelicula = Pelicula(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])
                        self.peliculas[pelicula.titulo] = pelicula
                    elif existe_pelicula.hora_transmision != datos[7]:
                        existe_pelicula.hora_transmision = datos[7]
        return
    
    def pista_contraseña(self):
        fecha_actual = datetime.date.today()
        print(f"PISTA: {fecha_actual}")
        fragmento_uno = int(fecha_actual.day) * int(fecha_actual.month) + int(fecha_actual.day)
        fragmento_dos = int(fecha_actual.day) * int(fecha_actual.month) - int(fecha_actual.day)
        fragmento_tres = int(fecha_actual.day) * int(fecha_actual.day) - int(fecha_actual.day)
        fragmento_cuatro = int(fecha_actual.month) * int(fecha_actual.month) + int(fecha_actual.month)       
        contraseña = str(fragmento_uno) + str(fragmento_dos) + str(fragmento_tres) + str(fragmento_cuatro) + "001"
        print(contraseña)
        return contraseña
    
    def crear_salas(self, num_salas_crear: int, recrear_sala):
        print("\n * INFO: EL NUMERO DE ASIENTOS DEBE CUMPLIR DOS CONDICIONES: # 100 <= ASIENTOS <= 1000  Y SER / POR 10")
        cant_salas_act = [salas for salas in self.salas.keys()]
        if len(cant_salas_act) == 0:
            cant_salas_act = 0
        else:
            cant_salas_act = cant_salas_act[-1]
        for num_sala in range(0, num_salas_crear):
            if recrear_sala != False:
                num_sala = recrear_sala
            elif recrear_sala == False:
                num_sala = cant_salas_act + 1
            print(f"\nCREACIÓN DE LA SALA # {num_sala}")
            num_asientos = int(input("\n-- Ingrese el número de asientos: "))
            if num_asientos % 10 == 0 and 100 <= num_asientos <= 500:
                pelicula = ""
                sala = Sala(num_sala, num_asientos, pelicula)
                sala.generar_asientos()
                self.salas[sala.num_sala] = sala
                cant_salas_act += 1
                print(f"\n * INFO: SE CREO LA SALA # {num_sala} EXITOSAMENTE")
            else:
                print("\n * INFO: DEBE CUMPLIR DOS CONDICIONES: # 100 <= ASIENTOS <= 1000  Y SER / POR 10\n")
                return
        return
    
    def recrear_sala_eliminada(self):
        if len(self.salas_eliminadas) > 0:
            print(f" HAS ELIMINADO {len(self.salas_eliminadas)} SALA(S) ANTERIORMENTE\n")
            recrear = int(input("Desea recrear alguna sala (1. Sí - 2. No): "))
            if recrear == 1:
                num_sala_recrear =  self.salas_eliminadas[0]
                self.crear_salas(1, num_sala_recrear)
                self.salas_eliminadas.remove(num_sala_recrear)
                return True
            elif recrear == 2:
                print(" * INFO: NO SE RECREO NINGUNA SALA\n")
                print("CONTINUEMOS CON LA CREACIÓN HABITUAL\n")
                return False
            else:
                print(f" * INFO: LA OPCION {recrear} NO ES VALIDA\n")
                return None
        else:
            return False

    def asignar_peli_sala(self):
        num_sala = int(input("-- Ingrese el número de la sala: "))
        sala = self.buscar_sala(num_sala)
        if sala != False:
            nombre_pelicula = input("-- Ingrese el nombre de la pelicula: ")
            pelicula = self.buscar_pelicula(nombre_pelicula)
            if not isinstance(pelicula, list):
                if  pelicula != False:
                    sala.pelicula = nombre_pelicula
                    print(f"\n * INFO: SE ASIGNO LA PELICULA {nombre_pelicula} A LA SALA # {num_sala} EXITOSAMENTE")
                else:
                    print(f"\n * INFO: LA PELICULA {nombre_pelicula} NO EXISTE")
            else:
                pelicula = pelicula[0]
                print(f"\n * INFO: LA PELICULA {pelicula.titulo} FUE ASIGNADA A OTRA SALA")
        else:
            print(f"\n * INFO: LA SALA # {num_sala} NO EXISTE")
        return
        
    def eliminar_sala(self):
        num_sala = int(input("-- Ingrese el número de la sala: "))
        sala = self.buscar_sala(num_sala)
        if sala != False:
            self.salas_eliminadas.append(sala.num_sala)
            del self.salas[sala.num_sala]
            print(f"\n * INFO: SE ELIMINO LA SALA # {num_sala}")
        else:
            print(f"\n* INFO: LA SALA # {num_sala} NO EXISTE")
        return
    
    def actualizar_peliculas(self):
        self.leer_peliculas()
        print("\n * INFO: SE ACTUALIZARON LAS PELICULAS EXITOSAMENTE")
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

    def similitud_texto(self, pelicula):
        peliculas_similares = []
        peliculas = [peli_act.titulo for peli_act in self.peliculas.values()]
        for pelis_act in peliculas:
            cant_pal_simi = 0
            for pala_uno, pala_dos in zip(pelis_act, pelicula):
                if pala_uno == pala_dos:
                    cant_pal_simi += 1
            if cant_pal_simi > 3:
                peliculas_similares.append(pelis_act)
        aux_simili_texto = self.auxiliar_similitud_texto(pelicula, peliculas)
        peliculas_similares_unida = peliculas_similares + aux_simili_texto
        peliculas_similares_unida = set(peliculas_similares_unida)
        peliculas_similares_unida = list(peliculas_similares_unida)
        if len(peliculas_similares_unida) > 0:
            print(" \n LA PELICULA QUE SE ESTA BUSCANDO PUEDE SER SIMILAR A:\n")
            for peli in peliculas_similares_unida:
                print(f" -- {peli}")
        return
    
    def auxiliar_similitud_texto(self, pelicula, peliculas_cine):
        pelis_simila = []
        for peli in peliculas_cine:
            peli_uno_separada = word_tokenize(peli)
            peli_dos_separada = word_tokenize(pelicula)
            peli_uno_set = set(peli_uno_separada)
            peli_dos_set = set(peli_dos_separada)
            union_set = peli_uno_set.union(peli_dos_set)
            peli_uno_contiene = []
            peli_dos_contiene = []
            for palabra in union_set:
                if palabra in peli_uno_separada:
                    peli_uno_contiene.append(1)
                else:
                    peli_uno_contiene.append(0)
                if palabra in peli_dos_separada:
                    peli_dos_contiene.append(1)
                else:
                    peli_dos_contiene.append(0)
            x_peli = np.array(peli_uno_contiene)
            y_peli = np.array(peli_dos_contiene)
            porcen_similitud = (x_peli @ y_peli) / (np.linalg.norm (x_peli)) * (np.linalg.norm (y_peli))
            if porcen_similitud > 0.0:
                pelis_simila.append(peli)
        return pelis_simila
    
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
        if sala != False and isinstance(sala, list) and usuario != False:
            sala = sala[1]
            asiento = self.asignar_asiento(sala, usuario)
            num_ticket = asiento + str(dni)
            print(num_ticket)
            datos_ticket = [num_ticket, fecha, sala.num_sala, asiento, dni, pelicula]
            usuario.adquirir_ticket(datos_ticket)
            self.deshabilitar_asiento(sala, asiento, dni)
            print(f"\n * INFO: SE RESERVO EL TICKET {num_ticket} EXITOSAMENTE")
        elif usuario == False:
            print(f"\n * INFO: EL DNI {dni} NO SE ENCUENTRA REGISTRADO")
        else:
            print(f"\n * INFO: LA PELICULA {pelicula} NO EXISTE O NO HA SIDO ASIGNADA A UNA SALA")
        return
    
    def cancelar_ticket(self, num_ticket: str, dni: int):
        usuario = self.buscar_usuario(dni)
        tickets = usuario.tickets
        log_dni = str(usuario.dni)
        log_dni = len(log_dni)
        if len(tickets) > 0 and num_ticket != "":
            datos_ticket = [[cod_ticket[:-log_dni], ticket] for cod_ticket, ticket in tickets.items() if cod_ticket == num_ticket]
            sala = datos_ticket[0][1].num_sala
            for sala_usuario in self.salas.values():
                if sala_usuario.num_sala == sala:
                    sala = sala_usuario
            self.habilitar_asiento(sala, datos_ticket[0][0])
            del datos_ticket[0][1]
            print(f"\n * INFO: SE CANCELO EL TICKET {num_ticket} EXITOSAMENTE")
        else:
            print(f"\n * INFO: EL TICKET {num_ticket} NO SE HA ENCONTRADO")
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