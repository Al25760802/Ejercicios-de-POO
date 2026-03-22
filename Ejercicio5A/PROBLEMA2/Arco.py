from Mob import Mob

class Arco(Herramienta):
    def __init__(self, material: str, durabilidad: int, flechas: int):
        super().__init__(material, durabilidad)
        self.flechas = flechas

    @property
    def nombre(self): return "Arco"

    def usar(self, objetivo: str):
        if self.flechas <= 0:
            return "¡Sin flechas!"
        self.flechas -= 1
        self.desgastar()
        return f"{self.nombre} dispara a {objetivo} (Flechas restantes: {self.flechas})"
