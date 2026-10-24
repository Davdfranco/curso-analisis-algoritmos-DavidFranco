# Retroalimentación — Laboratorio evaluativo 02

**Estudiante:** David Stiven Franco Lopez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `e2e7e60`

Excelente trabajo: un laboratorio completo, bien verificado y con análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **99 / 100** |
| **Nota (0–5)** | **4.95** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica dónde divide y vencerás empieza a ganar y explica por qué pierde con series muy cortas (costo de las llamadas recursivas).
- Compara con el máximo de un arreglo: combinar cuesta `Θ(1)`, la recurrencia da `Θ(n)` y por eso dividir no ayuda.
- Recomienda divide y vencerás y declara que la cifra para 1.000.000 de registros es una estimación, con su razonamiento (16,5 horas contra 5,7 segundos).

**Lo que puede mejorar:**
- El "cruce" entre n=10 y n=50 se apoya en una diferencia muy pequeña en n=50 (0,000151 s contra 0,000145 s). Sería más prudente decir que ahí los dos son casi iguales y que la ventaja clara aparece desde n=100.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término.
- Aplica el método maestro y verifica que el caso 2 se cumple.
- Justifica por qué la fuerza bruta es `Θ(n²)` (n²/2 pares con trabajo constante cada uno).

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en las listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta, y ninguna función modifica la lista recibida.
- Sus pruebas además comprueban que los índices devueltos sumen lo que se reporta. El código cumple PEP 8, con *type hints* y *docstrings*.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes; cubre siete tamaños.
- El factor al duplicar n (×3,93 para fuerza bruta y ×2,07 para divide y vencerás) se calcula bien y se contrasta con lo teórico.
- La tabla de valores medidos es un buen complemento para leer los tamaños pequeños.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, informe en el orden pedido, gráfica visible, enlaces al código en cada parte e instrucciones de reproducción claras.
- Hay tres commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre sin errores y genera la gráfica. Los tiempos de su equipo son distintos a los de otro computador, pero la forma de las curvas es la misma.

## Para el próximo laboratorio
- Apoye cada afirmación sobre un tamaño concreto con los valores medidos, como lo hizo con su tabla.
- Cuando dos tiempos sean casi iguales, descríbalos como empate en lugar de un cruce exacto.
- Mantenga los commits pequeños y descriptivos, como en este laboratorio.
