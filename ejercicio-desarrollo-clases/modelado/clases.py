# Importamos el codecs

import codecs

#Creamos la clase estudainte en la cual se declararan los valores de cada nota y el nombre para poder sacar el promedio de cada estudiante
#En el metodo obtener_promedio se realizara el calculo por el cual se sacara el promedio
class Estudiante():

	def __init__(self, name, n1, n2, n3):
		self.name = name
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		
	def obtener_nombre(self):
		return self.name

	def obtener_promedio(self):
		self.promedio = (self.n1 + self.n2 + self.n3) / 3
		return self.promedio



#En la clase MiArchivo ingresaremos a informacion.csv para obtener los datos de cada estudiante 
#Ademas retornaremos una lista mediante el metodo "obtener_informacion" cuyos elementos seran unicamente lineas
#Por ultimo tenemos el metodo para cerrar el archivo(en el principal esto ya se explico que era para evitar el uso de memoria innecesaria)
class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


#Dentro de la Clase MiArchivoEscribir ingresaremos cada estudiante con su respectivo promedio
#mediante el metodo"agregar_informacion ingresamos el nombre y el promedio a promedio.csv
#por ultimo cerramos el archivo
class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("data/promedios.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s tiene un promedio de: %.2f\n" % (p.obtener_nombre(), p.obtener_promedio()))

    def cerrar_archivo(self):
        self.archivo.close()