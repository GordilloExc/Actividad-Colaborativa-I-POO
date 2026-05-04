from volador import Volador

class Avion(Volador):

    # Atributos privados
    _modelo: str
    _aerolinea: str
    _num_motores: int # número de motores

    # método constructor
    def __init__(self, modelo: str, aerolinea: str, num_motores: float):
        self.setModelo(modelo)
        self.setAerolinea(aerolinea)
        self.setNum_motores(num_motores)

    # Getter y setter de modelo
    def getModelo(self):
        return self._modelo

    def setModelo(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El modelo debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El modelo no puede tener caracteres especiales")
        else:
            self._modelo = valor

    # Getter y setter de aerolinea
    def getAerolinea(self):
        return self._aerolinea

    def setAerolinea(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: La aerolinea debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: La aerolinea no puede tener caracteres especiales")
        else:
            self._aerolinea = valor

    # Getter y setter de envergadura
    def getNum_motores(self):
        return self._num_motores

    def setNum_motores(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError("ERROR: El número de motores debe ser un número")
        if valor <= 0:
            raise ValueError("ERROR: El número de motores no puede ser menor o igual a 0")
        else:
            self._num_motores = valor

    def describir(self):
        print(f"Avión: {self.getModelo()} | Aerolínea: {self.getAerolinea()} | Motores: {self.getNum_motores()}")

    # Implementación del método volar
    def volar(self):
        print(f"¡{self.getModelo()} volando con sus motores! Num_motores: {self.getNum_motores()}")
