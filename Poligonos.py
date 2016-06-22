import time
from tkinter import *
import turtle
tk=Tk()
canvas=Canvas(tk, width=500, height=500)
canvas.pack(expand=YES, fill=BOTH)
canvas.create_rectangle ((10, 10, 40, 40), fill="blue")
canvas.create_arc(10, 10, 70, 70, start=0, extent=90, fill="pink")
canvas.create_oval(10, 10, 50, 50, width=2, fill="purple")
def movefig1(event):
	if event.keysym=='Up':
		canvas.move(3,0,-3)
	elif event.keysym=='Down':
		canvas.move(1,0,3)
	elif event.keysym=='Left':
		canvas.move(2,-3,0)
	elif event.keysym=='Right':
		canvas.move(2,3,0)

canvas.bind_all('<KeyPress-Up>', movefig1)
canvas.bind_all('<KeyPress-Down>', movefig1)
canvas.bind_all('<KeyPress-Left>', movefig1)
canvas.bind_all('<KeyPress-Right>', movefig1)
tk.mainloop()