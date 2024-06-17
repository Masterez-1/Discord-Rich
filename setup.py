# Este archivo sirve a la hora de compilarlo en la consola con;
# python setup.py build
# esto genera la carpeta con el ejecutable

from cx_Freeze import setup, Executable
import sys

# Nombre del archivo de tu script Python e icono
script = 'DiscordRichMZ.py'
icon = 'icon.ico'  # Icono (La ruta es la default, si la pones en carpeta asegurate de poner el directorio)

# Definir la base en función del sistema operativo
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Esto suprime la consola

# Archivos adicionales a incluir
files = ['config.json', 'icon.ico']

# Configuración de la build
setup(
    name='Presencia de Discord',
    version='2.0',
    description='Discord Rich MZ',
    options={"build_exe": {"include_files": files}},
    executables=[Executable(script, base=base, icon=icon)]
)
