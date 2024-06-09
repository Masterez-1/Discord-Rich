import json
import os
from pypresence import Presence
import time
import threading
import pystray
from pystray import MenuItem as item
from PIL import Image

# Ruta del archivo de configuración
config_path = "config.json"

# Valores predeterminados de la configuración
default_config = {
    "client_id": "ID_CLIENTE_DISCORD",
    "state": "Texto de ejemplo para el estado",
    "details": "Texto de ejemplo para detalles",
    "large_image": "Nombre_imagen",
    "large_text": "Texto_imagen",
    "small_image": "Nombre_imagen",
    "small_text": "Texto_imagen",
    "party_id": "ID_PARTY_DISCORD",
    "buttons": [
        {"label": "Mis proyectos", "url": "https://proximamente.com"},
        {"label": "Discord", "url": "https://proximamente.com"}
    ]
}

# Crear el archivo de configuración si no existe
if not os.path.exists(config_path):
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, ensure_ascii=False, indent=4)

# Leer la configuración
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Crear una instancia de Presence usando el client_id del archivo de configuración
RPC = Presence(config["client_id"])
RPC.connect()  # Conectar con Discord

# Imprimir para confirmar conexión
print("Connectado")

# Fijar el tiempo de inicio
start_time = time.time()

# Función para actualizar la presencia
def update_presence():
    RPC.update(
        state=config["state"],
        details=config["details"],
        start=start_time,  # Usar el tiempo de inicio fijo
        large_image=config["large_image"],
        large_text=config["large_text"],
        small_image=config["small_image"],
        small_text=config["small_text"],
        party_id=config["party_id"],
        buttons=config["buttons"]
    )
    print("Presencia actualizada")

def create_image(file_path):
    return Image.open(file_path)

def on_exit(icon, item):
    icon.stop()
    print("Desconectado")
    exit(0)

# Función para iniciar el icono de la bandeja
def setup_tray():
    icon = pystray.Icon("discord_presence")
    icon.icon = create_image("icon.ico")
    icon.menu = pystray.Menu(
        item('Cerrar', on_exit),
    )
    icon.run()

# Actualizar la presencia inicialmente
update_presence()

# Mantener el script corriendo y actualizar la presencia periódicamente
def presence_loop():
    try:
        while True:
            update_presence()
            time.sleep(15)  # Mantener la conexión activa
    except KeyboardInterrupt:
        print("Desconectado")

# Ejecutar el loop de presencia en un hilo separado
thread = threading.Thread(target=presence_loop)
thread.daemon = True
thread.start()

# Iniciar el icono de la bandeja
setup_tray()
