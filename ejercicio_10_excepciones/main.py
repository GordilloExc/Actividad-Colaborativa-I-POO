from coche import Coche
from excesoVelocidadException import ExcesoVelocidadException

# Creamos un coche
coche1 = Coche("Ferrari", "Puresangre")
coche1.describir()

# Intentamos incrementar la velocidad
try:
    coche1.incrementarVelocidad(200)  
    coche1.incrementarVelocidad(101) 
except ExcesoVelocidadException as e:
    print(f"¡Excepción capturada!: {e}")

coche1.describir()