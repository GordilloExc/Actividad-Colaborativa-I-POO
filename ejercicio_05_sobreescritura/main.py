from coche import Coche
from bicicleta import Bicicleta

# Probamos el coche
coche1 = Coche("Ferrari", "Puresangre", 2022, 2, "Extra")
coche1.describir()
coche1.acelerar(200)   # normal
coche1.acelerar(300)   # supera el límite asignado
coche1.describir()

# Probamos la bicicleta
bici1 = Bicicleta("GW", "Jaguar", 2025, 7, "Montana")
bici1.describir()
bici1.acelerar(20)     # normal
bici1.acelerar(40)     # supera el límite asignado
bici1.describir()