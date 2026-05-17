from config.tallas import (
    TALLAS_ESPECIALES,
    TALLAS_ADULTOS,
    TALLAS_NINOS
)


def mostrar_tallas(tallas):

    print("\n🎨 Tallas disponibles:\n")

    tallas_normalizadas = [

        t.strip().upper().split("_")[0]

        for t in tallas
    ]

    especiales = [
        t for t in TALLAS_ESPECIALES
        if t in tallas_normalizadas
    ]

    adultos = [
        t for t in TALLAS_ADULTOS
        if t in tallas
    ]

    ninos = [
        t for t in TALLAS_NINOS
        if t in tallas
    ]

    # 🔥 especiales
    if especiales:

        print("📌 Especiales:")

        for talla in especiales:

            print(f"   - {talla}")

        print()

    # 🔥 adultos
    if adultos:

        print("🧑 Adultos:")

        for talla in adultos:

            print(f"   - {talla}")

        print()

    # 🔥 niños
    if ninos:

        print("👦 Niños:")

        for talla in ninos:

            print(f"   - {talla}")

        print()


def mostrar_productos(productos):

    print("\n📦 Productos disponibles:\n")

    for producto in productos:

        print(f" - {producto}")