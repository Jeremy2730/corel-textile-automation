from corel.shape_manager import buscar_shape_por_nombre


def buscar_shape_origen(
    doc_base,
    origen_nombre
):

    for page in doc_base.Pages:

        shape = buscar_shape_por_nombre(
            page.Shapes,
            origen_nombre
        )

        if shape:
            return shape

    return None