"""Medicion comparativa: lista enlazada frente a tabla hash.

Experimento A: tiempo de busqueda de guias inexistentes frente al
numero de guias n, con la tabla en un factor de carga cercano a 2.
Experimento B: tiempo de busqueda frente al factor de carga alfa,
con n fijo.

Guarda las graficas en graficas/lista_vs_tabla.png y
graficas/tiempo_vs_alfa.png.
"""

import gc
import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from estructuras import ListaEnlazada, TablaHash

TAMANIOS = [100, 500, 1000, 5000, 10000, 20000, 50000, 100000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 7, 10]
BUSQUEDAS = 200
REPETICIONES_LISTA = 15
REPETICIONES_TABLA = 51
RONDAS_TABLA = 7
MUESTRA_EXISTENTES = 200
SEMILLA = 7
ESTADOS = ["en bodega", "en reparto", "entregado"]
CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un numero entero es primo.

    Args:
        numero: entero a evaluar.

    Returns:
        True si el numero es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: int) -> int:
    """Busca el primo mas cercano a un valor dado.

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a `objetivo` (el menor si hay empate).
    """
    distancia = 0
    while True:
        if es_primo(objetivo - distancia):
            return objetivo - distancia
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def generar_guias(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n guias distintas de diez digitos.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador, para reproducir los datos.

    Returns:
        Lista de n enteros distintos entre 10**9 y 10**10 - 1.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def construir(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con las mismas guias.

    Args:
        guias: guias a insertar, en el mismo orden en ambas.
        m: numero de casillas de la tabla.

    Returns:
        Una tupla con la lista enlazada y la tabla hash.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = estado_de(guia)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def estado_de(guia: int) -> str:
    """Asigna un estado a una guia, sin depender del orden de insercion.

    Args:
        guia: numero de guia del envio.

    Returns:
        Uno de los estados de ESTADOS, siempre el mismo para la guia.
    """
    return ESTADOS[guia % len(ESTADOS)]


def construir_tabla(guias: list[int], m: int) -> TablaHash:
    """Construye solo una tabla hash con las guias dadas.

    Args:
        guias: guias a insertar, en el orden dado.
        m: numero de casillas de la tabla.

    Returns:
        La tabla hash con todas las guias insertadas.
    """
    tabla = TablaHash(m)
    for guia in guias:
        tabla.insertar(guia, estado_de(guia))
    return tabla


def verificar_tabla(
    tabla: TablaHash, guias: list[int], inexistentes: list[int]
) -> None:
    """Comprueba que una tabla reconstruida responde correctamente.

    Args:
        tabla: tabla ya construida con `guias`.
        guias: guias almacenadas en la tabla.
        inexistentes: guias que no estan almacenadas.
    """
    azar = random.Random(SEMILLA)
    muestra = azar.sample(guias, min(MUESTRA_EXISTENTES, len(guias)))
    for guia in muestra:
        assert tabla.buscar(guia) == estado_de(guia), (
            f"La tabla devolvio un estado incorrecto para {guia}"
        )
    for guia in inexistentes:
        assert tabla.buscar(guia) is None, f"Tabla hallo la guia {guia}"


def barajar(guias: list[int], ronda: int) -> list[int]:
    """Devuelve las guias en un orden distinto para cada ronda.

    Args:
        guias: guias originales.
        ronda: numero de ronda; con la misma ronda el orden se repite.

    Returns:
        Una copia de `guias` mezclada con semilla fija.
    """
    copia = list(guias)
    random.Random(SEMILLA + ronda).shuffle(copia)
    return copia


def verificar(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
    inexistentes: list[int],
) -> None:
    """Comprueba que lista y tabla devuelven lo mismo.

    Revisa una muestra de guias existentes y todas las inexistentes.

    Args:
        lista: lista enlazada ya construida.
        tabla: tabla hash ya construida.
        guias: guias almacenadas en ambas estructuras.
        inexistentes: guias que no estan almacenadas.
    """
    azar = random.Random(SEMILLA)
    muestra = azar.sample(guias, min(MUESTRA_EXISTENTES, len(guias)))
    for guia in muestra:
        estado_lista = lista.buscar(guia)
        assert estado_lista is not None, f"La lista perdio la guia {guia}"
        assert estado_lista == tabla.buscar(guia), (
            f"Lista y tabla difieren en la guia existente {guia}"
        )
    for guia in inexistentes:
        assert lista.buscar(guia) is None, f"Lista hallo la guia {guia}"
        assert tabla.buscar(guia) is None, f"Tabla hallo la guia {guia}"


def medir(
    estructura: ListaEnlazada | TablaHash,
    guias: list[int],
    repeticiones: int,
) -> float:
    """Mide el tiempo medio por busqueda de una estructura.

    Cronometra solo el ciclo de busquedas. Repite la tanda completa
    `repeticiones` veces y devuelve el promedio por busqueda de la
    tanda mas rapida. El ruido del sistema operativo solo suma tiempo,
    nunca lo resta, asi que la tanda mas rapida es la que menos
    interferencia tuvo (el mismo criterio de timeit en Python).

    Args:
        estructura: lista o tabla ya construida.
        guias: guias a buscar (las mismas para ambas estructuras).
        repeticiones: cuantas veces se repite la tanda de busquedas.

    Returns:
        Tiempo medio por busqueda, en microsegundos.
    """
    promedios: list[float] = []
    gc.collect()
    gc.disable()
    try:
        for _ in range(repeticiones):
            inicio = time.perf_counter()
            for guia in guias:
                estructura.buscar(guia)
            fin = time.perf_counter()
            promedios.append((fin - inicio) / len(guias))
    finally:
        gc.enable()
    return min(promedios) * 1e6


def medir_tabla_en_rondas(
    guias: list[int], m: int, inexistentes: list[int]
) -> float:
    """Mide la tabla reconstruyendola en varias rondas.

    En cada ronda se construye una tabla nueva (insertando las guias
    en otro orden) y se mide con `medir`. El resultado es la mediana
    de las rondas (cada una ya es su tanda mas rapida), para no
    depender de como quedo acomodada la memoria en una sola
    construccion. La construccion no se cronometra.

    Args:
        guias: guias a almacenar.
        m: numero de casillas de la tabla.
        inexistentes: guias a buscar.

    Returns:
        Mediana de los tiempos medios por busqueda, en microsegundos.
    """
    tiempos = []
    for ronda in range(RONDAS_TABLA):
        tabla = construir_tabla(barajar(guias, ronda), m)
        verificar_tabla(tabla, guias, inexistentes)
        tiempos.append(medir(tabla, inexistentes, REPETICIONES_TABLA))
    return statistics.median(tiempos)


def experimento_a() -> tuple[list[int], list[int], list[float], list[float]]:
    """Compara lista y tabla para distintos numeros de guias.

    Returns:
        Tupla con los valores de n, los m usados, los tiempos medios
        de la lista y los tiempos medios de la tabla (microsegundos).
    """
    ms: list[int] = []
    t_lista: list[float] = []
    t_tabla: list[float] = []
    for n in TAMANIOS:
        m = primo_cercano(n // 2)
        guias = generar_guias(n)
        inexistentes = generar_guias_inexistentes(
            set(guias), BUSQUEDAS, SEMILLA
        )
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias, inexistentes)
        t_lista.append(
            medir(lista, inexistentes, REPETICIONES_LISTA)
        )
        del lista, tabla
        t_tabla.append(
            medir_tabla_en_rondas(guias, m, inexistentes)
        )
        ms.append(m)
        print(
            f"n={n:>7}  m={m:>6}  alfa={n / m:5.2f}  "
            f"lista={t_lista[-1]:10.3f} us  tabla={t_tabla[-1]:7.3f} us"
        )
    return TAMANIOS, ms, t_lista, t_tabla


def experimento_b() -> tuple[list[int], list[float], list[float]]:
    """Mide la tabla con n fijo y distintos factores de carga.

    Las rondas se intercalan: en cada una se mide todos los alfa antes
    de pasar a la siguiente, para que un cambio de carga del equipo
    no afecte a un solo alfa. El tiempo de cada alfa es la mediana de
    sus rondas.

    Returns:
        Tupla con los m usados, los factores de carga reales y los
        tiempos medios por busqueda (microsegundos).
    """
    guias = generar_guias(N_FIJO)
    inexistentes = generar_guias_inexistentes(
        set(guias), BUSQUEDAS, SEMILLA
    )
    ms = [primo_cercano(round(N_FIJO / alfa)) for alfa in ALFAS]
    for m in ms:
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias, inexistentes)
    del lista, tabla
    por_alfa: list[list[float]] = [[] for _ in ms]
    for ronda in range(RONDAS_TABLA):
        orden = barajar(guias, ronda)
        for posicion, m in enumerate(ms):
            tabla = construir_tabla(orden, m)
            verificar_tabla(tabla, guias, inexistentes)
            por_alfa[posicion].append(
                medir(tabla, inexistentes, REPETICIONES_TABLA)
            )
    alfas = [N_FIJO / m for m in ms]
    tiempos = [statistics.median(tandas) for tandas in por_alfa]
    for m, alfa, tiempo in zip(ms, alfas, tiempos):
        print(f"n={N_FIJO}  m={m:>6}  alfa={alfa:6.3f}  "
              f"tabla={tiempo:7.3f} us")
    return ms, alfas, tiempos


def graficar_a(
    ns: list[int], t_lista: list[float], t_tabla: list[float]
) -> None:
    """Dibuja lista vs tabla en escala lineal y logaritmica.

    Args:
        ns: valores de n.
        t_lista: tiempos medios de la lista (microsegundos).
        t_tabla: tiempos medios de la tabla (microsegundos).
    """
    fig, ejes = plt.subplots(1, 2, figsize=(13, 5))
    for eje, escala in zip(ejes, ("linear", "log")):
        eje.plot(ns, t_lista, marker="o", label="Lista enlazada")
        eje.plot(ns, t_tabla, marker="s", label="Tabla hash (alfa ≈ 2)")
        eje.set_xscale(escala)
        eje.set_yscale(escala)
        eje.set_xlabel("Número de guías n (envíos)")
        eje.set_ylabel("Tiempo medio por búsqueda (µs)")
        eje.grid(True, alpha=0.3)
        eje.legend()
    ejes[0].set_title("Búsqueda de guía inexistente (escala lineal)")
    ejes[1].set_title("Búsqueda de guía inexistente (escala logarítmica)")
    fig.tight_layout()
    fig.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close(fig)


def graficar_b(alfas: list[float], tiempos: list[float]) -> None:
    """Dibuja el tiempo de la tabla frente al factor de carga.

    Args:
        alfas: factores de carga reales de cada tabla.
        tiempos: tiempos medios por busqueda (microsegundos).
    """
    pendiente, intercepto = np.polyfit(alfas, tiempos, 1)
    xs = np.linspace(min(alfas), max(alfas), 50)
    plt.figure(figsize=(8, 5))
    plt.plot(alfas, tiempos, marker="o", label="Tiempo medido")
    plt.plot(
        xs,
        pendiente * xs + intercepto,
        linestyle="--",
        label=f"Recta ajustada (t = {intercepto:.2f} + "
        f"{pendiente:.2f}·α)",
    )
    plt.title(f"Tabla hash: tiempo de búsqueda vs. factor de carga "
              f"(n = {N_FIJO:,})".replace(",", "."))
    plt.xlabel("Factor de carga α = n / m (guías por casilla)")
    plt.ylabel("Tiempo medio por búsqueda (µs)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()
    print(f"\nRecta ajustada: t = {intercepto:.3f} + {pendiente:.3f}*alfa")


def main() -> None:
    """Ejecuta los dos experimentos y guarda las graficas."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    print(f"Repeticiones: lista {REPETICIONES_LISTA}, "
          f"tabla {REPETICIONES_TABLA} x {RONDAS_TABLA} rondas "
          f"(tanda mas rapida de {BUSQUEDAS} busquedas)\n")
    print("Experimento A: lista frente a tabla")
    ns, _, t_lista, t_tabla = experimento_a()
    graficar_a(ns, t_lista, t_tabla)
    print("\nExperimento B: efecto del factor de carga")
    _, alfas, tiempos = experimento_b()
    graficar_b(alfas, tiempos)
    print(f"\nGraficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    main()
