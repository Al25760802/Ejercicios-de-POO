from Mob import Mob

class Espada(Herramienta):
    @property
    def nombre(self): return "Espada"
    
    def usar(self, objetivo: str):
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} ataca a {objetivo} (daño: {daño})"