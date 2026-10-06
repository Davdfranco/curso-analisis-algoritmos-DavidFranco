# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** David Stiven Franco Lopez · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `b280226`

Muy buen trabajo en general: el código y el análisis práctico están sólidos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 19 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **87 / 100** |
| **Nota (0–5)** | **4.35** |

## 1. Corrección conceptual (18 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que alcance en las cuatro horas, y explica por qué duplicar el servidor solo es una solución temporal.
- Da un segundo ejemplo propio (el sistema de seguridad del centro comercial) y explica qué restricción se incumpliría.
- Relaciona la ejecución diaria del proceso con el consumo de energía acumulado y nombra al paciente como quien asume el costo del error.

**Lo que puede mejorar:**
- El ejemplo del centro comercial no trae cifras (cuántos eventos, cuánto tiempo máximo); con números sería más concreto.
- Decir que el tiempo crece "exponencialmente" con `O(n²)` no es correcto: el crecimiento es cuadrático.
- Del segundo perjuicio (el operador del centro de contacto) no queda claro quién asume el costo.
- En la tensión sobre el orden de la lista, el texto habla de equilibrar velocidad y exactitud. Lo que se pedía era reconocer que, como el orden decide a quién se llama primero, el ordenamiento debe ser siempre correcto además de rápido.

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué se toma cada uno, justifica que usaría el peor caso por la ventana estricta y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Calcula insertion sort línea a línea y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- El caso promedio de insertion sort se explica de forma aproximada (`t_i ≈ i/2`); faltó mostrar la suma completa.
- Para el mejor caso de insertion sort convendría contar con más cuidado las comparaciones (`n - 1`).

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `list.sort()`.
- `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores dan listas del tamaño pedido, sin repetidos y con semilla; el estilo del código es limpio.

**Lo que puede mejorar:**
- Las funciones `medir` no tienen tipos en todos sus parámetros (`generador`, `algoritmo`).

## 4. Calidad del análisis de las gráficas (19 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el promedio (A), y lo contrasta con su predicción.
- El concepto técnico recomienda merge sort, usa un dato medido (n = 6400) para responder sobre el servidor, extrapola a 1.200.000 registros declarándolo como estimación y discute la memoria.

**Lo que puede mejorar:**
- No dice en el informe que cada tiempo es la mediana de tres repeticiones; la forma de medir es parte del resultado.
- La gráfica de comparaciones no indica unidades en el eje vertical.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta y archivos con la estructura pedida, informe en el orden correcto, gráficas visibles, enlaces al código en cada parte práctica y más de cinco commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción usan un comando de activación propio de Windows; convendría indicar también el de macOS/Linux.
- Los commits del laboratorio se hicieron casi todos en pocos minutos; es mejor ir registrando el avance mientras se trabaja.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ambos algoritmos ordenan correctamente y las gráficas se generan. Los tiempos coinciden con lo que muestra el informe.

## Para el próximo laboratorio
- Acompañe los ejemplos propios con cifras concretas.
- Use "cuadrático" o "exponencial" según corresponda y revise esa diferencia.
- Al hablar de decisiones que afectan a personas, explique qué obligación adicional trae cada una (aquí: que el orden sea siempre correcto).
- Declare en el informe cómo midió (repeticiones, mediana) y rotule todos los ejes con unidades.
- Haga commits a medida que avanza y deje instrucciones para varios sistemas operativos.
