import tkinter as tk
from tkinter import scrolledtext

from diagnostics.system_info import get_system_info
from diagnostics.network import get_network_info
from diagnostics.hardware import get_hardware_info

def iniciar_gui():
    ventana = tk.Tk()
    ventana.title("DeepInfo")
    ventana.geometry("800x600")
    ventana.resizable(False, False)

    salida_texto = scrolledtext.ScrolledText(
        ventana, wrap=tk.WORD, width=85, height=20, font=("Consolas", 10)
    )
    salida_texto.pack(pady=10)

    def mostrar_info(funcion):
        try:
            resultado = funcion()
        except Exception as e:
            resultado = f"⚠️ Error: {e}"
        salida_texto.delete(1.0, tk.END)
        salida_texto.insert(tk.END, resultado)

    marco_botones = tk.Frame(ventana)
    marco_botones.pack(pady=5)

    tk.Button(marco_botones, text="🖥️ Sistema", width=20,
              command=lambda: mostrar_info(get_system_info)).grid(row=0, column=0, padx=5)
    tk.Button(marco_botones, text="🌐 Red", width=20,
              command=lambda: mostrar_info(get_network_info)).grid(row=0, column=1, padx=5)
    tk.Button(marco_botones, text="⚙️ Hardware", width=20,
              command=lambda: mostrar_info(get_hardware_info)).grid(row=0, column=2, padx=5)
    tk.Button(marco_botones, text="❌ Salir", width=20,
              command=ventana.quit).grid(row=0, column=3, padx=5)

    ventana.mainloop()