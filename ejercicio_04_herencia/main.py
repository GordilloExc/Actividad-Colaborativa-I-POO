# Importamos las clases
from coche import Coche
from bicicleta import Bicicleta

# Creamos un objeto Coche
coche1 = Coche("Ferrari", "Puresangre", 2022, 2, "Extra")
coche1.describir()
coche1.acelerar(250)
coche1.describir()

# Creamos un objeto Bicicleta
bici1 = Bicicleta("GW", "Jaguar", 2025, 7, "Montaña")
bici1.describir()
bici1.acelerar(20)
bici1.describir()