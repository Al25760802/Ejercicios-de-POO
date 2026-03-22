🎓 Sistema de Gestión de Estudiantes (POO)
Este proyecto es una implementación básica de Programación Orientada a Objetos (POO) en Python. 
Permite modelar el comportamiento de un estudiante, gestionar sus calificaciones y calcular promedios de forma automática.

🚀 Características
Modelado de Datos: Almacena nombre, edad y carrera.

Gestión de Calificaciones: Permite añadir múltiples notas a un historial dinámico.

Cálculo Automático: Incluye un método para obtener el promedio aritmético.

Interacción: Método integrado para presentar la información del usuario de forma amigable.

🛠️ Estructura de la Clase
La clase Estudiante cuenta con los siguientes componentes:

Componente	Descripción
__init__	Constructor que inicializa los datos básicos y una lista vacía de calificaciones.
setCalificaciones	Método para agregar una nueva nota a la lista.
mostrarPromedio	Calcula la media. Retorna 0 si no hay calificaciones para evitar errores de división.
mostrarInformacionUsuario	Retorna un saludo con los datos principales del estudiante.
💻 Ejemplo de Uso
Python
# Crear un nuevo estudiante
estudiante = Estudiante("David", 22, "Ing. en sistemas")

# Agregar notas
estudiante.setCalificaciones(70)
estudiante.setCalificaciones(100)

# Ver resultados
print(estudiante.mostrarInformacionUsuario())
print(f"Promedio: {estudiante.mostrarPromedio()}")
📋 Requisitos
Python 3.x
