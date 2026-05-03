# Importamos la clase padre
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):

    # atributos extra
    _num_velocidades: int
    _tipo: str
    _velocidad_maxima: float = 40.0

    # Método constructor
    def __init__(self, marca: str, modelo: str, año: int, num_velocidades: int, tipo: str):
        super().__init__(marca, modelo, año)
        self.setNum_velocidades(num_velocidades)
        self.setTipo(tipo)

    def getNum_velocidades(self):
        return self._num_velocidades

    def setNum_velocidades(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("ERROR: El número de velocidades debe ser un número")
        if valor != 1 and valor != 7 and valor != 21:
            raise ValueError("ERROR: El número de velocidades solo puede ser 1, 7 o 21")
        else:
            self._num_velocidades = valor

    def getTipo(self):
        return self._tipo

    def setTipo(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El tipo de bicicleta debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El tipo de bicicleta no puede tener caracteres especiales")
        else:
            self._tipo = valor

    # Sobreescritura del método acelerar
    def acelerar(self, incremento: float):
        self._velocidad = self._velocidad + incremento
        if self._velocidad > self._velocidad_maxima:
            self._velocidad = self._velocidad_maxima
            print(f"¡Velocidad máxima de la bicicleta alcanzada! {self._velocidad_maxima} km/h")
        else:
            print(f"Bicicleta pedaleando... velocidad actual: {self._velocidad} km/h")