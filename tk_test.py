from collections import deque
import tkinter

BG_COLOR = "blue"
FG_COLOR = "red"

world_width = 600
world_height = 500
x = 250
y = 300
xmove = 10
ymove = 0
last_xmove = None
last_ymove = None
snake_len = 20
snake = deque([[x, y]])

def key(event):
    global xmove, ymove, last_xmove, last_ymove
    last_xmove = xmove
    last_ymove = ymove
    if event.keysym == 'd':
        xmove = 10
        ymove = 0
    elif event.keysym == 'a':
        xmove = -10
        ymove = 0
    elif event.keysym == 'w':
        xmove = 0
        ymove = -10
    elif event.keysym == 's':
        xmove = 0
        ymove = 10

def draw():
    global x, y, xmove, ymove
    if len(snake) == snake_len: # don't let the snake stretch longer than its length
        point = snake.popleft()
        C.create_line(point[0], point[1], point[0] + 10, point[1], fill=BG_COLOR, width=10)

    point = [x + xmove, y + ymove]
    if len(snake) > 1: # snakes dont move backwards
        if point == snake[-2]:
            xmove = last_xmove
            ymove = last_ymove
            point = [x + last_xmove, y + last_ymove]
        
    if point in snake: # snake ate itself and died
        quit()

    # flat earth snake dies if it reaches the edge
    if ( point[0] < 0 or point[0] > world_width
            or point[1] < 0 or point[1] > world_height):
        quit()

    x, y = point
    C.create_line(x, y, x + 10, y,fill=FG_COLOR, width=10)
    snake.append(point)
    top.after(16, draw)


top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=500, width=600)
C.pack()

top.bind_all('<Key>', key)
top.after(16, draw)
top.mainloop()
