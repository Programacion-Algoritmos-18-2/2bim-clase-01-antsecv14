#Importamos de la carpeta modelado el archivo clases

from modelado.clases import *

#Se crean los objetos para leer y escribir los archivos respectivamente

m = MiArchivo() 

m2 = MiArchivoEscribir() 

#Recibimos una lista en la cual cada uno de sus elementos sera una linea

lista = m.obtener_informacion()

#hacemos que la lista solo utilice los elementos de la posicion uno a la 6 (de esta manera eliminamos los titulos)

lista = lista[1:6]

#Creamos una lista nueva

listaNueva = []  			

#Separamos cada linea de la lista con el simbolo | utilizando el split, reemplazamos los \n con unas '' para que de esta forma se elimine
# por ultimo agregamos cada elemento a la nueva lista

for linea in lista:
	linea = linea.split("|")               
	linea[3] = linea[3].replace('\n', '')
	listaNueva.append(linea)


#Creamos un objeto para obtener el promedio de las notas de cada estudiante y dentro del nuevo archivo escribimos 
for linea in listaNueva:

	objeto = Estudiante(linea[0], int(linea[1]), int(linea[2]), int(linea[3]))
	m2.agregar_informacion(objeto)

#Utilizando los metodos cerrar archivo respectivamente para poder evitar el uso innecesario de la memoria

m.cerrar_archivo()
m2.cerrar_archivo()

#Finalmente imprimomos un mensaje que nos muestre que el proceso ha culminado

print("Proceso realizado con éxito")
