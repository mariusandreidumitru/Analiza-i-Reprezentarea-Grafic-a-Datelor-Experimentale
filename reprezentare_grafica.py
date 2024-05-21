import turtle

# Datele
x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 7, 10, 11, 10, 10, 9, 9, 7]

# Funcția liniară
a_lin = 0.1897
b_lin = 7.5287
y_lin = [a_lin * xi + b_lin for xi in x]

# Funcția parabolică
a_par = 0.091
b_par = -1.067
c_par = 13.680
y_par = [a_par * xi**2 + b_par * xi + c_par for xi in x]

# Configurare turtle
screen = turtle.Screen()
screen.setworldcoordinates(0, 0, 12, 15)
t = turtle.Turtle()
t.speed(0)

# Desenarea axelor
t.penup()
t.goto(1, 0)
t.pendown()
t.goto(1, 15)
t.penup()
t.goto(0, 1)
t.pendown()
t.goto(12, 1)

# Desenarea punctelor date
t.penup()
t.color('blue')
for i in range(len(x)):
    t.goto(x[i] + 1, y[i] + 1)
    t.dot(5, 'blue')

# Desenarea funcției liniare
t.penup()
t.color('red')
t.goto(x[0] + 1, y_lin[0] + 1)
t.pendown()
for i in range(len(x)):
    t.goto(x[i] + 1, y_lin[i] + 1)

# Desenarea funcției parabolice
t.penup()
t.color('green')
t.goto(x[0] + 1, y_par[0] + 1)
t.pendown()
for i in range(len(x)):
    t.goto(x[i] + 1, y_par[i] + 1)

# Adăugarea legendelor
t.penup()
t.goto(9, 13)
t.color('blue')
t.write('Punctele date', align='left')
t.goto(9, 12)
t.color('red')
t.write('Regresie liniară', align='left')
t.goto(9, 11)
t.color('green')
t.write('Regresie parabolică', align='left')

# Terminarea desenului
t.hideturtle()
turtle.done()
