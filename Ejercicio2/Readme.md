# 🏦 Sistema de Gestión Bancaria: POO en Python
**Concepto:** Encapsulamiento de Métodos y Gestión de Estado Interno  
**Proyecto:** Simulación de transacciones para cuentas de ahorro.

## 📖 Descripción
Este proyecto implementa una clase robusta llamada `CuentaBancaria`, diseñada para gestionar las operaciones financieras básicas de un usuario. El enfoque principal es el **manejo dinámico del saldo**, asegurando que las operaciones de retiro y depósito actualicen correctamente el estado del objeto.

## 🛠️ Funcionalidades del Sistema
El código permite realizar las siguientes acciones críticas:

1.  **💰 Depósito:** Incrementa el saldo de la cuenta de forma acumulativa.
2.  **💸 Retiro con Validación:** Incluye una regla de negocio que impide retirar más dinero del disponible, retornando un mensaje de "Saldo insuficiente" en caso de error.
3.  **🔍 Consulta de Saldo:** Método dedicado para obtener el estado actual de los fondos.
4.  **📋 Reporte de Información:** Genera un resumen amigable con el nombre del titular y su balance actual.

## 📊 Casos de Prueba Implementados
El script ejecuta simulaciones para dos perfiles distintos, demostrando la independencia de los objetos en memoria:

| Titular | Saldo Inicial | Operaciones Realizadas | Resultado Final |
| :--- | :--- | :--- | :--- |
| **Ivan Zero** | $2,000.0 | Depósito $700, Retiro $500, Depósito $5,000 | $7,200.0 |
| **Rut Rojas** | $5,000.0 | Depósito $200, Retiro $6,000 (Fallido) | $5,200.0 |

# 🐾 Simulador de Cuidado de Mascotas: POO en Python
**Concepto:** Gestión de Estados Dinámicos y Reglas de Validación  
**Proyecto:** Sistema de interacción y bienestar para mascotas virtuales.

## 📖 Descripción
Este proyecto implementa la clase `Mascota`, diseñada para modelar el comportamiento y las necesidades básicas de un animal doméstico. El sistema utiliza **encapsulamiento de lógica** para controlar el "Nivel de Felicidad", asegurando que los valores se mantengan dentro de un rango lógico (0-100) mediante validaciones internas.

## 🛠️ Funcionalidades del Sistema
El código permite gestionar el ciclo de bienestar de la mascota a través de los siguientes métodos:

1.  **🍖 Alimentar:** Incrementa el nivel de felicidad en **10 puntos**.
2.  **🎾 Jugar:** Incrementa el nivel de felicidad en **20 puntos**.
3.  **🛡️ Limitador de Rango:** Ambos métodos de interacción incluyen un "techo" de **100 puntos**, evitando que el valor exceda el límite máximo permitido.
4.  **❓ Validación de Estado (`esFeliz`):** Un método booleano que determina si la mascota tiene un nivel de bienestar óptimo (mayor a 70).

## 📊 Casos de Prueba
El script simula la evolución de dos mascotas con diferentes estados iniciales:

| Mascota | Especie | Felicidad Inicial | Proceso de Cuidado | ¿Es Feliz al final? |
| :--- | :--- | :--- | :--- | :--- |
| **Stella** | 🐈 Gato | 50 pts | Alimentar (+10) + Jugar (+20) | **Sí** (80 pts) |
| **Spike** | 🐕 Perro | 10 pts | Alimentar (+10) + Jugar (+20) | **No** (40 pts) |
