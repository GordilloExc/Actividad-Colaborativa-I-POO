# importamos la clase vehiculo
from vehiculo import Vehiculo

# clase hija coche que hereda Vehiculo
class Coche(Vehiculo):
    #atributo extras
    _num_puertas: int
    _tipo_combustible: str

     # método constructor
    def __init__(self, marca: str, modelo: str, año: int, num_puertas: int, tipo_combustible: str):
        super().__init__(marca, modelo, año)  # llama al constructor del padre
        self.setNum_puertas(num_puertas)
        self.setTipo_combustible(tipo_combustible)

    def getTipo_combustible(self):
        return self._tipo_combustible

    def setTipo_combustible(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El tipo de combustible debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El tipo de combustible no puede tener datos alphanúmericos")
        else:
            self._tipo_combustible = valor

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
