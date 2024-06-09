from cx_Freeze import setup, Executable
import sys

# Nombre del archivo de tu script Python e icono
script = 'DiscordRichMZ.py'
icon = 'icon.ico'  # Asegúrate de que la ruta del icono es correcta

# Definir la base en función del sistema operativo
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Esto suprime la consola

# Archivos adicionales a incluir
files = ['config.json', 'icon.ico']

# Configuración de la build
setup(
    name='Presencia de Discord',
    version='0.4',
    description='Mostrar en discord una presencia personalizada',
    options={"build_exe": {"include_files": files}},
    executables=[Executable(script, base=base, icon=icon)]
)
