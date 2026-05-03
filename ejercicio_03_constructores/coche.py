# Se crea la clase coche
class Coche:

    # Atributos de la clase privados
    _marca: str
    _modelo: str
    _año: int

    def __init__ (self, marca: str, modelo: str, año: int):
        self.setMarca(marca)
        self.setModelo(modelo)
        self.setAño(año)


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

    #Método que imprime la información del coche
    def describir(self):
        print(f"marca: {self.getMarca()} modelo: {self.getModelo()} año: {self.getAño()}")


# Primer objeto
coche1 = Coche("Suzuki", "Vitara", 2015)
coche1.describir()

# Segundo objeto
coche2 = Coche("Toyota", "Prado", 2022)
coche2.describir()

# Tercer objeto
coche3 = Coche("Ford", "Mustang", 2011)
coche3.describir()



