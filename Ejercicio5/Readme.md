# 🐾 Ejemplo: Abstracción Básica con Animales

Este proyecto sirve como una introducción técnica al uso del módulo `abc` en Python. Demuestra cómo definir una interfaz común para diferentes tipos de objetos (Perros y Gatos) asegurando que todos compartan un comportamiento base: `hablar()`.

## 🏗️ Estructura de Clases

El código sigue el patrón de diseño de **Clase Base Abstracta (ABC)**:

1.  **Clase `Animal` (Abstracta):** Define el contrato. No se puede instanciar y obliga a sus hijos a implementar el método `hablar()`.
2.  **Clase `Perro` (Concreta):** Implementa el contrato devolviendo `"Guau"`.
3.  **Clase `Gato` (Concreta):** Implementa el contrato devolviendo `"Miau"`.

## 🛠️ Conceptos Clave Ilustrados

* **Contratos de Software:** La clase `Animal` garantiza que cualquier objeto considerado un "Animal" tendrá un método para comunicarse.
* **Polimorfismo:** Un mismo método (`hablar()`) produce resultados diferentes dependiendo del objeto que lo invoque.
* **Encapsulamiento de Comportamiento:** Cada subclase decide internamente cómo se realiza la acción de hablar.

## 📝 Notas de Implementación (Correcciones)

Para que el código funcione perfectamente en un entorno de producción, se deben observar los siguientes detalles:

* **Importación:** Se prefiere el uso de `@abstractmethod` sobre `@abstractclassmethod` para métodos de instancia simples.
* **Sintaxis:** Asegurarse de cerrar correctamente los paréntesis en la definición de métodos y corregir nombres de clases heredadas (ej. de `Animasl` a `Animal`).

## 🚀 Ejemplo de Ejecución
```python
# Salida esperada al ejecutar el script:
"Guau"
"Miau"
