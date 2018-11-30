from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Persona

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0])
    print(p)
    m2.agregar_informacion(p)

m.cerrar_archivo()
m2.cerrar_archivo()
