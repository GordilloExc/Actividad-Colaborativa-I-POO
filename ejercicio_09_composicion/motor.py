# Clase de Motor
class Motor:

    # Atributos privados
    _potencia: float  # en caballos de fuerza (HP)
    _tipo: str        # gasolina, diesel, eléctrico

    # método constructor
    def __init__(self, potencia: float, tipo: str):
        self.setPotencia(potencia)
        self.setTipo(tipo)

    def getPotencia(self):
        return self._potencia

    def setPotencia(self, valor: float):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("ERROR: La potencia debe ser un número")
        if valor <= 0:
            raise ValueError("ERROR: La potencia no puede ser menor o igual a 0")
        else:
            self._potencia = valor

    def getTipo(self):
        return self._tipo

    def setTipo(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El tipo debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El tipo no puede tener caracteres especiales")
        else:
            self._tipo = valor

    def describir(self):
        print(f"Motor: {self.getTipo()} | Potencia: {self.getPotencia()} HP")