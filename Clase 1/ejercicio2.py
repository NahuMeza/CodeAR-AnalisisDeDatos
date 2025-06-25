import tkinter as tk

contador = 0

def aumentar():
    global contador
    contador += 1
    etiqueta.config(text=f"Contador: {contador}")

def reducir():
    global contador
    contador -= 1
    etiqueta.config(text=f"Contador: {contador}")  

ventana = tk.Tk()
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Contador: 0", font=("Arial", 20))
etiqueta.pack(pady=10)

boton_aumentar = tk.Button(ventana, text="Aumentar", command=aumentar)
boton_aumentar.pack()

boton_reducir = tk.Button(ventana, text ="decrementar", command=reducir)
boton_reducir.pack()

ventana.mainloop()

# Agrega un boton que decremente el contador