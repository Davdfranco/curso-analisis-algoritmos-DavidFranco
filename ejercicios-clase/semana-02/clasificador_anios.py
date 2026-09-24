"""Clasificador de anios bisiestos.

Complete las funciones siguiendo la especificacion de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un anio es bisiesto.

    Un anio es bisiesto si es divisible por 4, excepto los anios
    divisibles por 100 que no lo sean tambien por 400.

    Args:
        anio: anio a evaluar (numero entero).

    Returns:
        True si el anio es bisiesto, False en caso contrario.
    """
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de anios separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas invalidas).

    Returns:
        Lista de anios como enteros.
    """
    while True:
        entrada = input("Ingrese anios separados por comas (ej. 2000,2023,2024): ")
        partes = [parte.strip() for parte in entrada.split(",") if parte.strip()]
        try:
            anios = [int(parte) for parte in partes]
            return anios
        except ValueError:
            print("Entrada invalida. Ingrese solo numeros enteros separados por comas.")


def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    bisiestos = [anio for anio in anios if es_bisiesto(anio)]

    print()
    print(f"Anios ingresados: {anios}")
    print(f"Anios bisiestos: {bisiestos}")
    print(f"Cantidad de anios bisiestos: {len(bisiestos)} de {len(anios)}")


if __name__ == "__main__":
    main()
