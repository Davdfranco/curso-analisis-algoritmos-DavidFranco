"""Medicion comparativa: fuerza bruta frente a divide y venceras.

Mide el tiempo de ejecucion de las dos soluciones del subarreglo
maximo sobre la misma serie de variaciones de caja, para varios
tamanios de entrada, y guarda la grafica en graficas/tiempo_vs_n.png.
"""

import random
import statistics
import time
from typing import Callable

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANIOS = [10, 50, 100, 500, 1000, 4000, 8000]
REPETICIONES = 5
SEMILLA = 42


def generar_serie(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera una serie de variacion diaria de caja.

    Args:
        n: cantidad de dias de la serie.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n variaciones enteras entre -100 y 100.
    """
    rng = random.Random(semilla)
    return [rng.randint(-100, 100) for _ in range(n)]


def medir(
    algoritmo: Callable[..., tuple[int, int, float]], *args: object
) -> tuple[float, tuple[int, int, float]]:
    """Mide el tiempo mediano de un algoritmo sobre los mismos datos.

    El tiempo de generacion de los datos no se cronometra: los
    argumentos ya vienen construidos cuando se llama a esta funcion.

    Args:
        algoritmo: funcion a medir (subarreglo_fuerza_bruta o
            subarreglo_maximo).
        *args: argumentos con los que se invoca el algoritmo.

    Returns:
        Una tupla con el tiempo mediano en segundos y el resultado
        (inicio, fin, suma) de la ultima ejecucion.
    """
    tiempos = []
    resultado = None
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado = algoritmo(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return statistics.median(tiempos), resultado


def main() -> None:
    """Ejecuta el experimento y genera la grafica de tiempo vs. tamanio."""
    tiempos_bruta = []
    tiempos_dyv = []

    for n in TAMANIOS:
        serie = generar_serie(n)

        tiempo_bruta, resultado_bruta = medir(subarreglo_fuerza_bruta, serie)
        tiempo_dyv, resultado_dyv = medir(subarreglo_maximo, serie, 0, n - 1)

        assert resultado_bruta[2] == resultado_dyv[2], (
            f"n={n}: las soluciones no coinciden "
            f"({resultado_bruta[2]} vs {resultado_dyv[2]})"
        )

        tiempos_bruta.append(tiempo_bruta)
        tiempos_dyv.append(tiempo_dyv)
        print(
            f"n={n:>5}  fuerza_bruta={tiempo_bruta:.6f}s  "
            f"divide_y_venceras={tiempo_dyv:.6f}s"
        )

    plt.figure(figsize=(8, 5))
    plt.plot(TAMANIOS, tiempos_bruta, marker="o", label="Fuerza bruta")
    plt.plot(TAMANIOS, tiempos_dyv, marker="o", label="Divide y vencerás")
    plt.title("Subarreglo máximo: tiempo de ejecución vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada n (días)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_n.png")
    plt.close()

    print("\nGrafica guardada en graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    main()
