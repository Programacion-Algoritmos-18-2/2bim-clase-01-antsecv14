"""
    Ejecutable de manejo de excepciones
"""

from paquete_excepciones.miexepcion import MiError

bandera = True
x = 0

while bandera:
    try:
        x = input("Ingresar valor:\n")
        x = float(x)
        if x < 20:
            raise MiError(x)
        bandera = False    
    except MiError as e:
        print(e)
    
    except ValueError as e:
        print("Existe un error, con el valor (%s) ingresado (%s)" % (x, e))


print("Su valor (%s) ingresado cumple las condiciones" % (x))
