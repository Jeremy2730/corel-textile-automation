from config.piezas import PIEZAS
from config.productos import PRODUCTOS


def obtener_piezas_producto(
    producto
):

    piezas = []

    piezas_permitidas = (
        PRODUCTOS[producto]
    )

    for origen, destino in PIEZAS.items():

        if destino not in piezas_permitidas:
            continue

        piezas.append(
            (origen, destino)
        )

    return piezas