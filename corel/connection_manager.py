import win32com.client


def conectar_corel():

    try:

        app = None

        for v in range(20, 30):

            try:

                app = win32com.client.Dispatch(
                    f"CorelDRAW.Application.{v}"
                )

                print(f"✅ Conectado a CorelDRAW v{v}")

                break

            except:
                continue

        if not app:

            print("❌ No se encontró CorelDRAW")

            return None

        app.Visible = True

        print("🟢 Corel listo")

        return app

    except Exception as e:

        print("❌ Error conectando Corel:", e)

        return None