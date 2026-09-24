"""Calculo del promedio de una lista de numeros."""


def calcular_promedio(numeros: list[float]) -> float:
    """Calcula el promedio de una lista de numeros.

    Args:
        numeros: lista de valores numericos.

    Returns:
        El promedio (media aritmetica) de los valores de la lista.
    """
    suma = 0
    for numero in numeros:
        suma = suma + numero
    return suma / len(numeros)


def main() -> None:
    """Punto de entrada del script."""
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))


if __name__ == "__main__":
    main()
