# Discord Rich Presence Bot

Este proyecto permite integrar un **Discord Rich Presence** altamente configurable en tu aplicación utilizando Python. Es ideal para mostrar detalles personalizados en tu perfil de Discord, como estado, imágenes, botones y más.

---

## 🎯 Características

- **Presencia personalizada**: Define texto, imágenes y botones adaptados a tus necesidades.
- **Actualización automática**: Mantiene la conexión con Discord y actualiza el estado cada 15 segundos.
- **Configuración sencilla**: Archivo `config.json` para personalizar tu presencia sin modificar el código.
- **Icono en bandeja**: Soporte para un icono interactivo en la bandeja del sistema.
- **Consola estilizada**: Créditos y enlaces al repositorio estilizados con `pyfiglet`.

---

## 🛠️ Requisitos

Antes de empezar, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.8 o superior
- Librerías de Python:
  - `pypresence`
  - `pystray`
  - `Pillow`
  - `pyfiglet`

Instala las dependencias ejecutando:

```bash
pip install pypresence pystray pillow pyfiglet
```

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/Masterez-1/Discord-Rich.git
cd Discord-Rich
```

### 2. Configurar el archivo
Edita el archivo `config.json` generado automáticamente en la primera ejecución. Un ejemplo de configuración predeterminada:

```json
{
    "client_id": "ID_CLIENTE_DISCORD",
    "state": "Estado personalizado",
    "details": "Detalles personalizados",
    "large_image": "Nombre_imagen",
    "large_text": "Texto_imagen",
    "small_image": "Nombre_imagen",
    "small_text": "Texto_imagen",
    "party_id": "ID_PARTY_DISCORD",
    "buttons": [
        {"label": "Botón 1", "url": "https://ejemplo.com"},
        {"label": "Botón 2", "url": "https://ejemplo.com"}
    ]
}
```

### 3. Ejecutar el script
```bash
python main.py
```

Al iniciar, verás los créditos en la consola y se establecerá la conexión con Discord.

### 4. Icono en bandeja
Un icono aparecerá en la bandeja del sistema. Haz clic derecho para cerrar la aplicación de forma segura.

---

## 📂 Estructura del proyecto

```plaintext
Discord-Rich/
├── config.json         # Archivo de configuración generado automáticamente
├── icon.ico            # Icono para la bandeja del sistema
├── main.py             # Código principal
├── README.md           # Documentación del proyecto
```

---

## 🛡️ Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estas pautas:

1. Haz un fork del proyecto.
2. Crea una rama para tu característica (`git checkout -b nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva característica'`).
4. Haz push a tu rama (`git push origin nueva-caracteristica`).
5. Abre un Pull Request.

---

## ⚠️ Notas importantes

- Solo se permiten **dos botones** en Discord Rich Presence.
- Usa imágenes previamente subidas al portal de aplicaciones de Discord.
- Para "Compilar" Ejecutar el "Setup.py" y genera una build con el exe.

---

## ✨ Créditos

- **Autor**: [Masterez-1](https://github.com/Masterez-1)
- **Repositorio**: [Discord Rich](https://github.com/Masterez-1/Discord-Rich)

---

