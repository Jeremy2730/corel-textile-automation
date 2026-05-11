def buscar_shape_por_nombre(
    shapes,
    nombre
):

    for shape in shapes:

        try:

            if shape.Name.lower() == nombre.lower():
                return shape

        except:
            pass

    return None