"""Experimento de la Parte 4: validacion experimental de la complejidad."""

import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANIOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ALGORITMOS = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


def medir(algoritmo, lote: list[int]) -> float:
    """Mide el tiempo mediano de ejecucion de un algoritmo sobre un lote.

    El tiempo de generacion de datos no se cronometra: el lote ya
    viene generado antes de llamar a esta funcion.

    Args:
        algoritmo: funcion de ordenamiento (insertion_sort o merge_sort).
        lote: lista de datos a ordenar en cada repeticion.

    Returns:
        El tiempo mediano en segundos sobre REPETICIONES ejecuciones.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(lote)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return statistics.median(tiempos)


def main() -> None:
    """Ejecuta el experimento comparativo y genera la grafica de la Parte 4."""
    resultados: dict[str, list[float]] = {nombre: [] for nombre in ALGORITMOS}

    for n in TAMANIOS:
        lote = generar_aleatorio(n)
        print(f"n={n:>5}", end="  ")
        for nombre, algoritmo in ALGORITMOS.items():
            tiempo = medir(algoritmo, lote)
            resultados[nombre].append(tiempo)
            print(f"{nombre}={tiempo:.6f}s", end="  ")
        print()

    plt.figure(figsize=(8, 5))
    for nombre in ALGORITMOS:
        plt.plot(TAMANIOS, resultados[nombre], marker="o", label=nombre)
    plt.title("Tiempo de ejecucion vs. tamaño de entrada (escenario A - aleatorio)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()

    print("\nGrafica guardada en graficas/parte4_tiempo.png")


if __name__ == "__main__":
    main()
