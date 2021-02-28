import tkinter as tk
from tkinter import *
from CanvasPlus import CanvasPlus
import random
import time

main = tk.Tk()
main.title('Tetris')
canvas_width, canvas_height = (400, 800)
main.geometry('400x800')
win = CanvasPlus(main, width=canvas_width, height=canvas_height, bg='black')
# x = 40
# for i in range(10):
#     win.create_line(x, 0, x, 800, fill='gray', stipple='gray12')
#     x += 40
#     print(x)


class Shapes:
    def __init__(self, pos_x=180, pos_y=60, side=1):
        shapes = ('L', 'I', 'J', 'O', 'S', 'T', 'Z')  # tuple of shapes
        #self.name = shapes[random.randint(0, 6)]
        self.name = 'L'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.side = side

    def get_name(self):
        return self.name

    def draw(self, name):
        if name == 'L':
            tet1 = win.create_rectangle(self.pos_x-60, self.pos_y-20,
                                        self.pos_x+20, self.pos_y+20, fill='white', tag='L', outline="")
            tet2 = win.create_rectangle(self.pos_x+20, self.pos_y-60,
                                        self.pos_x+60, self.pos_y+20, fill='white', tag='L', outline="")
            win.to_polygon(tet1)
            win.to_polygon(tet2)
        elif name == 'I':
            self.pos_x = 200
            tet = win.create_rectangle(self.pos_x-80, self.pos_y-40,
                                       self.pos_x+80, self.pos_y, fill='white', tag='I', outline="")
            win.to_polygon(tet)
        elif name == 'J':
            tet1 = win.create_rectangle(self.pos_x-20, self.pos_y-20,
                                        self.pos_x+60, self.pos_y+20, fill='white', tag='J', outline="")
            tet2 = win.create_rectangle(self.pos_x-20, self.pos_y-60,
                                        self.pos_x-60, self.pos_y+20, fill='white', tag='J', outline="")
            win.to_polygon(tet1)
            win.to_polygon(tet2)
        elif name == 'O':
            self.pos_x = 200
            win.create_rectangle(self.pos_x-40, self.pos_y-40,
                                 self.pos_x+40, self.pos_y+40, fill='white', tag='O', outline="")
        elif name == 'S':
            tet1 = win.create_rectangle(self.pos_x - 60, self.pos_y - 20,
                                        self.pos_x + 20, self.pos_y + 20, fill='white', tag='S', outline="")
            tet2 = win.create_rectangle(self.pos_x - 20, self.pos_y - 60,
                                        self.pos_x + 60, self.pos_y - 20, fill='white', tag='S', outline="")
            win.to_polygon(tet1)
            win.to_polygon(tet2)
        elif name == 'T':
            tet1 = win.create_rectangle(self.pos_x - 60, self.pos_y - 20,
                                        self.pos_x + 60, self.pos_y + 20, fill='white', tag='T', outline="")
            tet2 = win.create_rectangle(self.pos_x - 20, self.pos_y - 60,
                                        self.pos_x + 20, self.pos_y + 20, fill='white', tag='T', outline="")
            win.to_polygon(tet1)
            win.to_polygon(tet2)
        elif name == 'Z':
            tet1 = win.create_rectangle(self.pos_x - 60, self.pos_y - 60,
                                        self.pos_x + 20, self.pos_y - 20, fill='white', tag='Z', outline="")
            tet2 = win.create_rectangle(self.pos_x - 20, self.pos_y - 20,
                                        self.pos_x + 60, self.pos_y + 20, fill='white', tag='Z', outline="")
            win.to_polygon(tet1)
            win.to_polygon(tet2)


def keypress(event):
    x = 0
    y = 0
    tetris = win.find_withtag(current_shape.get_name())
    if event.char == "a" and current_shape.pos_x > 80:
        x = -40
        current_shape.pos_x -= 40
    elif event.char == "d" and current_shape.pos_x < 320:
        x = 40
        current_shape.pos_x += 40
    elif event.char == "w":
        for i in tetris:  # go tru all elements of the shape
            win.rotate(i, current_shape.pos_x, current_shape.pos_y, 90, unit="d")
    elif event.char == "s" and current_shape.pos_y < 780:
        y = 40
        current_shape.pos_y += 40




    for i in tetris:
        win.move(i, x, y)


current_shape = Shapes()
current_shape.draw(current_shape.get_name())

main.bind("<Key>", keypress)
win.pack()
mainloop()
