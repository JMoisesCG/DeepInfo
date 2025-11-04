import platform
import getpass

def get_system_info():
    info = [
        f"Usuario: {getpass.getuser()}",
        f"Sistema operativo: {platform.system()}",
        f"Versión: {platform.version()}",
        f"Arquitectura: {platform.machine()}",
        f"Nombre del equipo: {platform.node()}",
    ]
    return "\n".join(info)