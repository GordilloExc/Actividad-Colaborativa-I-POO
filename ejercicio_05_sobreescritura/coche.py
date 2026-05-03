# Importamos la clase padre
from vehiculo import Vehiculo

class Coche(Vehiculo):

    # Atributos extras
    _num_puertas: int
    _tipo_combustible: str
    _velocidad_maxima: float = 300.0

    # Método constructor
    def __init__(self, marca: str, modelo: str, año: int, num_puertas: int, tipo_combustible: str):
        super().__init__(marca, modelo, año)
        self.setNum_puertas(num_puertas)
        self.setTipo_combustible(tipo_combustible)

    def getNum_puertas(self):
        return self._num_puertas

    def setNum_puertas(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("ERROR: El número de puertas debe ser un número")
        if valor != 2 and valor != 4:
            raise ValueError("ERROR: El número de puertas solo puede ser 2 o 4")
        else:
            self._num_puertas = valor

    def getTipo_combustible(self):
        return self._tipo_combustible

    def setTipo_combustible(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El tipo de combustible debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El tipo de combustible no puede tener caracteres especiales")
        else:
            self._tipo_combustible = valor

    # Sobreescritura del método acelerar
    def acelerar(self, incremento: float):
        self._velocidad = self._velocidad + incremento
        if self._velocidad > self._velocidad_maxima:
            self._velocidad = self._velocidad_maxima
            print(f"¡Velocidad máxima del coche alcanzada! {self._velocidad_maxima} km/h")
        else:
            print(f"Coche acelerando... velocidad actual: {self._velocidad} km/h")