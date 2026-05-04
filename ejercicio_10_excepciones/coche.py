from excesoVelocidadException import ExcesoVelocidadException

class Coche:

    _marca: str
    _modelo: str
    _velocidad: float
    _velocidad_maxima: float = 299.0

    def __init__(self, marca: str, modelo: str):
        self.setMarca(marca)
        self.setModelo(modelo)
        self._velocidad = 0.0

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

    def getVelocidad(self):
        return self._velocidad

    # Método que lanza excepción personalizada
    def incrementarVelocidad(self, velocidad: float):
        if self._velocidad + velocidad > self._velocidad_maxima:
            raise ExcesoVelocidadException(
                f"ERROR: Velocidad máxima excedida. Límite: {self._velocidad_maxima} km/h"
            )
        else:
            self._velocidad += velocidad
            print(f"Velocidad actual: {self._velocidad} km/h")

    def describir(self):
        print(f"Marca: {self.getMarca()} | Modelo: {self.getModelo()} | Velocidad: {self.getVelocidad()} km/h")