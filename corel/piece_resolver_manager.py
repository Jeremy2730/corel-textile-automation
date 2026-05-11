from corel.shape_manager import (buscar_shape_por_nombre)
from corel.origen_manager import (buscar_shape_origen)

def resolver_shapes_transferencia(
    doc_base,
    page,
    origen_nombre,
    destino_nombre
):

    shape_destino = (
        buscar_shape_por_nombre(
            page.Shapes,
            destino_nombre
        )
    )

    shape_origen = (
        buscar_shape_origen(
            doc_base,
            origen_nombre
        )
    )

    return (
        shape_origen,
        shape_destino
    )