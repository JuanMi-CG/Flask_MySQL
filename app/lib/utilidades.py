# app/lib/utilidades.py

def formatear_fecha(fecha):
    """Recibe un objeto fecha y devuelve una cadena formateada."""
    return fecha.strftime('%d/%m/%Y')

class Calculadora:
    """Clase de ejemplo para realizar operaciones matemáticas."""
    @staticmethod
    def sumar(a, b):
        return a + b
