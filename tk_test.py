from collections import deque
import tkinter

x = 250
y = 300
xvect = 10
yvect = 0
last_xvect = None
last_yvect = None
line_len = 20
line = deque()

def key(event):
    global xvect, yvect, last_xvect, last_yvect
    last_xvect = xvect
    last_yvect = yvect
    if event.keysym == 'd':
        xvect = 10
        yvect = 0
    elif event.keysym == 'a':
        xvect = -10
        yvect = 0
    elif event.keysym == 'w':
        xvect = 0
        yvect = -10
    elif event.keysym == 's':
        xvect = 0
        yvect = 10

def draw():
    global x, y, xvect, yvect
    if len(line) == line_len:
        point = line.popleft()
        C.create_line(point[0], point[1], point[0] + 10, point[1], fill="blue", width=10)

    x += xvect
    y += yvect
    point = [x,y]
    if len(line) > 0:
        if point == line[-1]:
            x += last_xvect
            y += last_yvect
            xvect = last_xvect
            yvect = last_yvect
            point = [x,y]

    if point in line:
        quit()

    C.create_line(x, y, x + 10, y,fill="red", width=10)
    line.append(point)
    top.after(16, draw)


top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=500, width=600)
C.pack()

top.bind_all('<Key>', key)
top.after(16, draw)
top.mainloop()