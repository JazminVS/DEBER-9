from tkinter import *
tk=Tk()
tk.title('POLIGONOS EN MOVIMIENTO')
canvas=Canvas(tk, width=500, height=500,bg="orange")
canvas.pack(expand=YES, fill=BOTH)
canvas.create_rectangle((10, 10, 40, 40),width=2, fill="white")
canvas.create_arc(10, 10, 70, 70, start=0, extent=90, width=2,fill="pink")
canvas.create_oval(10, 10, 50, 50, width=2, fill="blue")
def movefig1(event):
	if event.keysym=='Up':
		canvas.move(1,0,-3)
		canvas.move(2,0,-3)
	elif event.keysym=='Down':
		canvas.move(1,0,3)
		canvas.move(3,0,3)
		canvas.move(2,0,3)
	elif event.keysym=='Left':
		canvas.move(1,-3,0)
		canvas.move(3,-3,0)
	elif event.keysym=='Right':
		canvas.move(1,3,0)
		canvas.move(2,3,0)
		canvas.move(3,3,0)

canvas.bind_all('<KeyPress-Up>', movefig1)
canvas.bind_all('<KeyPress-Down>', movefig1)
canvas.bind_all('<KeyPress-Left>', movefig1)
canvas.bind_all('<KeyPress-Right>', movefig1)
tk.mainloop()