# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** David Stiven Franco Lopez · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `f699aa7`

Excelente trabajo: informe completo, código limpio y análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 24 / 25 |
| Corrección de la implementación | 20 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue entre que el algoritmo sea correcto y que alcance en la ventana de cuatro horas, y explica por qué duplicar el servidor solo aplaza el problema.
- El segundo ejemplo (dashboard de seguridad) trae cifras y la restricción que se incumple (refrescar cada 3 segundos).
- Nombra dos perjuicios (el paciente de alto riesgo y el operador del centro de contacto) e indica quién asume el costo de cada uno.
- Explica bien la tensión: el orden decide a quién se llama primero, así que debe ser siempre correcto, no solo rápido.

**Lo que puede mejorar:**
- La relación entre tiempo de ejecución y consumo de energía queda general; faltó una cifra o un cálculo sencillo (por ejemplo, horas de servidor encendido por noche y por año).
- Hay afirmaciones que no se sostienen con el caso, como hablar de "fraude" o de una "intervención quirúrgica" cuando lo que se retrasa es la llamada de contacto.

## 2. Calidad de la explicación teórica (24 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué se toma cada uno, justifica el peor caso por la ventana estricta y deja la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Calcula insertion sort línea a línea (mejor caso con exactamente n - 1 comparaciones, caso promedio con la suma completa) y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- En el conteo línea a línea, sume también el costo de las líneas fijas del ciclo exterior para llegar al total de forma explícita.

## 3. Corrección de la implementación (20 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `list.sort()`.
- `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores dan listas del tamaño pedido, sin repetidos y con semilla.
- Cumple PEP 8, con tipos y descripciones en todas las funciones.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el promedio (A), y lo contrasta con su predicción.
- La conclusión de la Parte 4 describe lo que hace cada curva y la relaciona con O(n²) frente a Θ(n log n).
- El concepto técnico recomienda merge sort, extrapola a 1.200.000 registros declarándolo como estimación, responde sobre el servidor y discute la memoria.

**Lo que puede mejorar:**
- Los valores del informe para merge sort en n = 6400 (0,045 s y "54 veces más rápido") no coinciden con la gráfica publicada, donde merge sort está cerca de 0,035 s y la diferencia es mayor. Cite siempre lo que se lee en su propia gráfica.
- La explicación de por qué merge sort no gana con tamaños pequeños es muy breve; la gráfica casi no distingue ese tramo y faltó señalarlo con datos.
- En la gráfica de comparaciones, la unidad "(Unidades)" del eje vertical no dice nada; bastaba "número de comparaciones".

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta y archivos con la estructura pedida, informe en el orden correcto, gráficas visibles, enlaces al código en cada parte práctica e instrucciones de reproducción para Windows y macOS/Linux.
- Seis commits con mensajes descriptivos que tocan el laboratorio.

**Lo que puede mejorar:**
- Los cinco primeros commits se hicieron en un lapso de pocos minutos; es mejor registrar el avance a medida que se trabaja.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ambos algoritmos ordenan correctamente (también con listas vacías y repetidos) y las gráficas se generan con la forma que muestra el informe.

## Para el próximo laboratorio
- Cuando cite un dato del informe, verifíquelo contra la gráfica o la salida del script.
- Convierta el tiempo de ejecución en una estimación de energía con una cuenta sencilla.
- Mantenga los ejemplos del caso dentro de lo que realmente ocurre en él.
- Explique con datos qué pasa con tamaños pequeños cuando la gráfica no se ve como se espera.
- Haga commits pequeños mientras avanza.
