import win32com.client

for v in range(15, 30):
    try:
        app = win32com.client.Dispatch(f"CorelDRAW.Application.{v}")
        print(f"✅ Encontrado: CorelDRAW.Application.{v}")
        break
    except:
        pass

print("Prueba terminada")