# 🎮 Sistema de Registro: Torneo de Videojuegos ITE

Este proyecto consiste en un sistema de gestión de participantes desarrollado en **Python** para el Instituto Tecnológico de Ensenada. El objetivo principal es aplicar conceptos avanzados de **Programación Orientada a Objetos (POO)** para modelar una situación del mundo real.

---

## 🎯 Objetivos de la Práctica
* Implementar **Herencia** para reutilizar lógica común.
* Aplicar **Polimorfismo** mediante la sobreescritura de métodos (`Method Overriding`).
* Utilizar la función `super()` para extender comportamientos de la clase padre.
* Gestionar la lógica de negocio (reglas de puntos) dentro de las clases.

---

## 📐 Arquitectura del Sistema (POO)

El sistema se basa en una jerarquía de clases donde `Jugador` actúa como la entidad principal.

### 1. Clase Base: `Jugador`
Es la superclase que contiene los atributos que todo asistente al torneo posee:
* **Atributos:** `nombre`, `num_control`, `nivel` y `puntos`.
* **Lógica de Puntos:** Implementa validaciones para que el saldo de puntos nunca sea inferior a **0**, protegiendo la integridad de los datos.

### 2. Clase: `Competidor` (Hereda de Jugador)
Especialización para los alumnos que juegan activamente.
* **Atributo extra:** `equipo`.
* **Especialización:** Sobreescribe `mostrar_perfil()` para incluir el nombre del equipo, llamando primero a la lógica del padre para evitar duplicidad de código.

### 3. Clase: `Observador` (Hereda de Jugador)
Especialización para los asistentes que apoyan el evento.
* **Atributo extra:** `partidas_vistas`.
* **Método único:** `ver_partida()`, el cual incrementa el contador de vistas y otorga automáticamente **5 puntos** al perfil.



---

## 📁 Estructura de Archivos
La solución está modularizada para facilitar el mantenimiento:

```text
torneo_tec/
├── Jugador.py       # Definición de la Superclase.
├── Competidor.py    # Definición de Subclase para competidores.
├── Observador.py    # Definición de Subclase para espectadores.
└── main.py          # Pruebas unitarias e instanciación de objetos.
