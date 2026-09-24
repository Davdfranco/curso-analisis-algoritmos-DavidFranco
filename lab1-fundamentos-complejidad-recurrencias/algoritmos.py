"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de menor a mayor. No modifica la lista recibida: trabaja
    sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = actual

    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de menor a mayor. No modifica la lista recibida: trabaja
    sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    comparaciones = 0

    def _merge_sort(lista: list[int]) -> list[int]:
        nonlocal comparaciones

        if len(lista) <= 1:
            return lista

        medio = len(lista) // 2
        izquierda = _merge_sort(lista[:medio])
        derecha = _merge_sort(lista[medio:])

        return _merge(izquierda, derecha)

    def _merge(izquierda: list[int], derecha: list[int]) -> list[int]:
        nonlocal comparaciones
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones += 1
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    ordenada = _merge_sort(datos.copy())
    return ordenada, comparaciones
