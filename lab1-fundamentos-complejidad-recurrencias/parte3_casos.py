"""Experimento de la Parte 3: peor, mejor y caso promedio de insertion sort."""

import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANIOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}


def medir(generador, n: int) -> tuple[float, int]:
    """Mide el tiempo mediano y las comparaciones de insertion_sort.

    Genera el lote una sola vez y ejecuta insertion_sort varias veces
    sobre el mismo lote para obtener un tiempo mediano mas estable.
    El tiempo de generacion de datos no se cronometra.

    Args:
        generador: funcion que genera el lote de datos (recibe n).
        n: tamanio del lote a generar y ordenar.

    Returns:
        Una tupla con el tiempo mediano en segundos y el numero de
        comparaciones (constante entre repeticiones para un mismo lote).
    """
    lote = generador(n)
    tiempos = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(lote)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    return statistics.median(tiempos), comparaciones


def main() -> None:
    """Ejecuta el experimento y genera las graficas de la Parte 3."""
    resultados: dict[str, dict[str, list[float]]] = {
        nombre: {"tiempos": [], "comparaciones": []} for nombre in ESCENARIOS
    }

    for nombre, generador in ESCENARIOS.items():
        print(f"Escenario {nombre}:")
        for n in TAMANIOS:
            tiempo, comparaciones = medir(generador, n)
            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(f"  n={n:>5}  tiempo={tiempo:.6f}s  comparaciones={comparaciones}")

    plt.figure(figsize=(8, 5))
    for nombre in ESCENARIOS:
        plt.plot(TAMANIOS, resultados[nombre]["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    for nombre in ESCENARIOS:
        plt.plot(TAMANIOS, resultados[nombre]["tiempos"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecución vs. tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()

    print("\nGraficas guardadas en graficas/parte3_comparaciones.png y graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()
