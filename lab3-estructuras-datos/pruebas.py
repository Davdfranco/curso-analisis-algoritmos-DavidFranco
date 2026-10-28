"""Pruebas de la lista enlazada y de la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def construir(
    envios: dict[int, str], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    # Arma una lista y una tabla con exactamente los mismos envios.
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia, estado in envios.items():
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def envios_al_azar(azar: random.Random, cantidad: int) -> dict[int, str]:
    # Genera envios con guias distintas de diez digitos.
    estados = ["en bodega", "en reparto", "entregado"]
    envios: dict[int, str] = {}
    while len(envios) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in envios:
            envios[guia] = azar.choice(estados)
    return envios


# 1. Busqueda exitosa e infructuosa con la serie de la situacion problema.
serie = {
    1000000010: "en bodega",
    1000000024: "en reparto",
    1000000017: "en bodega",
    1000000005: "entregado",
}
lista, tabla = construir(serie, 7)

for guia, estado in serie.items():
    assert lista.buscar(guia) == estado
    assert tabla.buscar(guia) == estado

assert lista.buscar(1000000011) is None
assert tabla.buscar(1000000011) is None
assert lista.buscar(9999999999) is None
assert tabla.buscar(9999999999) is None
assert lista.tamano == 4
assert tabla.tamano == 4

# 2. Colision forzada: con m = 7, las guias 10, 24 y 17 caen en la casilla 3.
tabla = TablaHash(7)
assert 10 % 7 == 24 % 7 == 17 % 7 == 3
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

# Las tres guias se pueden buscar despues de colisionar.
for guia in (10, 24, 17):
    assert tabla.buscar(guia) == "en bodega"
assert tabla.buscar(3) is None

# La lista de la casilla 3 tiene longitud 3 y las demas quedaron vacias.
assert tabla.casillas[3].tamano == 3
for indice in range(7):
    if indice != 3:
        assert tabla.casillas[indice].tamano == 0

# 3. Factor de carga tras esas tres inserciones.
assert tabla.factor_carga() == 3 / 7

# 4. Veinte colecciones aleatorias: lista y tabla responden lo mismo para
#    guias existentes y para guias inexistentes. Se alternan varios m, entre
#    ellos uno muy chico, para que haya colisiones de verdad.
azar = random.Random(2026)
for numero in range(20):
    cantidad = azar.randint(1, 400)
    m = azar.choice([7, 31, 101, 211])
    envios = envios_al_azar(azar, cantidad)
    lista, tabla = construir(envios, m)

    for guia, estado in envios.items():
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado

    inexistentes = 0
    while inexistentes < 25:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in envios:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None
            inexistentes += 1

    assert lista.tamano == cantidad
    assert tabla.tamano == cantidad
    assert tabla.factor_carga() == cantidad / m

# 5. Casos de borde: lista vacia y tabla de una sola casilla (degenera en
#    una lista).
assert ListaEnlazada().buscar(1000000010) is None

una_casilla = TablaHash(1)
for guia in (10, 24, 17):
    una_casilla.insertar(guia, "en reparto")
assert una_casilla.casillas[0].tamano == 3
assert una_casilla.buscar(24) == "en reparto"
assert una_casilla.buscar(99) is None
assert una_casilla.factor_carga() == 3.0

# 6. La insercion va al inicio: la ultima guia insertada queda en la cabeza.
lista = ListaEnlazada()
lista.insertar(1, "a")
lista.insertar(2, "b")
assert lista.cabeza is not None and lista.cabeza.guia == 2

print("Todas las pruebas pasaron correctamente.")
