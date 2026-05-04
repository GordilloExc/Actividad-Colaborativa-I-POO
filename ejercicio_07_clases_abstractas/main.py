from perro import Perro
from gato import Gato

# Lista con diferentes tipos de vehículos
animales = [
    Perro("Oreo", "Beagle", 7, 25, "Mediano"),
    Gato("Licas", "Persa", 6, 14, "Pequeño"),
]

print("--- Lista de animales ---")
for animal in animales:
    animal.describir()
    animal.hacerSonido()
    print("-------------------------------")