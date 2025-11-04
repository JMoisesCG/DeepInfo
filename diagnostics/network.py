import socket

def get_network_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        info = [
            f"Nombre del host: {hostname}",
            f"Dirección IP local: {ip_address}",
        ]
        return "\n".join(info)
    except Exception as e:
        return f"Error al obtener información de red: {e}"