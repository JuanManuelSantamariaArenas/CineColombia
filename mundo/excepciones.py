class CineColombiaError(Exception):
    def __init__(self, msg: str):
        self.mensaje = msg

class NumAsientosNoDivisiblesPorDiezError(CineColombiaError): # POR DEFINIR
    def __init__(self, msg: str):
        super().__init__(msg)

class DatosSinIngresarError(CineColombiaError):
    def __init__(self, msg: str):
        super().__init__(msg)