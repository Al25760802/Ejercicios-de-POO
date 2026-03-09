from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero

Zero = Guerrero("Zero", 10, "Espada mataDragones")
JAZZ = Mago("JAZZ", 15, "Vacio infinito!!!")
Arquimedes = Arquero("Arquimedes", 10, 29)

Zero.presentarse()
Zero.usar_habilidad()
print("---")
JAZZ.presentarse()
JAZZ.usar_habilidad()
print("---")
Arquimedes.presentarse()
Arquimedes.usar_habilidad()