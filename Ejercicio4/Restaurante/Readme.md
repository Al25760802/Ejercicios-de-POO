# 🍽️ Sistema de Gestión de Menú: Restaurante POO

Este módulo demuestra el uso de **importaciones modulares** y **especialización de clases** en Python. El sistema permite gestionar diferentes categorías de productos (Comidas, Bebidas y Postres) manteniendo una estructura de código limpia y organizada.

## 📂 Estructura del Proyecto

Para que este script funcione, el proyecto se organiza en los siguientes módulos:
* `comida.py`: Define la clase `Comida` y atributos como el tipo de platillo (Entrada, Principal).
* `bebida.py`: Define la clase `Bebida` y atributos como la temperatura (Fría/Caliente).
* `postre.py`: Define la clase `Postre` y atributos booleanos (ej. si contiene gluten o azúcar).
* `main.py`: Punto de entrada donde se instancian los objetos y se muestra la información.

## 🚀 Implementación del Menú

En el script principal, se han configurado los siguientes elementos de prueba:

| Objeto | Descripción | Precio | Atributo Especial |
| :--- | :--- | :--- | :--- |
| **Pozole** | Pozole rojo | $85.0 | Plato Principal |
| **Sangría** | Bebida de sangría | $35.0 | Temperatura: Fría |
| **Chocoflan** | Chocoflan | $45.0 | Sin gluten/azúcar (False) |

## 🛠️ Conceptos Clave
* **Modularidad:** Uso de `from modulo import Clase` para evitar archivos de código gigantes y difíciles de mantener.
* **Instanciación:** Creación de objetos específicos con parámetros personalizados (Nombre, Precio, Categoría).
* **Consistencia de Interfaz:** Todos los objetos implementan los métodos `mostrar_info()` y `tipo()`, permitiendo una salida de datos uniforme.

## 📊 Ejemplo de Salida en Consola
```text
Nombre: Pozole rojo | Precio: 85.0
Tipo de platillo: Principal
---
Nombre: Bebida de sangrìa | Precio: 35.0
Categoría: Fría
---
Nombre: chocoflan | Precio: 45.0
Detalle: Postre estándar
