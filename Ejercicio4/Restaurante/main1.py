from comida import Comida
from bebida import Bebida
from postre import Postre

Pozole = Comida("Pozole rojo", 85.0, "Principal")
Sangrìa = Bebida("Bebida de sangrìa", 35.0, "Fría")
Chocoflan = Postre("chocoflan", 45.0, False)

Pozole.mostrar_info()
Pozole.tipo()
print("---")

Sangrìa.mostrar_info()
Sangrìa.tipo()
print("---")

Chocoflan.mostrar_info()
Chocoflan.tipo()