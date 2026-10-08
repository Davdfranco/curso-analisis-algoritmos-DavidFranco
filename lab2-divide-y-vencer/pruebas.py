"""Pruebas de las dos soluciones del subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo, suma_cruzada


def suma_directa(valores: list[float], inicio: int, fin: int) -> float:
    # Suma el tramo [inicio, fin] recorriendolo, para confirmar que los
    # indices que devuelve cada funcion realmente corresponden a su suma.
    total = 0.0
    for indice in range(inicio, fin + 1):
        total += valores[indice]
    return total


def verificar(serie: list[float], suma_esperada: float | None = None) -> None:
    original = list(serie)

    bruta = subarreglo_fuerza_bruta(serie)
    dyv = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert serie == original, f"la lista de entrada fue modificada: {serie}"
    assert bruta[2] == dyv[2], (
        f"las dos soluciones no coinciden para {serie}: "
        f"bruta={bruta} dyv={dyv}"
    )
    assert bruta[2] == suma_directa(serie, bruta[0], bruta[1]), (
        f"los indices de fuerza bruta no coinciden con su suma: {bruta}"
    )
    assert dyv[2] == suma_directa(serie, dyv[0], dyv[1]), (
        f"los indices de divide y venceras no coinciden con su suma: {dyv}"
    )
    if suma_esperada is not None:
        assert bruta[2] == suma_esperada, (
            f"se esperaba suma {suma_esperada} y se obtuvo {bruta[2]}"
        )


# Caso 1: la serie de ocho dias de la situacion problema (suma esperada 17).
verificar([-3, 5, -2, 8, -6, 3, 9, -4], 17)

# Caso 2: series de un solo elemento.
verificar([5], 5)
verificar([-5], -5)

# Caso 3: todos los valores son negativos; la mejor racha es el dia
# menos malo, no la serie completa.
verificar([-5, -2, -9, -14], -2)
verificar([-10, -1, -10], -1)

# Caso 4: todos los valores son positivos; la mejor racha es la serie
# completa.
verificar([2, 4, 1, 3], 10)
verificar([7, 7, 7], 21)

# Caso 5: el mejor tramo cruza el punto medio, por lo que ninguna mitad
# por separado alcanza la suma maxima.
verificar([-2, 6, -1, 7, -3], 12)
verificar([3, -8, 4, 4, -8, 3], 8)

# Caso 6: suma_cruzada se revisa por separado, forzando el tramo a tocar
# ambas mitades.
assert suma_cruzada([-3, 5, -2, 8, -6, 3, 9, -4], 0, 3, 7)[2] == 17
assert suma_cruzada([-5, -2, -9, -14], 0, 1, 3)[2] == -11

# Caso 7: veinte listas aleatorias con semilla fija, para que el docente
# pueda reproducir exactamente los mismos casos.
generador = random.Random(17)
for _ in range(20):
    tamanio = generador.randint(1, 80)
    serie_aleatoria = [generador.randint(-100, 100) for _ in range(tamanio)]
    verificar(serie_aleatoria)

print("Todas las pruebas pasaron correctamente.")
