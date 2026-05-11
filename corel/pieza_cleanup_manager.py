def obtener_shapes_a_eliminar(
    shapes,
    piezas_permitidas
):

    eliminar = []

    for shape in shapes:

        nombre_shape = shape.Name.lower()

        if nombre_shape not in piezas_permitidas:

            eliminar.append(shape)

    return eliminar