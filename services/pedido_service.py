from config.productos import PRODUCTOS
from config.aliases import ALIASES_TALLAS
from config.tallas import TALLAS_ESPECIALES


def crear_pedido(
    tallas_existentes,
    tallas_base
):

    print("\n📦 Productos disponibles:\n")

    productos_disponibles = list(PRODUCTOS.keys())

    for p in productos_disponibles:
        print(f" - {p}")

    pedido_texto = input(
        "📦 Cantidades por talla, cantidad, producto (ej: 4XL:2:camiseta): "
    ).strip()

    pedido = []

    items = pedido_texto.split(",")

    for item in items:

        item = item.strip()

        if not item:
            continue

        try:

            talla, cantidad, producto = item.split(":")

            talla = talla.strip().upper()

            # aliases
            if talla in ALIASES_TALLAS:
                talla = ALIASES_TALLAS[talla]

            cantidad = int(cantidad.strip())

            producto = producto.strip().lower()

            # validar talla
            if talla not in tallas_existentes:

                print(
                    f"⚠️ La talla {talla} no existe en plantilla"
                )

                continue

            # validar producto
            if producto not in productos_disponibles:

                print(
                    f"⚠️ Producto inválido: {producto}"
                )

                continue

            # validar tallas especiales
            if talla in TALLAS_ESPECIALES:

                if talla not in tallas_base:

                    print(
                        f"⚠️ No existe diseño base para talla especial {talla}"
                    )

                    continue

            pedido.append({

                "talla": talla,
                "cantidad": cantidad,
                "producto": producto
            })

        except Exception as e:

            print(f"❌ Formato inválido: {item}")
            print(e)

    return pedido