# 🛡️ Guía de Práctica: Manejo de Excepciones en Python
**Nivel:** De Básico a Avanzado  
**Concepto:** Gestión de Errores en Tiempo de Ejecución (Runtime Errors)

## ⚡ ¿Qué es una Excepción?
Una excepción es un evento que ocurre durante la ejecución de un programa e interrumpe su flujo normal. En lugar de permitir que el programa "truene" (crash), Python nos permite **atrapar** el error, manejarlo con gracia y continuar la ejecución.

### El Bloque Maestro: `try / except`
| Bloque | Función |
| :--- | :--- |
| **`try`** | Código "peligroso" que podría fallar. |
| **`except`** | Se ejecuta solo si ocurrió un error en el `try`. |
| **`else`** | Se ejecuta solo si **NO** hubo errores. |
| **`finally`** | Se ejecuta **siempre** (ideal para cerrar archivos o limpiar memoria). |

---

## 📋 Diccionario de Errores Comunes
Para ser un experto, debes identificar estas excepciones frecuentes:

* **`ZeroDivisionError`**: Intentar dividir un número entre 0.
* **`ValueError`**: Tipo de dato correcto, pero valor inapropiado (ej: `int("hola")`).
* **`TypeError`**: Operación entre tipos incompatibles (ej: `len(5)`).
* **`IndexError`**: Intentar acceder a un índice que no existe en una lista.
* **`KeyError`**: Buscar una clave inexistente en un diccionario.

---

## 🎯 Reto Integrador: Registro de Calificaciones
El objetivo de este reto es construir un sistema de gestión académica blindado contra errores de usuario.

### Especificaciones del Sistema:
1.  **Validación de Entrada:** Uso de una función `pedir_entero` para asegurar que el usuario no ingrese texto donde se esperan números.
2.  **Excepciones Personalizadas:** Creación de `CalificacionFueraDeRangoError` para validar que las notas estén estrictamente entre **0 y 100**.
3.  **Flujo de Cierre:** Uso de `finally` para mostrar un reporte de sesión (cantidad de alumnos registrados) sin importar si el proceso fue exitoso o fallido.

> *Nota: Las funciones de persistencia en archivos (.txt) y manejo de `PermissionError` quedan reservadas para la siguiente fase de la práctica.*

---

## 🛠️ Cómo Probar los Ejercicios
1. Ejecuta el script de práctica:
   ```bash
   python manejo_excepciones.py
