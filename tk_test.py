import tkinter

time1 = None
x = 250
y = 300
xvect = 10
yvect = 0

def key(event):
    global xvect, yvect
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
    x += xvect
    y += yvect
    C.create_line(x, y, x + 10, y,fill="red", width=10)
    top.after(16, draw)


top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=500, width=600)
C.pack()

top.bind_all('<Key>', key)
top.after(16, draw)
top.mainloop()
