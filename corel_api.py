import win32com.client
import shutil
import os


class CorelAPI:
    def __init__(self):
        self.app = None
        self.doc = None

    def conectar(self):
        try:
            # 🔍 Detectar versión automáticamente
            for v in range(20, 30):
                try:
                    self.app = win32com.client.Dispatch(f"CorelDRAW.Application.{v}")
                    print(f"✅ Conectado a CorelDRAW v{v}")
                    break
                except:
                    continue

            if not self.app:
                print("❌ No se encontró ninguna versión de Corel")
                return False

            self.app.Visible = True

            print("🟢 Corel listo (sin documentos abiertos no hay problema)")

            return True

        except Exception as e:
            print("❌ Error al conectar con Corel")
            print(e)
            return False


    def crear_documento_desde_doc(self, doc_origen, nombre_archivo, carpeta):
        try:
            # Activar documento origen
            doc_origen.Activate()

            ruta = f"{carpeta}\\{nombre_archivo}.cdr"

            # Guardar copia directa
            doc_origen.SaveAs(ruta)

            print(f"📁 Documento creado: {ruta}")

            # Abrir el nuevo documento ya guardado
            nuevo_doc = self.app.OpenDocument(ruta)

            return nuevo_doc

        except Exception as e:
            print("❌ Error creando documento desde doc:", e)
            return None


    def copiar_archivo_base(self, ruta_origen, nombre_archivo, carpeta_destino):
        try:
            ruta_destino = os.path.join(carpeta_destino, f"{nombre_archivo}.cdr")
            
            # copiar archivo
            shutil.copy(ruta_origen, ruta_destino)
            
            print(f"📁 Archivo copiado: {ruta_destino}")
            
            # abrir en Corel
            doc = self.app.OpenDocument(ruta_destino)
            
            return doc

        except Exception as e:
            print("❌ Error copiando archivo:", e)
            return None
            
        
    def abrir_documento(self, ruta):
        try:
            doc = self.app.OpenDocument(ruta)
            print(f"📂 Abierto: {ruta}")
            return doc
        except Exception as e:
            print("❌ Error abriendo documento:", e)
            return None


    def filtrar_tallas(self, doc, pedido):
        try:
            paginas_a_borrar = []

            # recorrer páginas
            for i in range(doc.Pages.Count, 0, -1):
                page = doc.Pages.Item(i)

                nombre = page.Name.strip()

                tallas_pedido = []

                for item in pedido:
                    tallas_pedido.append(item["talla"])

                if nombre not in tallas_pedido:
                    paginas_a_borrar.append(page)

            # borrar después
            for page in paginas_a_borrar:
                print(f"🗑️ Eliminando talla: {page.Name}")
                page.Delete()

            print("✅ Tallas filtradas correctamente")

        except Exception as e:
            print("❌ Error filtrando tallas:", e)


    def duplicar_paginas(self, doc, pedido):
        try:

            paginas_originales = []

            for i in range(1, doc.Pages.Count + 1):
                paginas_originales.append(doc.Pages.Item(i))

            for page in paginas_originales:

                nombre_base = page.Name.strip()

                cantidad = 1

                for item in pedido:

                    if item["talla"] == nombre_base:

                        cantidad = item["cantidad"]
                        break

                if cantidad > 1:
                    page.Name = f"{nombre_base}_1"

                for n in range(2, cantidad + 1):

                    indice_actual = page.Index

                    doc.AddPages(1)

                    nueva_pagina = doc.Pages.Item(doc.Pages.Count)

                    # mover página al lugar correcto
                    nueva_pagina.MoveTo(
                        indice_actual + n - 1
                    )

                    nueva_pagina.Name = f"{nombre_base}_{n}"

                    page.Activate()

                    sr = page.Shapes.All()

                    sr.CreateSelection()

                    self.app.ActiveSelection.Duplicate()

                    duplicados = self.app.ActiveSelectionRange

                    nueva_pagina.Activate()

                    for shape in duplicados:
                        shape.MoveToLayer(nueva_pagina.ActiveLayer)

            print("\n📦 Producción generada:\n")

            total = 0

            for item in pedido:

                talla = item["talla"]
                cantidad = item["cantidad"]
                producto = item["producto"]

                print(f"{talla} → {cantidad} unidades ({producto})")

                total += cantidad

            print(f"\n✅ Total páginas: {total}")

            print("✅ Páginas duplicadas correctamente")

        except Exception as e:
            print("❌ Error duplicando páginas:", e)

    def limpiar_piezas_por_producto(self, doc, pedido):

        try:

            productos = {

                "camiseta": [
                    "delantero",
                    "espalda",
                    "manga_derecha",
                    "manga_izquierda"
                ],

                "buso": [
                    "delantero",
                    "espalda",
                    "manga_larga_derecha",
                    "manga_larga_izquierda"
                ],

                "uniforme": [
                    "delantero",
                    "espalda",
                    "manga_derecha",
                    "manga_izquierda",
                    "pantaloneta_derecho",
                    "pantaloneta_izquierdo"
                ],

                "uniforme_largo": [
                    "delantero",
                    "espalda",
                    "manga_larga_derecha",
                    "manga_larga_izquierda",
                    "pantaloneta_derecho",
                    "pantaloneta_izquierdo"
                ],

                "pantaloneta": [
                    "pantaloneta_derecho",
                    "pantaloneta_izquierdo"
                ]
            }

            for page in doc.Pages:

                nombre_pagina = page.Name.upper()

                talla = nombre_pagina.split("_")[0]

                producto = None

                for item in pedido:

                    if item["talla"] == talla:

                        producto = item["producto"]
                        break

                if not producto:
                    continue

                piezas_permitidas = productos[producto]

                eliminar = []

                for shape in page.Shapes:

                    nombre_shape = shape.Name.lower()

                    if nombre_shape not in piezas_permitidas:
                        eliminar.append(shape)

                for shape in eliminar:

                    print(f"🗑️ Eliminando pieza: {shape.Name}")

                    shape.Delete()

            print("✅ Piezas limpiadas según producto")

        except Exception as e:
            print("❌ Error limpiando piezas:", e)


    def listar_shapes(self, doc):

        try:

            for page in doc.Pages:

                print(f"\n📄 Página: {page.Name}")

                for shape in page.Shapes:

                    try:
                        print(
                            f" - Nombre: {shape.Name} | "
                            f"Tipo: {shape.Type}"
                        )

                    except:
                        print("❌ Error leyendo shape")

        except Exception as e:
            print("❌ Error listando shapes:", e)

    def obtener_tallas_base(self, doc):

        tallas = []

        try:

            for page in doc.Pages:

                nombre = page.Name.strip().upper()

                tallas.append(nombre)

        except:
            pass

        return tallas


    def transferir_diseno(self, doc_base, doc_resultado, pedido):

        try:

            # 🔥 mapa origen → destino
            piezas = {
                "molde_delantero": "delantero",
                "molde_espalda": "espalda",

                "molde_manga_derecha": "manga_derecha",
                "molde_manga_izquierda": "manga_izquierda",

                "molde_manga_larga_derecha": "manga_larga_derecha",
                "molde_manga_larga_izquierda": "manga_larga_izquierda",

                "molde_pantaloneta_derecho": "pantaloneta_derecho",
                "molde_pantaloneta_izquierdo": "pantaloneta_izquierdo"
            }

            productos = {

                "camiseta": [
                    "delantero",
                    "espalda",
                    "manga_derecha",
                    "manga_izquierda"
                ],

                "buso": [
                    "delantero",
                    "espalda",
                    "manga_larga_derecha",
                    "manga_larga_izquierda"
                ],

                "uniforme": [
                    "delantero",
                    "espalda",
                    "manga_derecha",
                    "manga_izquierda",
                    "pantaloneta_derecho",
                    "pantaloneta_izquierdo"
                ],

                "uniforme_largo": [
                    "delantero",
                    "espalda",
                    "manga_larga_derecha",
                    "manga_larga_izquierda",
                    "pantaloneta_derecho",
                    "pantaloneta_izquierdo"
                ],

                "pantaloneta": [
                    "pantaloneta_derecho",
                    "pantaloneta_izquierdo"
                ]
            }

            # recorrer páginas resultado
            for page in doc_resultado.Pages:

                page.Activate()

                print(f"\n📄 Procesando talla: {page.Name}")

                producto_actual = None

                talla_actual = page.Name.split("_")[0].upper()

                for item in pedido:

                    if item["talla"] == talla_actual:

                        producto_actual = item["producto"]
                        break

                if not producto_actual:
                    continue

                # recorrer piezas
                for origen_nombre, destino_nombre in piezas.items():

                    # 🔥 ignorar piezas que no pertenecen al producto
                    if destino_nombre not in productos[producto_actual]:
                        continue

                    shape_origen = None
                    shape_destino = None

                    # 🔍 buscar origen en diseño base
                    for p in doc_base.Pages:

                        for s in p.Shapes:

                            if s.Name.lower() == origen_nombre.lower():

                                shape_origen = s
                                break

                    if not shape_origen:
                        print(f"❌ No encontrado origen: {origen_nombre}")
                        continue

                    # 🔍 buscar destino en página actual
                    for s in page.Shapes:

                        if s.Name.lower() == destino_nombre.lower():

                            shape_destino = s
                            break

                    if not shape_destino:
                        print(f"❌ No encontrado destino: {destino_nombre}")
                        continue

                    if destino_nombre not in productos[producto_actual]:
                        continue

                    print(f"🎯 {origen_nombre} → {destino_nombre}")

                    # 🔥 borrar placeholder
                    try:

                        if shape_destino.PowerClip.Shapes.Count > 0:

                            internos = []

                            for interno in shape_destino.PowerClip.Shapes:
                                internos.append(interno)

                            for interno in internos:
                                interno.Delete()

                    except:
                        pass

                    # 🔥 copiar contenido interno
                    contenido = shape_origen.PowerClip.Shapes

                    for interno in contenido:

                        nombre_textura = interno.Name.lower()

                        # copiar solo texturas
                        if not nombre_textura.startswith("textura"):
                            continue

                        interno.Copy()

                        page.Activate()

                        self.app.ActiveLayer.Paste()

                        pegado = self.app.ActiveSelection.Shapes[0]

                        pegado.AddToPowerClip(shape_destino)

                        try:

                            powerclip_shapes = shape_destino.PowerClip.Shapes

                            if powerclip_shapes.Count == 0:
                                continue

                            contenido_pc = powerclip_shapes.Item(
                                powerclip_shapes.Count
                            )

                            # 📏 medidas molde
                            ancho_molde = shape_destino.SizeWidth
                            alto_molde = shape_destino.SizeHeight

                            # 📏 medidas textura original
                            ancho_textura = contenido_pc.SizeWidth
                            alto_textura = contenido_pc.SizeHeight

                            # 🔥 escala proporcional inteligente
                            escala_x = ancho_molde / ancho_textura
                            escala_y = alto_molde / alto_textura

                            # usar la MAYOR para cubrir todo
                            escala = max(escala_x, escala_y)

                            # 🔥 solo reducir si es necesario
                            if escala < 1:

                                nuevo_ancho = ancho_textura * escala
                                nuevo_alto = alto_textura * escala

                                contenido_pc.SetSize(
                                    nuevo_ancho,
                                    nuevo_alto
                                )

                            # 🔥 centrar
                            contenido_pc.CenterX = shape_destino.CenterX
                            contenido_pc.CenterY = shape_destino.CenterY

                        except Exception as e:

                            print(
                                f"⚠️ Error ajustando PowerClip: {e}"
                            )

            print("\n✅ Todas las piezas transferidas correctamente")

        except Exception as e:
            print("❌ Error transfiriendo diseño:", e)