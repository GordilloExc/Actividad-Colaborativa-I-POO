from volador import Volador

class Pajaro(Volador):

    # Atributos
    _nombre: str
    _especie: str
    _envergadura: float # tamaño de alas

    # método constructor
    def __init__(self, nombre: str, especie: str, envergadura: float):
        self.setNombre(nombre)
        self.setEspecie(especie)
        self.setEnvergadura(envergadura)

    # Getter y setter de nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: El nombre debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: El nombre no puede tener caracteres especiales")
        else:
            self._nombre = valor

    # Getter y setter de especie
    def getEspecie(self):
        return self._especie

    def setEspecie(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("ERROR: La especie debe ser texto")
        elif not valor.isalpha():
            raise ValueError("ERROR: La especie no puede tener caracteres especiales")
        else:
            self._especie = valor

    # Getter y setter de envergadura
    def getEnvergadura(self):
        return self._envergadura

    def setEnvergadura(self, valor: float):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("ERROR: La envergadura debe ser un número")
        if valor <= 0:
            raise ValueError("ERROR: La envergadura no puede ser menor o igual a 0")
        else:
            self._envergadura = valor

    def describir(self):
        print(f"Pájaro: {self.getNombre()} | Especie: {self.getEspecie()} | Envergadura: {self.getEnvergadura()} cm")

    # Implementación del método volar
    def volar(self):
        print(f"¡{self.getNombre()} volando con sus alas! Envergadura: {self.getEnvergadura()} cm")
