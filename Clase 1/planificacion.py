# import turtle

# window = turtle.Screen()
# window.bgcolor("lightblue")

# screen_turtle = turtle.Turtle()
# screen_turtle.shape("arrow")
# screen_turtle.color("green")
# screen_turtle.speed(1)

# for i in range(0,11):
#     screen_turtle.left(90)
#     screen_turtle.forward(100)

# window.mainloop()

import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

window.title("Hola Mundo!")
etiqueta1 = tk.Label(window, text="¡Hola!")
etiqueta1.pack(expand="true")

boton = tk.Button(window, text="Haz clic")
boton.pack(expand="true")

entrada = tk.Entry(window)
entrada.pack(expand="true")


window.mainloop()
