from config.productos import PRODUCTOS
from corel.document_manager import abrir_documento
from corel.page_context_manager import obtener_contexto_pagina
from corel.piece_resolver_manager import resolver_shapes_transferencia
from corel.pieza_transfer_manager import transferir_pieza
from corel.connection_manager import conectar_corel
from corel.product_context_manager import obtener_producto_pagina
from services.pedido_utils import obtener_cantidad_por_talla
from corel.page_manager import (obtener_paginas_originales,crear_nueva_pagina, mover_pagina)
from corel.shape_duplicate_manager import (duplicar_shapes_pagina)
from services.resumen_service import (mostrar_resumen_produccion)
from corel.pieza_cleanup_manager import (obtener_shapes_a_eliminar)
from corel.delete_manager import (eliminar_shapes)
from corel.page_filter_manager import (obtener_paginas_a_borrar)
from corel.delete_page_manager import (eliminar_paginas)
from services.pedido_utils import (obtener_tallas_pedido)
from utils.logger import (log_info,log_error, log_warning)
from corel.piezas_producto_manager import (obtener_piezas_producto)
from corel.page_name_manager import (obtener_nombres_paginas)
from corel.file_manager import (copiar_archivo_base)
from corel.shape_list_manager import (listar_shapes_documento)
from corel.personalization.overlay_manager import (OverlayManager)
from corel.personalization.logo_manager import (LogoManager)
from config.logos import LOGOS
from corel.powerclip_manager import (limpiar_zonas_pagina)
from corel.personalization.logo_scale_manager import (calcular_alto_logo)


