from services.pedido_utils import (obtener_producto_por_talla)
from utils.logger import (log_warning)

def obtener_paginas_a_borrar(
    pages,
    tallas_pedido
):

    paginas = []

    for i in range(
        pages.Count,
        0,
        -1
    ):

        page = pages.Item(i)

        nombre = (
            page.Name
            .strip()
            .upper()
        )

        if nombre not in tallas_pedido:

            paginas.append(page)

    return paginas


def obtener_contexto_pagina(
    page,
    pedido
):

    talla_actual = (
        page.Name.split("_")[0].upper()
    )

    producto_actual = (
        obtener_producto_por_talla(
            pedido,
            talla_actual
        )
    )

    if not producto_actual:

        log_warning(
            f"No se encontró producto "
            f"para talla: {talla_actual}"
        )

        return None

    return {
        "talla": talla_actual,
        "producto": producto_actual
    }