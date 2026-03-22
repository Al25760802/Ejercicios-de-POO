# 🔨 Proyecto: La Fábrica de Herramientas (Minecraft Forge)

Este módulo simula un sistema de forja y gestión de durabilidad para herramientas de **Minecraft**, aplicando conceptos avanzados de encapsulamiento y propiedades abstractas.

## 🛠️ Características Técnicas
* **@property Abstracta:** Uso de decoradores para obligar a definir el nombre de la herramienta en las subclases.
* **Gestión de Daño:** Diccionario de mapeo según el material (Madera hasta Netherita).
* **Sistema de Desgaste:** Lógica de reducción de usos y estado de rotura (`self.rota`).

## 💎 Herramientas Incluidas
1. **Pico:** Especializado en minería de menas.
2. **Espada:** Diseñada para el combate y cálculo de daño a mobs.
3. **Pala:** Optimizada para excavación de suelos.
4. **Arco (Bonus):** Sistema de combate a distancia con gestión limitada de flechas.

## 🚀 Ejemplo de Salida
Al ejecutar el script, el sistema simula el uso de una herramienta hasta su destrucción:
```text
Pico de diamante mina mena de diamante (daño: 6)
[Pico de diamante] ✅ 4 usos
...
[Pico de diamante] 💔 ROTA
