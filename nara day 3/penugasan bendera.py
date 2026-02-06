import turtle
import time

t = turtle.Turtle()
t.speed(3)
t.width(2)

screen = turtle.Screen()
screen.bgcolor("lightgray")

def gambar_persegi(warna):
    t.color("black", warna)
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

# POSISI AWAL (ATAS)
t.penup()
t.goto(-150, 100)
t.pendown()

# PUTIH (atas) ✅
gambar_persegi("white")

time.sleep(0.5)

# MERAH (bawah) ✅
t.penup()
t.goto(-150, 0)
t.pendown()
gambar_persegi("red")

t.hideturtle()
turtle.done()