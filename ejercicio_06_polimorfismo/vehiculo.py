# Clase padre Vehiculo
class Vehiculo:

    # Atributos privados
    _marca: str
    _modelo: str
    _año: int
    _velocidad: float

    # método constructor
    def __init__(self, marca: str, modelo: str, año: int):
        self.setMarca(marca)
        self.setModelo(modelo)
        self.setAño(año)
        self._velocidad = 0.0  # siempre empieza en 0

    def getMarca(self):
        return self._marca

    def setMarca(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: La marca debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: La marca no puede tener datos alphanúmericos")
        else:
            self._marca = valor


    def getModelo(self):
        return self._modelo

    def setModelo(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El modelo debe ser en texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El modelo no puede tener datos alfanúmericos")
        else:
            self._modelo = valor

    def getAño(self):
        return self._año

    def setAño(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("ERROR: El año ingresado no es válido")
        if valor < 1900:
            raise ValueError("ERROR: El año no puede ser menor a 1900")
        elif valor > 2026:
            raise ValueError("ERROR: El año ingresado no puede ser mayor a 2026")
        else:
            self._año = valor

    def getVelocidad(self):
        return self._velocidad

    # Método acelerar
    def acelerar(self, incremento: float):
        self._velocidad = self._velocidad + incremento
        print(f"Velocidad actual: {self._velocidad} km/h")

    #Método que imprime la información del coche
    def describir(self):
        print(f"marca: {self.getMarca()} | modelo: {self.getModelo()} | año: {self.getAño()} | velocidad: {self.getVelocidad()} km/h")