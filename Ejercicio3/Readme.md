# 🐾 Sistema de Interacción Animal: POO en Python
**Concepto:** Herencia, Polimorfismo y Gestión de Instancias  
**Nivel:** Básico - Intermedio

## 📖 Descripción
Este proyecto demuestra cómo utilizar la **Programación Orientada a Objetos** para modelar comportamientos de mascotas (Perros y Gatos). Se enfoca en la creación de múltiples instancias a partir de clases importadas, permitiendo que cada objeto mantenga su propio estado (nombre y edad) y comportamiento.

## 📂 Estructura del Proyecto
Para que el sistema funcione correctamente, el código se divide en tres módulos principales:

* `Perro.py`: Contiene la lógica específica de los canes, incluyendo métodos de descripción y sonidos.
* `Gato.py`: Define el comportamiento de los felinos.
* `main.py`: Punto de entrada donde se instancian los animales y se ejecutan sus acciones.

## 🛠️ Implementación Técnica

### 1. Instanciación de Objetos
El sistema crea cuatro objetos únicos, asignándoles características específicas de identidad:

| Variable | Clase | Nombre | Edad |
| :--- | :--- | :--- | :--- |
| `pelusa` | 🐈 Gato | Pelusa | 4 años |
| `naranjo` | 🐈 Gato | Naranjo | 2 años |
| `solovino` | 🐕 Perro | Solovino | 6 años |
| `boton` | 🐕 Perro | Botón | 8 años |

### 2. Ejecución de Métodos
El script utiliza métodos **polimórficos** y **concretos**:
* **`hablar()`**: Cada animal emite su sonido característico según su especie.
* **`describir()`**: Muestra la información detallada (nombre y edad) del objeto seleccionado.

---

## 💻 Código de Ejemplo (`main.py`)
```python
from Perro import Perro
from Gato import Gato

# 1. Creación de instancias con parámetros específicos
pelusa = Gato('Pelusa', 4)
naranjo = Gato('Naranjo', 2)
solovino = Perro('Solovino', 6)
boton = Perro('Boton', 8)

# 2. Interacción con los objetos
pelusa.hablar()    # Salida: Miau!
solovino.describir() # Salida: Datos del perro Solovino
naranjo.hablar()   # Salida: Miau!
boton.hablar()     # Salida: Guau!
