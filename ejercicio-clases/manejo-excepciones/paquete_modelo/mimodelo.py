"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, name):
        """
        """
        self.nombre = name
        self.edad = 0

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad

    def __str__(self):
        """
        """
        return "%s - %d" % (self.nombre, self.edad)
