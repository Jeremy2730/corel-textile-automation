# corel/personalization/logo_scale_manager.py

from config.tallas import (
    TALLAS_NINOS,
    TALLAS_ADULTOS,
    TALLAS_ESPECIALES
)

from config.logo_sizes import (
    LOGO_SIZES
)


def interpolar(minimo, maximo, idx, total):

    if total <= 0:
        return minimo

    factor = idx / total

    return minimo + (
        (maximo - minimo) * factor
    )


def calcular_alto_logo(
    asset_name,
    talla
):

    talla = talla.upper()

    config = LOGO_SIZES[
        asset_name
    ]

    # 🔥 TALLAS ESPECIALES
    if talla in TALLAS_ESPECIALES:

        return config["max_adulto"]

    # =========================================
    # 👦 NIÑOS
    # =========================================

    if talla in TALLAS_NINOS:

        minimo = config["min_nino"]
        maximo = config["max_nino"]

        idx = TALLAS_NINOS.index(
            talla
        )

        total = (
            len(TALLAS_NINOS) - 1
        )

        return interpolar(
            minimo,
            maximo,
            idx,
            total
        )

    # =========================================
    # 🧑 ADULTOS
    # =========================================

    if talla in TALLAS_ADULTOS:

        minimo = config["min_adulto"]
        maximo = config["max_adulto"]

        idx = TALLAS_ADULTOS.index(
            talla
        )

        total = (
            len(TALLAS_ADULTOS) - 1
        )

        return interpolar(
            minimo,
            maximo,
            idx,
            total
        )

    # fallback
    return config["min_adulto"]