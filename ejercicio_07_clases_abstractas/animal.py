# Importamos ABC y abstractmethod
from abc import ABC, abstractmethod

# se crea clase abstracta animal
class Animal(ABC): # hereda de ABC

    # Atributos privados
    _nombre: str
    _raza: str
    _edad: int
    _peso: float
    _tamaño: str # pequeño, mediano y grande

    # método constructor

    def __init__(self, nombre: str, raza: str, edad: int, peso: float, tamaño: str):
        self.setNombre(nombre)
        self.setRaza(raza)
        self.setEdad(edad)
        self.setPeso(peso)
        self.setTamaño(tamaño)

    def getNombre(self):
        return self._nombre

    def setNombre(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El nombre debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El nombre no puede tener datos alphanúmericos")
        else:
            self._nombre = valor
    
    def getRaza(self):
        return self._raza

    def setRaza(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: La raza debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: La raza no puede tener datos alphanúmericos")
        else:
            self._raza = valor

    def getEdad(self):
        return self._edad

    def setEdad(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("ERROR: El dato ingresado no es válido")
        if valor < 0:
            raise ValueError("ERROR: El año no puede ser menor a 0")
        elif valor > 30:
            raise ValueError("ERROR: El año ingresado no puede ser mayor a 30")
        else:
            self._edad = valor

    def getPeso(self):
        return self._peso

    def setPeso(self, valor: float):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("ERROR: El peso debe ser un número")
        if valor <= 0:
            raise ValueError("ERROR: El peso no puede ser menor o igual a 0")
        elif valor > 200:
            raise ValueError("ERROR: El peso no puede ser mayor a 200 kg")
        else:
            self._peso = valor

    def getTamaño(self):
        return self._tamaño

    def setTamaño(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El tamaño debe ser en texto: pequeño, mediano y grande")
        elif not valor.isalpha():
            raise ValueError("ERROR: El tamaño no puede tener datos alphanúmericos")
        else:
            self._tamaño = valor

    # método describir
    def describir(self):
        print(f"Nombre: {self.getNombre()} | Raza: {self.getRaza()} | Edad: {self.getEdad()} | Peso: {self.getPeso()} kg | Tamaño: {self.getTamaño()}")    
        

    # método abstracto, las clases hijas o implementan
    @abstractmethod
    def hacerSonido(self):
        pass
