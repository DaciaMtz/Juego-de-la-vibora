#TC001S.1 Actividad 2 Juego de la Víbora
"""Videojuego de la víbora con dos actualuzaciones: 
    * La comida puede moverse al azar un paso a la vez y no debe de salirse de la ventana
    * Cada vez que se corra el juego, la víbora y la comida tienen colores diferentes entre sí, 
      pero al azar, de una serie de 5 diferentes colores, excepto el rojo """

#Dacia Martínez Díaz A01733799
#Fernando Aguilar Acosta A00827677

from turtle import *
from random import randrange, shuffle
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, bodycolor)

    square(food.x, food.y, 9, foodcolor)
    update()
    ontimer(move, 100)

    #Hacer que la comida se mueve a cada paso de la serpiente
    #Se define una variable con rango al azar de 4 y asignamos un valor de 1 a otra variable para que entre a un while.
    var=randrange(4)
    verify=1
    #Ciclo while que mueve a la comida una posición alrededor aleatoriamente
    while (verify == 1):
        #Condición if para verificar que la variable esté en rango y asignar otro valor al azar
        if (var == 0):
            if (food.x <= 14*10):
                food.x=food.x+10
                verify=0
            else:
                var=randrange(4)
        #Condición if para verificar que la variable esté en rango y asignar otro valor al azar
        if (var == 1):
            if (food.y <= 14*10):
                food.y=food.y+10
                verify=0
            else:
                var=randrange(4)
        #Condición if para verificar que la variable esté en rango y asignar otro valor al azar
        if (var == 2):
            if (food.x >= -14*10):
                food.x=food.x-10
                verify=0
            else:
                var=randrange(4)
        #Condición if para verificar que la variable esté en rango y asignar otro valor al azar
        if (var == 3):
            if (food.y >= -14*10):
                food.y=food.y-10
                verify=0
            else:
                var=randrange(4)

#Función que escoge dos colores al azar, uno para la comida y otro para la víbora, de una lista de 5 colores.
def coloresrandom():
    colorlist = ["blue", "black", "green", "purple", "orange"]  #Lista de 5 colores diferentes
    shuffle(colorlist)  #Revuelve los elementos de la lista de colores en un orden al azar
    global bodycolor, foodcolor
    bodycolor = colorlist[0]  #Escoge el primer elemento de la nueva lista desordenada
    foodcolor = colorlist[1]  #Escoge el segundo elemento de la nueva lista desordenada

setup(420, 420, 370, 0)
hideturtle()
coloresrandom()
tracer(False)
listen()
#Comandos para que la víbora cambie de dirección
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()