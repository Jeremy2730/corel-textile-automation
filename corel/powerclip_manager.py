def recorrer_shapes(shapes):

    resultado = []

    for shape in shapes:

        resultado.append(shape)

        try:

            if shape.Shapes.Count > 0:

                resultado.extend(
                    recorrer_shapes(
                        shape.Shapes
                    )
                )

        except:
            pass

    return resultado


def limpiar_placeholders(shape):

    try:

        eliminar = []

        internos = recorrer_shapes(
            shape.PowerClip.Shapes
        )

        for interno in internos:

            try:

                nombre = (
                    interno.Name
                    .strip()
                    .lower()
                )

                if nombre.startswith(
                    "placeholder"
                ):

                    eliminar.append(
                        interno
                    )

            except:
                pass

        for shape_delete in eliminar:

            shape_delete.Delete()

    except:
        pass

def limpiar_zonas_pagina(page):

    try:

        eliminar = []

        for shape in page.Shapes:

            try:

                nombre = (
                    shape.Name
                    .strip()
                    .lower()
                )

                if nombre.startswith(
                    "zona_"
                ):

                    eliminar.append(
                        shape
                    )

            except:
                pass

        for shape_delete in eliminar:

            shape_delete.Delete()

    except:
        pass