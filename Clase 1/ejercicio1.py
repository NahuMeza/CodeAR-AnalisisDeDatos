import turtle
import random

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "purple", "orange", "yellow"]

for i in range(100):
    t.color(random.choice(colors))
    t.forward(i)
    t.right(90)

turtle.done()

# Cambia los colores.
t.color("GREEN")
# Haz que gire 91 grados en vez de 59.
t.left(91)
# ¿Qué pasa si cambias t.forward(i) por t.forward(i * 2)?