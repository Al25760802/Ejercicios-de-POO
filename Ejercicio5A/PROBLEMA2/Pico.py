from Mob import Mob

class Pico(Herramienta):
    @property
    def nombre(self): return "Pico"
    
    def usar(self, objetivo: str):
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} mina {objetivo} (daño: {daño})"