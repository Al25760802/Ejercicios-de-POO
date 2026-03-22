# 🎓 Sistema de Registro Académico: POO en Python
**Concepto:** Gestión de Colecciones Dinámicas y Cálculos Agregados  
**Proyecto:** Modelo de información y desempeño para estudiantes universitarios.

## 📖 Descripción
Este proyecto implementa la clase `Estudiante`, la cual permite centralizar la información personal y académica de un alumno. La característica principal es la integración de una **lista dinámica** para almacenar calificaciones, permitiendo que el objeto calcule su propio rendimiento académico (promedio) de manera automatizada.

## 🛠️ Funcionalidades del Sistema
El código destaca por las siguientes capacidades técnicas:

1.  **📋 Constructor Multivariable:** Inicializa nombre, edad y carrera, además de preparar una lista vacía para las futuras calificaciones.
2.  **📈 Acumulación de Datos (`setCalificaciones`):** Permite añadir múltiples notas a lo largo del tiempo utilizando el método `.append()`.
3.  **🧮 Lógica Matemática (`mostrarPromedio`):** * Utiliza las funciones nativas `sum()` y `len()`.
    * Incluye una **validación de seguridad** para evitar el error de división entre cero si el estudiante aún no tiene notas registradas.
4.  **💬 Interfaz de Usuario:** Método de presentación profesional mediante *F-strings* para mostrar el perfil del estudiante.

## 📊 Casos de Prueba Implementados
El script demuestra la creación de múltiples perfiles y la gestión específica de datos para un estudiante:

| Estudiante | Carrera | Edad | Notas Registradas | Promedio Final |
| :--- | :--- | :--- | :--- | :--- |
| **Pako** | Ing. en Sistemas | 30 | (Sin registros) | 0 |
| **David** | Ing. en Sistemas | 22 | [70, 100] | **85.0** |
| **Carmen** | Ing. Industrial | 33 | (Sin registros) | 0 |
