# Importamos ABC y abstractmethod
from abc import ABC, abstractclassmethod

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
    
    def getNombre(self):
        return self._raza

    def setNombre(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: La raza debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: La raza no puede tener datos alphanúmericos")
        else:
            self._raza = valor

        
        

    # método abstracto, las clases hijas o implementan
    @abstractmethod
    def hacerSonido(self):
        pass
