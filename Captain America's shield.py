

#   Captain America Shield



from turtle import Turtle, Screen

def aylana(a, b):
	top = Turtle()
	top.shape('circle')
	top.shapesize(a)
	top.color(b)
	top.goto(0, 0)


def yulduz(a, size):
	global q
	yul = Turtle()
	yul.color('white')
	yul.penup()
	yul.goto(0, a)
	yul.hideturtle()
	yul.pensize(size)

	yul.right(72)
	yul.pendown()
	k=0

	for i in range(1,10):
		print(i)

	
		while True:
			yul.forward(1)
		
			x, y = yul.position()
			print(x, y)
			
			
			
			if x**2 + y**2 >= a**2:
				yul.right(72)
				break
				
			
				
			
			
		





def main():
	global q
	oyna = Screen()
	oyna.bgcolor('black')

	aylana(15, 'red')
	aylana(12, 'white')
	aylana(9, 'red')
	aylana(6, 'blue')


	#chiziq = Turtle()
	#chiziq.color('white')
	#chiziq.penup()
	
	#chiziq.pendown()
	a = 60
	q=0
	b=1
	size =1
	

	while True:
		q+=1
		print('q=', q)
		yulduz(a, size)
		if q==5:
			size = 3
			b=3
		if q==8:
			b=5

		a-=b
		if a==30:
			break

		

		


		#b = int(-(float(a)*math.cos(float(144)*math.pi/180)))
		#c = int(-(float(a)*math.sin(float(144)*math.pi/180)))

	aylana(20, 'blue')					
	oyna.mainloop()

main()	