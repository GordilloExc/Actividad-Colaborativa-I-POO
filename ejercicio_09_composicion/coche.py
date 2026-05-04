# Clase Coche que contiene un Motor (composición)
from motor import Motor

class Coche:

    # Atributos privados
    _marca: str
    _modelo: str
    _motor: Motor  

    # método constructor
    def __init__(self, marca: str, modelo: str, potencia: float, tipo_motor: str):
        self.setMarca(marca)
        self.setModelo(modelo)
        self._motor = Motor(potencia, tipo_motor)  # crea el Motor adentro

    def getMarca(self):
        return self._marca

    def setMarca(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: La marca debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: La marca no puede tener caracteres especiales")
        else:
            self._marca = valor

    def getModelo(self):
        return self._modelo

    def setModelo(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El modelo debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El modelo no puede tener caracteres especiales")
        else:
            self._modelo = valor

    # Método que describe el coche incluyendo el motor
    def describir(self):
        print(f"Coche: {self.getMarca()} {self.getModelo()}")
        self._motor.describir()  # llama al describir del Motor