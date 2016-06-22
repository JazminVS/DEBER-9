#REALIZAR UNA ESTRELLA DE N LADOS IMPARES
a=int(input("INGRESE EL NUMERO DE PUNTAS DE SU ESTRELLA: "))
import turtle 
t=turtle.Pen()

#if(a==0 or a==1 or a==2 or a==3 or a==4):
	#print("LO SIENTO! NO ENTIENDO TU ORDEN >_<")
if (a%2 !=0):
	angulo=180/a
	for x in range(1,a+1):
		t.forward(-100)
		t.left(180-angulo)
	turtle.getscreen()._root.mainloop()
else:
	print("LO SIENTO! NO ENTIENDO TU ORDEN >_<")