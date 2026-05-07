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

                if nombre not in pedido:
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

                cantidad = pedido.get(nombre_base, 1)

                page.Name = f"{nombre_base}_1"

                for n in range(2, cantidad + 1):

                    doc.AddPages(1)

                    nueva_pagina = doc.Pages.Item(doc.Pages.Count)

                    nueva_pagina.Name = f"{nombre_base}_{n}"

                    page.Activate()

                    sr = page.Shapes.All()

                    sr.CreateSelection()

                    self.app.ActiveSelection.Duplicate()

                    duplicados = self.app.ActiveSelectionRange

                    nueva_pagina.Activate()

                    for shape in duplicados:
                        shape.MoveToLayer(nueva_pagina.ActiveLayer)

            # ✅ RESUMEN FUERA DEL LOOP
            print("\n📦 Producción generada:\n")

            total = 0

            for talla, cantidad in pedido.items():
                print(f"{talla} → {cantidad} unidades")
                total += cantidad

            print(f"\n✅ Total páginas: {total}")

            print("✅ Páginas duplicadas correctamente")

        except Exception as e:
            print("❌ Error duplicando páginas:", e)