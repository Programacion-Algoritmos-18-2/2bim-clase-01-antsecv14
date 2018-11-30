from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
for d in lista:
    #print(d)
    p = Persona(d[1], d[2], d[3], d[0])
    print(p)
