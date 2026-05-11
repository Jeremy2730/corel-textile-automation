def eliminar_shapes(shapes):

    for shape in shapes:

        print(
            f"🗑️ Eliminando pieza: {shape.Name}"
        )

        shape.Delete()