class CorelAPI:
    def __init__(self):
        self.app = None
        self.doc = None
        self.overlay_manager = OverlayManager()
        self.logo_manager = LogoManager()
        
    def conectar(self):

        self.app = conectar_corel()

        return self.app is not None


    def copiar_archivo_base(
        self,
        ruta_origen,
        nombre_archivo,
        carpeta_destino
    ):

        try:

            return copiar_archivo_base(
                self.app,
                ruta_origen,
                nombre_archivo,
                carpeta_destino
            )

        except Exception as e:

            log_error(
                f"Error copiando archivo: {e}"
            )

            return None
            
        
    def abrir_documento(self, ruta):
        return abrir_documento(self.app, ruta)


    def filtrar_tallas(self,doc,pedido):

        try:

            tallas_pedido = (
                obtener_tallas_pedido(
                    pedido
                )
            )

            paginas_a_borrar = (
                obtener_paginas_a_borrar(
                    doc.Pages,
                    tallas_pedido
                )
            )

            eliminar_paginas(
                paginas_a_borrar
            )

            log_info("Tallas filtradas correctamente")

        except Exception as e:

            log_error(
                f"Error filtrando tallas: {e}"
            )


    def duplicar_paginas(self, doc, pedido):

        try:

            paginas_originales = (
                obtener_paginas_originales(doc)
            )

            for page in paginas_originales:

                nombre_base = page.Name.strip()

                cantidad = obtener_cantidad_por_talla(
                    pedido,
                    nombre_base
                )

                if cantidad > 1:

                    page.Name = (
                        f"{nombre_base}_1"
                    )

                for n in range(2, cantidad + 1):

                    indice_actual = page.Index

                    nueva_pagina = (
                        crear_nueva_pagina(doc)
                    )

                    mover_pagina(
                        nueva_pagina,
                        indice_actual + n - 1
                    )

                    nueva_pagina.Name = (
                        f"{nombre_base}_{n}"
                    )

                    duplicar_shapes_pagina(
                        self.app,
                        page,
                        nueva_pagina
                    )

            mostrar_resumen_produccion(
                pedido
            )

            print(
                "\n✅ Páginas duplicadas correctamente"
            )

        except Exception as e:

            print(
                "❌ Error duplicando páginas:",e)

    def limpiar_piezas_por_producto(
        self,
        doc,
        pedido
    ):

        try:

            for page in doc.Pages:

                producto = obtener_producto_pagina(
                    page,
                    pedido
                )

                if not producto:
                    continue

                config_producto = (
                    PRODUCTOS[producto]
                )

                piezas_permitidas = (
                    config_producto["piezas"]
                )

                overlays = (
                    config_producto.get(
                        "overlays",
                        []
                    )
                )

                zonas = (
                    config_producto.get(
                        "zonas",
                        []
                    )
                )

                permitidos = (

                    piezas_permitidas
                    + overlays
                    + zonas
                )

                shapes_eliminar = (
                    obtener_shapes_a_eliminar(
                        page.Shapes,
                        permitidos
                    )
                )

                eliminar_shapes(
                    shapes_eliminar
                )

            print(
                "✅ Piezas limpiadas según producto"
            )

        except Exception as e:

            print(
                "❌ Error limpiando piezas:",
                e
            )


    def listar_shapes(self, doc):

        listar_shapes_documento(doc)


    def obtener_tallas_base(self, doc):

        return obtener_nombres_paginas(
            doc.Pages
        )


    def transferir_diseno(self, doc_base, doc_resultado, pedido):

        try:
            
            # recorrer páginas resultado
            for page in doc_resultado.Pages:

                page.Activate()

                print(f"\n📄 Procesando talla: {page.Name}")

                talla_actual = (
                    page.Name
                    .split("_")[0]
                    .upper()
                )

                contexto = obtener_contexto_pagina(page,pedido)

                if not contexto:
                    continue

                producto_actual = contexto["producto"]

                piezas = obtener_piezas_producto(
                    producto_actual
                )

                for origen_nombre, destino_nombre in piezas:

                    OVERLAYS_INTELIGENTES = [
                        "rayas_hombros",
                        "franja_manga_derecha",
                        "franja_manga_izquierda"
                    ]

                    if origen_nombre in OVERLAYS_INTELIGENTES:
                        continue

                    shape_origen, shape_destino = (
                        resolver_shapes_transferencia(
                            doc_base,
                            page,
                            origen_nombre,
                            destino_nombre
                        )
                    )

                    if not shape_destino:

                        log_warning(
                            f"No encontrado destino: "
                            f"{destino_nombre}"
                        )

                        continue

                    if not shape_origen:

                        log_warning(
                            f"No encontrado origen: "
                            f"{origen_nombre}"
                        )

                        continue

                    transferir_pieza(
                        self.app,
                        page,
                        shape_origen,
                        shape_destino,
                        origen_nombre,
                        destino_nombre,
                        limpiar=True
                    )

                # ← TERMINÓ EL LOOP


                shape_delantero = (
                    resolver_shapes_transferencia(
                        doc_base,
                        page,
                        "delantero",
                        "delantero"
                    )[1]
                )

                if shape_delantero:

                    self.overlay_manager.insertar_overlay_powerclip(
                        self.app,
                        page,
                        doc_base,
                        "rayas_hombros",
                        shape_delantero
                    )

                shape_manga_derecha = (
                    resolver_shapes_transferencia(
                        doc_base,
                        page,
                        "manga_derecha",
                        "manga_derecha"
                    )[1]
                )

                if shape_manga_derecha:

                    self.overlay_manager.insertar_overlay_powerclip(
                        self.app,
                        page,
                        doc_base,
                        "franja_manga_derecha",
                        shape_manga_derecha
                    )

                shape_manga_izquierda = (
                    resolver_shapes_transferencia(
                        doc_base,
                        page,
                        "manga_izquierda",
                        "manga_izquierda"
                    )[1]
                )

                if shape_manga_izquierda:

                    self.overlay_manager.insertar_overlay_powerclip(
                        self.app,
                        page,
                        doc_base,
                        "franja_manga_izquierda",
                        shape_manga_izquierda
                    )

                for logo_data in LOGOS.values():

                    pieza_destino = (
                        resolver_shapes_transferencia(
                            doc_base,
                            page,
                            logo_data["pieza"],
                            logo_data["pieza"]
                        )[1]
                    )

                    if not pieza_destino:
                        continue

                    alto_logo = calcular_alto_logo(
                        logo_data["asset"],
                        talla_actual
                    )

                    self.logo_manager.insertar_logo_powerclip(
                        self.app,
                        page,
                        doc_base,
                        logo_data["asset"],
                        logo_data["zone"],
                        pieza_destino,
                        alto_logo
                    )

                # 🔥 limpiar todas las zonas
                limpiar_zonas_pagina(page)

            log_info("Todas las piezas transferidas correctamente")

        except Exception as e:
            log_error(
                f"❌ Error transfiriendo diseño: {e}"
            )