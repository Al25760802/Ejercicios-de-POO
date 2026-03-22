from Mob import Mob

class Pala(Herramienta):
    @property
    def nombre(self): return "Pala"
    
    def usar(self, objetivo: str):
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} excava {objetivo} (daño: {daño})"