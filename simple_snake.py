from collections import deque
import tkinter

BG_COLOR = "blue"
FG_COLOR = "red"

world_width = 60
world_height = 50
x = int(world_width / 2)
y = int(world_height / 2)
xmove = 1
ymove = 0
last_xmove = None
last_ymove = None
snake_len = 20
snake = deque([(x, y)])
point = snake[-1]
draw_count = 0
snakebday = 60 * 5 # ~5 seconds 
collision_list = [ [ False for w in range(world_width) ] for h in range(world_height) ]
collision_list[x][y] = True

def key(event):
    global xmove, ymove, last_xmove, last_ymove
    last_xmove = xmove
    last_ymove = ymove
    if event.keysym == 'd':
        xmove = 1
        ymove = 0
    elif event.keysym == 'a':
        xmove = -1
        ymove = 0
    elif event.keysym == 'w':
        xmove = 0
        ymove = -1
    elif event.keysym == 's':
        xmove = 0
        ymove = 1

def draw():
    global x, y, xmove, ymove, draw_count, snake_len
    global last_xmove, last_ymove, collision_list
    draw_count += 1
    if draw_count > snakebday: # snakes birthday grow by a segment
        snake_len += 1
        draw_count = 0

    if len(snake) == snake_len: # don't let the snake stretch longer than its length
        point = snake.popleft()
        C.create_line(point[0] * 10, point[1] * 10, point[0] + 10, point[1] * 10, fill=BG_COLOR, width=10)
        collision_list[point[0]][point[1]] = False

    point = (x + xmove, y + ymove)
    if len(snake) > 1: # snakes dont move backwards
        if point == snake[-2]:
            xmove = last_xmove
            ymove = last_ymove
            point = (x + last_xmove, y + last_ymove)
        
    if collision_list[point[1]][point[0]]: # snake ate itself and died
        quit()

    # flat earth snake dies if it reaches the edge
    if ( point[0] < 0 or point[0] > world_width
            or point[1] < 0 or point[1] > world_height):
        quit()
    print(point)
    x, y = point
    C.create_line(x * 10,  y * 10, x * 10 + 10, y * 10, fill=FG_COLOR, width=10)
    snake.append(point)
    collision_list[x][y] = True
    top.after(16, draw)


top = tkinter.Tk()

C = tkinter.Canvas(top, bg=BG_COLOR, height=world_height * 10, width=world_width * 10)
C.pack()


top.bind_all('<Key>', key)
top.after(16, draw)
top.mainloop()
