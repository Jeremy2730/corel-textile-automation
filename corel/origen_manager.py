# corel/origen_manager.py


def buscar_shape_en_contenedor(
    shapes,
    nombre_buscar
):

    nombre_buscar = (
        nombre_buscar
        .strip()
        .lower()
    )

    for shape in shapes:

        try:

            nombre = (
                shape.Name
                .strip()
                .lower()
            )

            # ✅ encontrado directo
            if nombre == nombre_buscar:
                print("🔍", nombre)

                return shape

            # ✅ buscar dentro de powerclip
            try:

                if shape.PowerClip:

                    encontrado = (
                        buscar_shape_en_contenedor(
                            shape.PowerClip.Shapes,
                            nombre_buscar
                        )
                    )

                    if encontrado:

                        return encontrado

            except:
                pass

        except:
            pass

    return None


def buscar_shape_origen(
    doc,
    nombre_shape
):

    for page in doc.Pages:

        encontrado = (
            buscar_shape_en_contenedor(
                page.Shapes,
                nombre_shape
            )
        )

        if encontrado:

            return encontrado

    return None