from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0) #Crea vector de food
snake = [vector(10, 0)] #Crea vector de snake
aim = vector(0, -10) #Crea vector de aim

colorfood = randrange(1,6)
colorsnake = randrange(1,6)

while colorfood == colorsnake:
    colorfood = randrange(1,6)
    
def SetColor(num):
    if num == 1:
        color = 'blue'
    elif num == 2:
        color = 'purple'
    elif num == 3:
        color = 'orange'
    elif num == 3:
        color = 'green'
    elif num == 4:
        color = 'pink'
    elif num == 5:
        color = 'black'
    return color

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190 #Límites de la ventana

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake: #Si la cabeza toca el cuerpo de la serpiente o toca los bordes de la ventana acaba el juego
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake)) #Muestra el tamaño actual de la serpiente
        food.x = randrange(-15, 15) * 10 #Da un valor de x random de -15 a 15 para la posición de la comida
        food.y = randrange(-15, 15) * 10 #Da un valor de y random de -15 a 15 para la posición de la comida
    else:
        snake.pop(0)

    clear()

    for body in snake:
       square(body.x, body.y, 9, SetColor(colorsnake))

    square(food.x, food.y, 9, SetColor(colorfood))
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle() #Esconde el cursor de turtle
tracer(False)
listen() #Escucha el input del teclado
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()