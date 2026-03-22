# ⛏️ Práctica 3: Abstracción en POO con Python
**Semestre:** 2° Semestre  
**Temática:** 🎮 Universo Minecraft  
**Concepto Clave:** Clases Abstractas y Contratos de Interfaz

## ⬛ Objetivo de Aprendizaje
El objetivo de esta práctica es dominar el concepto de **abstracción** mediante el uso del módulo `abc` (Abstract Base Classes) en Python. Se busca comprender cómo una clase abstracta define un **contrato** que obliga a las subclases a implementar comportamientos específicos, garantizando la integridad de la jerarquía de objetos.

---

## 💎 Contenido de la Práctica

### 🌍 Problema 1: Los Mobs del Overworld
Se modeló la jerarquía de entidades (mobs) utilizando una clase base abstracta `Mob`.
* **Clases Implementadas:** `Vaca`, `Creeper`, `Enderman` y `Zombie` (Bonus).
* **Métodos Abstractos:** `hacer_sonido()`, `comportamiento()` y `moverse()`.
* **Observación Técnica:** Al intentar instanciar la clase `Mob` directamente, Python lanza un `TypeError`. Esto confirma que las clases abstractas no pueden existir como objetos independientes, sino que sirven únicamente como moldes.

### 🔨 Problema 2: La Fábrica de Herramientas
Implementación de un sistema de forja que utiliza **propiedades abstractas** para definir atributos obligatorios.
* **Herramientas:** `Pico`, `Espada`, `Pala` y `Arco` (Bonus con gestión de flechas).
* **Lógica de Desgaste:** Cada uso reduce la durabilidad según el material (Madera, Piedra, Hierro, Oro, Diamante, Netherita).
* **Encapsulamiento:** Uso de atributos protegidos (`_material`, `_usos_restantes`) para gestionar el estado interno de la herramienta.

---

## 📦 Conceptos de Programación Aplicados
* **`ABC` / `ABCMeta`:** Para definir la naturaleza abstracta de las clases.
* **`@abstractmethod`:** Para obligar a la implementación de lógica en las subclases.
* **`@property` abstracta:** Para asegurar que cada herramienta tenga un nombre definido.
* **Polimorfismo:** Un mismo método (`usar()` o `presentarse()`) actúa de forma distinta según el objeto que lo ejecute.

---

## 🛠️ Instrucciones de Ejecución
1. Asegúrate de tener instalado **Python 3.8+**.
2. Clona el repositorio o descarga los archivos `.py`.
3. Ejecuta los scripts desde la terminal:
   ```bash
   python problema_1_mobs.py
   python problema_2_herramientas.py
