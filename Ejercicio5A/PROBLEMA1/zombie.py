from Mob import Mob

class Zombie(Mob):
    def hacer_sonido(self) -> str:
        return "Uuuuhhhgggg"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Camina torpemente hacia el jugador"
