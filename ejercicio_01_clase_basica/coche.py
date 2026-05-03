# Se crea la clase Coche
class Coche:

    # Atributos de la clase
    marca: str
    modelo: str
    año: int

    # Método que imprime la información del coche
    def describir(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.año}")


# Primer objeto
coche1 = Coche()
coche1.marca = "Suzuki"
coche1.modelo = "Vitara"
coche1.año = 2015
coche1.describir()

# Segundo objeto
coche2 = Coche()
coche2.marca = "Toyota"
coche2.modelo = "Prado"
coche2.año = 2022
coche2.describir()

# Tercer objeto
coche3 = Coche()
coche3.marca = "Ford"
coche3.modelo = "Mustang"
coche3.año = 2011
coche3.describir()