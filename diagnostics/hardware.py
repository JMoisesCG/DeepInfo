import platform
import psutil

def get_hardware_info():
    try:
        info = []

        info.append(f"Procesador: {platform.processor()}")
        info.append(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
        info.append(f"Núcleos lógicos: {psutil.cpu_count(logical=True)}")

        ram_total = psutil.virtual_memory().total / (1024 ** 3)
        info.append(f"RAM total: {ram_total:.2f} GB")

        return "\n".join(info)
    except Exception as e:
        return f"Error al obtener información de hardware: {e}"