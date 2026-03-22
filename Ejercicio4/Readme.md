# 📂 Colección de Proyectos: Programación Orientada a Objetos
**Semestre:** 2° Semestre  
**Temas:** Modularidad, Herencia, Especialización e Importación de Clases.

## 📝 Descripción General
Este repositorio contiene dos aplicaciones prácticas que demuestran la capacidad de organizar código en múltiples archivos y carpetas, facilitando el mantenimiento y la escalabilidad de sistemas complejos en Python.

---

## 🍽️ Proyecto 1: Sistema de Gestión de Menú
Este módulo simula la administración de productos en un restaurante, categorizando elementos por su naturaleza y atributos específicos.

### 🍱 Estructura de Clases
* **Comida:** Maneja platos principales con atributos de categoría (Entrada, Fuerte).
* **Bebida:** Gestiona el inventario de líquidos y su temperatura (Fría/Caliente).
* **Postre:** Controla detalles específicos como restricciones alimentarias.

**Ejemplo de implementación:**
```python
Pozole = Comida("Pozole rojo", 85.0, "Principal")
Sangría = Bebida("Bebida de sangría", 35.0, "Fría")
