import turtle

t = turtle.Turtle()
t.speed(5)

# Fungsi untuk menggambar lingkaran berwarna
def lingkaran_warna(x, y, radius, warna):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Gambar kepala kucing
lingkaran_warna(0, 0, 50, "orange")

# Gambar mata
lingkaran_warna(-20, 20, 10, "white")
lingkaran_warna(20, 20, 10, "white")

# Gambar pupil
lingkaran_warna(-20, 20, 5, "black")
lingkaran_warna(20, 20, 5, "black")

# Gambar hidung
lingkaran_warna(0, 0, 5, "pink")

t.hideturtle()
turtle.done()