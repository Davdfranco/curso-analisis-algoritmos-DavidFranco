"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    racha_inicio = 0
    racha_fin = 0
    mejor_suma = float(valores[0])

    for dia_inicial in range(len(valores)):
        acumulado = 0.0
        for dia_final in range(dia_inicial, len(valores)):
            acumulado += valores[dia_final]
            if acumulado > mejor_suma:
                mejor_suma = acumulado
                racha_inicio = dia_inicial
                racha_fin = dia_final

    return racha_inicio, racha_fin, mejor_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    acumulado = 0.0
    mejor_extremo_izq = medio
    mejor_suma_izq = float("-inf")
    for dia in range(medio, inicio - 1, -1):
        acumulado += valores[dia]
        if acumulado > mejor_suma_izq:
            mejor_suma_izq = acumulado
            mejor_extremo_izq = dia

    acumulado = 0.0
    mejor_extremo_der = medio + 1
    mejor_suma_der = float("-inf")
    for dia in range(medio + 1, fin + 1):
        acumulado += valores[dia]
        if acumulado > mejor_suma_der:
            mejor_suma_der = acumulado
            mejor_extremo_der = dia

    return mejor_extremo_izq, mejor_extremo_der, mejor_suma_izq + mejor_suma_der


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, float(valores[inicio])

    medio = (inicio + fin) // 2
    resultado_izq = subarreglo_maximo(valores, inicio, medio)
    resultado_der = subarreglo_maximo(valores, medio + 1, fin)
    resultado_cruz = suma_cruzada(valores, inicio, medio, fin)

    if resultado_izq[2] >= resultado_der[2] and resultado_izq[2] >= resultado_cruz[2]:
        return resultado_izq
    if resultado_der[2] >= resultado_cruz[2]:
        return resultado_der
    return resultado_cruz
