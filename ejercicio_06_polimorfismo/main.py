from coche import Coche
from bicicleta import Bicicleta

# Lista con diferentes tipos de vehículos
vehiculos = [
    Coche("Ferrari", "Puresangre", 2022, 2, "Extra"),
    Bicicleta("GW", "Jaguar", 2025, 7, "Montana"),
    Coche("Toyota", "Prado", 2020, 4, "Diesel")
]

# Polimorfismo: mismo método, diferente comportamiento
print("--- Acelerando todos los vehículos ---") # print que agrega mejora visual
for vehiculo in vehiculos:
    vehiculo.describir()
    vehiculo.acelerar(50)
    vehiculo.describir()
    print("-------------------------------") # print que agrega mejora visual