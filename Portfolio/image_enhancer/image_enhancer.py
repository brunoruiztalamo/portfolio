import tkinter as tk
import pyautogui
import os

def guardar_notas():
    notas = text_widget.get("1.0", "end-1c")  # Obtener el contenido del widget de texto
    with open("notas.txt", "w") as archivo:
        archivo.write(notas)

def cerrar_ventana():
    root.destroy()

def minimizar_ventana():
    root.iconify()

root = tk.Tk()
root.title("Bloc de Notas")
root.geometry('400x300+100+100')  # Definir el tamaño y la posición de la ventana

# Crear un widget de texto con scrollbars
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget = tk.Text(root, yscrollcommand=scrollbar.set)
text_widget.pack(fill='both', expand=True)

scrollbar.config(command=text_widget.yview)

# Agregar imagen de fondo
image_path = r'C:/VSCODE/Portfolio/widget bloc notas python/hojita.png'
background_image = tk.PhotoImage(file=image_path)

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, anchor='nw', image=background_image)

text_widget = tk.Text(root)
text_widget.pack(fill='both', expand=True)

# Configurar el widget de texto
text_widget.configure(font=("Arial", 12), bg='white', fg='black')
text_widget.configure(borderwidth=0, highlightthickness=0)

# Agregar botones para guardar, minimizar y cerrar
boton_guardar = tk.Button(root, text="Guardar", command=guardar_notas)
boton_guardar.pack(side=tk.LEFT, padx=5, pady=5)

boton_minimizar = tk.Button(root, text="Minimizar", command=minimizar_ventana)
boton_minimizar.pack(side=tk.LEFT, padx=5, pady=5)

boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(side=tk.LEFT, padx=5, pady=5)

# Mover la ventana al hacer clic y arrastrar en cualquier lugar
def mover_ventana(event):
    x, y = pyautogui.position()
    root.geometry(f'+{x}+{y}')

root.bind('<B1-Motion>', mover_ventana)

root.after(0, root.attributes, '-topmost', 1)  # Mantener la ventana por encima de otras
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Detectar el cierre de ventana

root.mainloop()


