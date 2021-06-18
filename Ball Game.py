

# Kichik animatsiya


import turtle 
from random import randint


def funk1():
	a,b = kv.position()
	if a+80 < 200:
		kv.goto(a+20, b)


def funk2():
	a, b = kv.position()
	if a-80 > -200:
		kv.goto(a-20, b)


def funk3():
	a,b = kv.position()
	if a+100 < 200:
		kv.goto(a+40, b)
	else:
		kv.goto(140, b)


def funk4():
	a,b = kv.position()
	if a-100 > -200:
		kv.goto(a-40, b)
	else:
		kv.goto(-140, b)		
	

def funk6():
	ranglar=['yellow','green', 'black', 'grey', 'orange', 'white', 'brown', 'pink', 'magenta']
	global ran1
	global ran2
	global ran3
	global ran4
	while True:
		ran0 = ranglar[randint(0,8)]
		ran1 = ranglar[randint(0,8)]
		ran2 = ranglar[randint(0,8)]
		ran3 = ranglar[randint(0,8)]
		ran4 = ranglar[randint(0,8)] 
		if ran3 != ran2 and ran4 != ran2 and ran0 != ran1:
			break
			
	main(ran0, ran1, ran2, ran3, ran4)

def funk7():
	global step_x, step_y
	step_x *= 1.1
	step_y *= 1.1
	print(step_x, step_y)





		
	
def funk8():

	global step_x, step_y
	step_x /= 1.1
	step_y /= 1.1
	print(step_x, step_y)
def funk9(txt, x, y):

	gap = turtle.Turtle()
	gap.penup()
	gap.speed(0)
	gap.hideturtle()
	gap.goto(x, y)
	gap.write(txt, font=10)





def main(rang0, rang1, rang2, rang3, rang4):
	global oyna
	global kv

	global step_x, step_y

	oyna = turtle.Screen()
	oyna.clear()
	oyna.setup(620,700)

	oyna.title('© 2020 . theRealHasanboy')
	oyna.bgcolor(rang0)


	ramka1 = turtle.Turtle()
	ramka1.shape('square')
	ramka1.penup()
	ramka1.speed(0)
	ramka1.shapesize(5,15.4)
	ramka1.goto(-145, 280)
	ramka1.color("white")
	
	funk9("""\" + \" va \" - \"    ->  Change speed""", -295, 300)
	funk9("""\" O \"    ->  Change color or restart """, -295, 250)



	ramka1 = turtle.Turtle()
	ramka1.shape('square')
	ramka1.shapesize(21)
	ramka1.color(rang1)

	chiziq=turtle.Turtle()
	chiziq.shape('square')
	chiziq.shapesize(20)
	chiziq.color(rang2)


	
	#chiziq.hideturtle()


	#chiziq.up()
	#chiziq.goto(200, 200)
	#chiziq.down()
	#chiziq.goto(200, -200)
	#chiziq.goto(-200, -200)
	#chiziq.goto(-200, 200)
	#chiziq.goto(200, 200)

	#chiziq2 = Turtle()

	#chiziq2.color('green')
	#chiziq2.pensize(8)
	#chiziq2.hideturtle()


	#chiziq2.up()
	#chiziq2.goto(-170, -200)
	#chiziq2.down()
	#chiziq2.goto(-170, -170)
	#chiziq2.goto(-50, -170)
	#chiziq2.goto(-50, -200)
	#chiziq2.goto(-170, -200)



	kv = turtle.Turtle()
	kv.shape('square')
	kv.shapesize(1,6)
	kv.penup()
	kv.speed(0)
	kv.color(rang3)
	kv.goto(0, -190)
	#kv.goto(0,0)
	#kv.shearfactor(-0.5)
	#kv.shapetransform()
	#(4.0, -1.0, -0.0, 2.0)


	koptok = turtle.Turtle()


	koptok.shape('circle')
	koptok.shapesize(1.5)
	koptok.penup()
	koptok.pensize(7)
	koptok.color(rang4)

	#koptok.down()


	koptok.goto(0, 0)

	#oyna.onkey(funk1, "Right")
	#oyna.onkey(funk2, "Left")
	#oyna.listen()

	step_x=3
	step_y=2

	#x=0
	#y=0
	while True:

		#x+=step_x
		#y+=step_y
		#koptok.goto(x, y)
		#koptok.penup()
		
		oyna.onkey(funk3, "Right")
		oyna.onkey(funk4, "Left")
		oyna.onkey(funk1, "a")
		oyna.onkey(funk2, "d")
		oyna.onkey(funk6, "o")
		oyna.onkey(funk7, "+")
		oyna.onkey(funk8, "-")
		oyna.listen()
		
		a, b = kv.position()


		x, y=koptok.position()
		if x >= 200 or x <= -200:
			step_x = -step_x
		if y >= 200: # or y <= -200:
			step_y = -step_y
		if x <= a+60 and x >= a-60 and y <= -170:
			step_y = -step_y
		if y <= -200:
			break


		koptok.goto(x+step_x, y+step_y)

	
	oyna.listen()	
	oyna.mainloop()











main('green', 'yellow', 'red', 'black', 'blue')
