def limpiar_powerclip(shape):

    try:

        if shape.PowerClip.Shapes.Count == 0:
            return

        internos = []

        for interno in shape.PowerClip.Shapes:
            internos.append(interno)

        for interno in internos:
            interno.Delete()

    except:
        pass