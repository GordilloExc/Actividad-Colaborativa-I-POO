# importamos la clase vehiculo
from vehiculo import Vehiculo

# clase hija coche que hereda Vehiculo
class Bicicleta(Vehiculo):
    
     # Atributos extra
    _num_velocidades: int
    _tipo: str

     # método constructor
    def __init__(self, marca: str, modelo: str, año: int, num_velocidades: int, tipo: str):
        super().__init__(marca, modelo, año)  # llama al constructor del padre
        self.setNum_velocidades(num_velocidades)
        self.setTipo(tipo)

    def getTipo(self):
        return self._tipo

    def setTipo(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El tipo de bicicleta debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El tipo de bicicleta no puede tener datos alphanúmericos")
        else:
            self._tipo = valor

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
