from pajaro import Pajaro
from avion import Avion

# Lista con diferentes voladores
voladores = [
    Pajaro("Aguila", "ave", 120),
    Avion("Boeing", "Avianca", 4),
]

for volador in voladores:
    volador.describir()        # muestra la info
    volador.volar()        # hace volar
    print("-------------------------------")