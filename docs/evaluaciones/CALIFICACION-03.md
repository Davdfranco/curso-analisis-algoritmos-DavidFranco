# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** David Stiven Franco Lopez · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `e28f1f2`

Excelente trabajo: su informe se apoya en sus propias mediciones y es honesto sobre lo que no pudo comprobar.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **100 / 100** |
| **Nota (0–5)** | **5.00** |

## 1. Corrección conceptual (20 / 20)
**Lo que hizo bien:**
- Explica bien la colisión con el ejemplo de las guías 10, 24 y 17 con m = 7, y compara encadenamiento y direccionamiento abierto con ventajas y costos.
- Justifica por qué la tabla no sirve para rangos y estima la altura y las comparaciones del árbol degenerado frente al equilibrado.
- Declara que la cifra para 5.000.000 de envíos es una estimación y explica por qué la curva de la lista no es una simple regla de tres.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla.
- Nombra la dispersión uniforme como supuesto y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Lista y tabla funcionan, la tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`.
- Las pruebas cubren la colisión con m = 7, `factor_carga` = 3/7 y veinte colecciones aleatorias, y pasan.
- Todas las funciones tienen *docstrings* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados con unidades y leyenda; la primera cubre ocho valores de `n` y la segunda siete valores de `α`.
- Calcula factores de crecimiento para todos los pares de `n` y los contrasta con `Θ(n)` y `Θ(1)`; en la segunda gráfica ajusta una recta y la interpreta.
- Explica con cuidado qué diferencias son ruido y cuáles parecen reales.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada: `lab3-estructuras-datos/` con todos los archivos del entregable.
- El informe sigue el orden pedido, las gráficas se ven con ruta relativa, cada parte enlaza su código y hay instrucciones de reproducción.
- Hay cinco commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y las estructuras responden correctamente. Las mediciones están hechas con semilla fija y generan las dos gráficas.
