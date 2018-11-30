"""
    Ejecutable de manejo de excepciones
"""

from paquete_excepciones.miexepcion import MiError

x = input("Ingresar valor:\n")
x = int(x)

try:
    if x < 20:
        raise MiError(x)
except MiError as e:
    print(e)
