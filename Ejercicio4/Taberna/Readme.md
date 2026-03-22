# ⚔️ Sistema de Héroes: RPG en Python
**Concepto:** Especialización de Clases y Polimorfismo  
**Proyecto:** Simulación de habilidades para personajes de combate.

## 📜 Descripción
Este proyecto implementa un sistema básico de roles para un juego de rol (RPG), donde cada personaje hereda atributos base (como nombre y nivel) pero posee **habilidades únicas** y equipamiento especializado.

## 📂 Arquitectura del Proyecto
El sistema se divide en módulos independientes para facilitar la expansión (por ejemplo, añadir un "Paladín" o "Ladrón" en el futuro):

* `Guerrero.py`: Especialista en combate cuerpo a cuerpo con armas pesadas.
* `Mago.py`: Usuario de artes místicas y hechizos de alto impacto.
* `Arquero.py`: Combatiente a distancia con gestión de proyectiles (flechas).
* `main.py`: Orquestador que instancia al equipo y ejecuta sus acciones.

## 👥 Personajes Registrados

| Héroe | Clase | Nivel | Equipo / Habilidad Especial |
| :--- | :--- | :--- | :--- |
| **Zero** | ⚔️ Guerrero | 10 | Espada mataDragones |
| **JAZZ** | 🪄 Mago | 15 | Vacío Infinito |
| **Arquimedes** | 🏹 Arquero | 10 | Carcaj con 29 flechas |

## 🛠️ Mecánicas Implementadas
1.  **Presentación:** Cada clase implementa un método `presentarse()` que muestra las estadísticas actuales del héroe.
2.  **Uso de Habilidades:** El método `usar_habilidad()` es **polimórfico**: aunque se llama igual en todos los personajes, el resultado en consola es distinto según la clase (el guerrero ataca, el mago lanza un hechizo y el arquero dispara).
3.  **Modularidad:** Uso de `from ... import ...` para mantener el código base limpio y fácil de leer.

## 📊 Ejemplo de Salida (Output)
```text
Soy Zero, un Guerrero de nivel 10.
¡Ataco con mi Espada mataDragones!
---
Soy JAZZ, un Mago de nivel 15.
¡Lanzo el hechizo Vacío infinito!!!
---
Soy Arquimedes, un Arquero de nivel 10.
¡Disparo una flecha! (Quedan 28)
