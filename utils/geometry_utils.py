def get_shape_bounds(shape):

    return {
        "x": shape.PositionX,
        "y": shape.PositionY,
        "width": shape.SizeWidth,
        "height": shape.SizeHeight
    }


def get_shape_center(shape):

    bounds = get_shape_bounds(shape)

    return (
        bounds["x"] + bounds["width"] / 2,
        bounds["y"] + bounds["height"] / 2
    )