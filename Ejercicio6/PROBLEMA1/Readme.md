# 🌍 Proyecto: Los Mobs del Overworld (POO)

Este proyecto implementa la lógica de entidades del universo **Minecraft** utilizando **Clases Abstractas** en Python. El objetivo es demostrar cómo una clase base puede definir un contrato de comportamiento que todas las subclases deben seguir.

## 📦 Conceptos de Programación
* **Clase Abstracta (`ABC`):** Definición de la clase base `Mob`.
* **Métodos Abstractos:** Implementación obligatoria de `hacer_sonido()`, `comportamiento()` y `moverse()`.
* **Polimorfismo:** Cada mob responde al método `presentarse()` con sus datos específicos.

## 🎮 Entidades Implementadas
| Mob | Sonido | Tipo | Movimiento |
| :--- | :--- | :--- | :--- |
| **Vaca** | Muuuu | Pasivo | Camina lento |
| **Creeper** | ...Ssssss | Agresivo | Corre al jugador |
| **Enderman** | Vwoop | Neutral | Teletransporte |
| **Zombie** | Bruuuh | Agresivo | Camina al sol |

## ⚠️ Nota sobre la Abstracción
Durante el desarrollo, se comprobó que intentar instanciar la clase `Mob` directamente genera un error:
> `TypeError: Can't instantiate abstract class Mob with abstract methods...`

Esto demuestra que las clases abstractas actúan estrictamente como plantillas y requieren una implementación concreta para ser utilizadas.

---
**Autor:** Ivan Cervantes Rojas 
**Curso:** 2° Semestre - Programación Orientada a Objetos
