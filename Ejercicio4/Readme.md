# 🚀 Proyecto Integrador: POO y Modularidad en Python
**Estudiante:** Ivan Cervantes Rojas  
**Temática:** Gestión de Menú (Restaurante) & Sistema de Héroes (RPG)

## 📝 Descripción
Este proyecto integra dos sistemas independientes en un único flujo de ejecución, demostrando el poder de la **Programación Orientada a Objetos** para resolver problemas de distintos dominios (Comercio y Videojuegos) utilizando los mismos principios de arquitectura de software.

## 📂 Estructura de Módulos Integrados
El código se apoya en una arquitectura de archivos separados para mantener la limpieza (Clean Code):

| Categoría | Módulos Relacionados | Propósito |
| :--- | :--- | :--- |
| **Gastronomía** | `Comida`, `Bebida`, `Postre` | Gestión de precios, tipos y detalles de menú. |
| **Combate RPG** | `Guerrero`, `Mago`, `Arquero` | Gestión de niveles, equipos y habilidades únicas. |

---

## 🛠️ Implementación Técnica

### 1. Sistema de Restaurante
Se instancian productos con atributos específicos que definen su comportamiento en el menú:
* **Pozole Rojo:** Plato principal ($85.0).
* **Sangría:** Bebida fría ($35.0).
* **Chocoflan:** Postre especializado ($45.0).

### 2. Sistema de Héroes
Se crean personajes con habilidades polimórficas (el mismo método realiza acciones distintas):
* **Zero (Guerrero):** Usa fuerza física con la *Espada mataDragones*.
* **JAZZ (Mago):** Ejecuta magia de área con *Vacio infinito*.
* **Arquimedes (Arquero):** Ataque a distancia con conteo de flechas.
