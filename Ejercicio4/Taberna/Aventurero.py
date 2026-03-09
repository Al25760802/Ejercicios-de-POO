class Aventurero:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def presentarse(self):
        print(f"Yo soy {self.nombre}, un legendario aventurero de nivel {self.nivel}")

    def usar_habilidad(self):
        print("Habilidad desconocida...")