#REALIZAR UNA ESTRELLA DE N LADOS IMPARES
a=int(input("INGRESE EL NUMERO DE PUNTAS DE SU ESTRELLA: "))
import turtle 

if(a<=4):
	print("LO SIENTO! NO ENTIENDO TU ORDEN >_<")
else:
	if (a%2!=0 ):
		t=turtle.Pen()
		ventana=turtle.Screen()
		ventana.bgcolor("orange")
		t.color(0,0,0)
		t.begin_fill()
		angulo=180/a
		for x in range(1,a+1):
			t.forward(-150)
			t.left(180-angulo)
		t.end_fill()
		turtle.getscreen()._root.mainloop()
	else:
		print("LO SIENTO! NO ENTIENDO TU ORDEN >_<")

