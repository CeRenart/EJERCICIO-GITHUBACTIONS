import sys

print("Iniciando escaneo de seguridad en ventas.json...")

with open("ventas.json", "r", encoding="utf-8") as f:
    contenido = f.read()

if "API_KEY" in contenido or "SECRET" in contenido:
    print("ALERTA: Se ha detectado una posible clave API expuesta.")
    sys.exit(1)

print("Escaneo completado: No se encontraron claves API expuestas.")