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
                print(f"\n * INFO: {opcion} NO ES UNA OPCIÓN VALIDA")

    def autentificar_admon(self):
        print("\n- AUTENTICAR ADMINISTRADOR -\n")
        usuario_admon = input("Usuario: ")
        if usuario_admon == "artlee":
            contraseña_admon = self.cine.pista_contraseña()
            contraseña = input("Contraseña: ")
            if contraseña == contraseña_admon:
                self.cine.autenticacion = True
                print("\n * INFO: SE AUTENTIFICO EL ADMON CORRECTAMENTE")
                return
            else:
                print("\n * INFO: CONTRASEÑA INCORRECTA")
        else: 
            print(f"\n * INFO: EL USUARIO {usuario_admon} NO CORRESPONDE AL DEL ADMINISTRADOR")
            self.cine.autenticacion = False
            return
    
    def crear_salas(self):
        try:
            print("\n- CREAR SALAS -\n")
            if self.cine.autenticacion:
                num_salas_crear = int(input("-- Ingrese el número de salas que desea crear: "))
                if num_salas_crear > 0:
                    self.cine.crear_salas(num_salas_crear)
                else: 
                    print("\n * INFO: EL NUMERO DE SALAS A CREAR DEBE SER MAYOR A CERO (0)")
            else:
                print("\n * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR")
        except DatosSinIngresarError:
            print("\n * INFO: DEBES INGRESAR LOS DATOS SOLICITADOS")
        except ValueError:
            print("\n * INFO: SE INGRESO CARACTERES NO CORRESPONDIENTES A NUMEROS")

    def asignar_peli_sala(self):
        try:
            print("\n- ASIGNACION DE PELICULA A UNA SALA -\n") 
            if self.cine.autenticacion:
                if len(self.cine.salas) > 0:
                    self.cine.asignar_peli_sala()
                else:
                    print(" * INFO: PRIMERO DEBES CREAR LAS SALAS DEL CINE")
            else:
                print(" * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR")
        except ValueError:
            print(" * INFO: SE INGRESO CARACTERES NO CORRESPONDIENTES A NUMEROS")

    def eliminar_sala(self):
        try:
            print("\n- ELIMINAR SALA -\n")
            if self.cine.autenticacion:
                self.cine.eliminar_sala()
            else:
                print(" * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR")
        except ValueError:
            print("\n * INFO: SE INGRESO CARACTERES NO CORRESPONDIENTES A NUMEROS")
    
    def salir_menu_admon(self):
        if len(self.cine.salas) > 0:
            print("\nGRACIAS POR ADMINISTRAR EL CINE, HAS CERRADO SESION COMO ADMON\n")
            self.ejecutar_usuario()
        else:
            print(" * INFO: PRIMERO DEBES CREAR LAS SALAS DEL CINE")

    def actualizar_peliculas(self):
        if self.cine.autenticacion:
            self.cine.actualizar_peliculas()
        else:
            print("\n * INFO: DEBES AUTENTICARTE COMO ADMINISTRADOR")

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
        try:
            print("\n- REGISTRAR USUARIO -\n")
            dni = int(input("-- Ingrese el número de identificación: "))
            nombre = input("-- Ingrese el nombre completo: ")
            edad = int(input("-- Ingrese la edad: "))
            self.cine.resgistrar_usuario(dni, nombre, edad)
        except DatosSinIngresarError:
            print(" * INFO: DEBES INGRESAR LOS DATOS SOLICITADOS")
        except ValueError:
            print("\n * INFO: SE INGRESO CARACTERES NO CORRESPONDIENTES A NUMEROS")

    def buscar_pelicula(self):
        try: 
            print("\n- BUSCAR PELICULA -\n")
            nombre_pelicula = input("-- Ingrese el nombre de la pelicula: ")
            datos = self.cine.buscar_pelicula(nombre_pelicula)
            if datos != False and isinstance(datos, list):
                pelicula = datos[0]
                sala = datos[1]
                print(f" * INFO: LA PELICULA {nombre_pelicula} SE ENCUENTRA DISPONIBLE EN LA SALA # {sala.num_sala} Y INICIA A LAS {pelicula.hora_transmision}")
            else: 
                print(f"\n * INFO: LA PELICULA {nombre_pelicula} NO SE ENCUENTRA DISPONIBLE")
        except DatosSinIngresarError:
            print(" * INFO: DEBES INGRESAR LOS DATOS SOLICITADOS")

    def reservar_ticket(self):
        try:
            print("\n- RESERVAR TICKET -\n")
            dni = int(input("-- Ingrese el número de identificación: "))
            nombre_pelicula = input("-- Ingrese el nombre de la pelicula: ")
            self.cine.reservar_ticket(dni, nombre_pelicula)
        except DatosSinIngresarError:
            print(" * INFO: DEBES INGRESAR LOS DATOS SOLICITADOS")
        except ValueError:
            print(" * INFO: SE INGRESO CARACTERES NO CORRESPONDIENTES A NUMEROS")

    def cancelar_ticket(self):
        try:
            print("\n- CANCELAR TICKET -\n")
            num_ticket = input("-- Ingrese el número del ticket: ")
            dni = int(input("-- Ingrese el número de identificación: "))
            self.cine.cancelar_ticket(num_ticket, dni)
        except DatosSinIngresarError:
            print(" * INFO: DEBES INGRESAR LOS DATOS SOLICITADOS")
        except ValueError:
            print(" * INFO: SE INGRESO CARACTERES NO CORRESPONDIENTES A NUMEROS")

    def salir_app(self):
        print("\nMUCHAS GRACIAS POR USAR LA APLICACIÓN 👍👍👍")
        self.cine.guardar()
        sys.exit(0)