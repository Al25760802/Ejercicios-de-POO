from abc import ABC, abstractclassmethod

#clase abstracta (plantilla)
class Animal(ABC):
    @abstractclassmethod
    def hablar(self)
    pass # No se implementa el método

# Clase en específico
class Perro(Animasl):
    def hablar(self):
        return "Guau"
# Clase en específico
class Gato(Animal):
    def hablar(self):
        return "Miau"
    
# Usar las clases
perro = Perro()
gato = Gato()
print(perro.hablar()) # Guau!
print(gato.hablar())  # Miau!  