"""
This is a calculator written in Python! Using various methods and ways it can solve numerous things in each of it's 3 modes. The first one, algebraic mode, solves standard equations, as well as equalities and inequalities to the first degree (as long as x is a whole number.) The second mode, geometric calculator, uses user-input and solves 2D shapes, such as circle, triangles and polygons. The last mode, graphing calculator, graphs points, slopes and the distance between two points. Along with all of these it has a dark and light mode. I used previous knowledge, as well as new information, methods and functions I learned while working on this project.
Sources used:
https://docs.python.org/3/library/turtle.html
https://docs.python.org/3/library/math.html
https://docs.python.org/3/
"""

import math
import turtle
import sys

#defining all values needed to be pre-defined
calc_start = True #while this value is true, the calculator will continuously loop
path = "undefined" #sets first path value to undefined
prev_path = "1" #sets the value of the previous path to 1, as no other path has been specified
background_foreground_color = ["white", "black"] #sets the default background and foreground colors for the turtle
ans = "1" #sets the default value for the ans variable to '1'

#defining things needed for turtle
t = turtle.Turtle()
tt = turtle.Turtle()
w = turtle.Screen()
t.speed(0) #speeds up turtle drawing speed
t.hideturtle() #hides turtle on screen
tt.speed(0) #speeds up turtle drawing speed
tt.hideturtle() #hides turtle on screen
w.setup(500,500) #sets turtle screen to a size of 500x500 pixels
turtle.title("Python Graphic Calculator") #renames the title of the turtle screen

#defining turtle screens as functions
def title_for_mode(titleofmode, bgfgcolor):
	tt.clear() #clears all previous drawings by turtle
	w.tracer(False) #turns off turtle animation, runs following drawings without screen updates
	w.bgcolor(bgfgcolor[0])
	tt.color(bgfgcolor[1])
	tt.pu()
	tt.setpos(-250,225)
	tt.pd()
	tt.fd(5)
	tt.write(titleofmode, move = False, align = "left", font = ("Arial", 20, "normal"))
	tt.fd(495)
	tt.pu()
	tt.setpos(0,0)
	w.update() #manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #returns the screen animations to the standard state
	tt.hideturtle()

def main_menu_algebraic_icon(bgfgcolor):
	t.color(bgfgcolor[1])
	t.pensize(10)
	t.pu()
	t.fd(10)
	t.pd()
	t.fd(20)
	t.bk(40)
	t.fd(20)
	t.left(90)
	t.fd(20)
	t.bk(40)
	t.fd(20)
	t.right(90)
	t.pu()
	t.fd(40)
	t.left(90)
	t.right(90)
	t.pd()
	t.fd(40)
	t.bk(20)
	t.pu()
	t.right(90)
	t.fd(30)
	t.left(90)
	t.pd()
	t.circle(1)
	t.pu()
	t.right(90)
	t.fd(20)
	t.left(90)
	t.pd()
	t.fd(20)
	t.bk(40)
	t.fd(20)
	t.pu()
	t.right(90)
	t.fd(20)
	t.left(90)
	t.pd()
	t.circle(1)
	t.pu()
	t.left(90)
	t.fd(20)
	t.left(90)
	t.fd(60)
	t.left(180)
	t.left(45)
	t.pd()
	t.fd(25)
	t.bk(50)
	t.fd(25)
	t.left(90)
	t.fd(25)
	t.bk(50)
	t.fd(25)
	t.right(135)
	t.pu()

def main_menu_geometric_icon(bgfgcolor):
	t.pd()
	color_for_geometric_icon = ("red","green","orange","violet") #defines colors for geometric colors
	radius = 55
	for i in range(4,0,-1):
		t.color(color_for_geometric_icon[i-1])
		t.begin_fill()
		t.circle(radius,360,i+3)
		t.end_fill()
		radius = radius - 5
	t.pu()

def main_menu_graphing_icon(bgfgcolor):
	t.pd()
	t.color(bgfgcolor[1])
	t.pensize(5)
	for i in range(4):
		t.fd(70)
		t.left(140)
		t.fd(12)
		t.bk(12)
		t.left(80)
		t.fd(12)
		t.bk(12)
		t.left(140)
		t.bk(70)
		t.right(90)
	t.pu()
	t.bk(70)
	t.right(90)
	t.fd(40)
	t.left(135)
	t.pd()
	t.pensize(3)
	t.color("red")
	t.left(180)
	t.left(140)
	t.fd(12)
	t.bk(12)
	t.left(80)
	t.fd(12)
	t.bk(12)
	t.left(140)
	t.left(180)
	t.fd(150)
	t.left(140)
	t.fd(12)
	t.bk(12)
	t.left(80)
	t.fd(12)
	t.bk(12)
	t.left(140)
	t.pu()
	t.setheading(0)

def main_menu_settings_icon(bgfgcolor):
	t.color(bgfgcolor[1])
	t.right(90)
	t.fd(25)
	t.left(90)
	t.pd()
	t.begin_fill()
	for i in range(8):
		t.circle(45,22.5)
		t.right(90)
		t.fd(15)
		t.left(90)
		t.circle(60,22.5)
		t.left(90)
		t.fd(15)
		t.right(90)
	t.end_fill()
	t.left(90)
	t.fd(25)
	t.right(90)
	t.color(bgfgcolor[0])
	t.begin_fill()
	t.circle(20)
	t.end_fill()
	t.setheading(0)
	t.pu()

def main_menu_screen(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.pu()
	t.setpos(0,180)
	t.write("Choose your path with the corresponding number: ", move = False, align = "center", font = ("Arial", 21, "normal"))
	t.setpos(-160,140)
	t.pd()
	main_menu_algebraic_icon(bgfgcolor)
	t.pu()
	t.setpos(-125,20)
	t.pd()
	t.write("[1] Algebraic Calculator", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.pu()
	t.setpos(110,50)
	t.pd()
	main_menu_geometric_icon(bgfgcolor)
	t.pu()
	t.setpos(115,20)
	t.color(bgfgcolor[1])
	t.write("[2] Geometric Calculator", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.setpos(-120,-100)
	t.pd()
	main_menu_graphing_icon(bgfgcolor)
	t.pu()
	t.setpos(-120,-200)
	t.color(bgfgcolor[1])
	t.write("[3] Graphing Calculator", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.setpos(125,-110)
	t.pd()
	main_menu_settings_icon(bgfgcolor)
	t.pu()
	t.setpos(110,-200)
	t.color(bgfgcolor[1])
	t.write("[4] Color Settings", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.setpos(0,-235)
	t.write("(Input [9] for how to navigate program)", move = False, align = "center", font = ("Arial", 14, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def algebraic_input_screen(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(-40,175)
	t.pd()
	main_menu_algebraic_icon(background_foreground_color)
	t.pu()
	t.setpos(0,25)
	t.pd()
	t.write("Enter an equation: ", move = False, align = "center", font = ("Arial", 40, "normal"))
	t.pu()
	t.setpos(0,-65)
	t.pd()
	t.write("This calculator can solve for x in\nequalities and inequalities,\nas well as doing normal calculations.", move = False, align = "center", font = ("Arial", 22, "normal"))
	t.pu()
	t.setpos(0,-220)
	t.pd()
	t.write("Use 'V' followed by a number in parantheses to get the square root of value in parantheses.\nUse '^' followed by a number to find a value to the power of the second number.\nUse 'ans' to use the answer of previous equation in the current equation.\nUse 'pi' for the exact value of pi.\n\nWhen solving inequalities, put '<' or '>' before '=' to avoid syntax errors.\nAny errors will be printed to terminal.\nThis calculator can only solve for x as a whole number in the first degree.\nThis calculator can only solve equations with one variable.\nThis variable must be 'x'.", move = False, align = "center", font = ("Arial", 12, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state 

def algebraic_answer_screen(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle 
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(-40,175)
	t.pd()
	main_menu_algebraic_icon(background_foreground_color)
	t.pu()
	t.setpos(0,40)
	t.pd()
	t.write("Type Of Equation: " + type_of_algebraic_equation, move = False, align = "center", font = ("Arial", 26, "normal"))
	t.pu()
	t.setpos(0,-75)
	t.pd()
	t.write(algebraic_equation + "\n" + ans_on_screen, move = False, align = "center", font = ("Arial", 40, "normal"))
	t.pu()
	t.setpos(0,-175)
	t.pd()
	t.write("Enter another equation:\n(Re-enter mode to see rules or\nreturn to calculator menu with 'back')", move = False, align = "center", font = ("Arial", 26, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def geometric_menu_screen(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(0,95)
	t.pd()
	main_menu_geometric_icon(background_foreground_color)
	t.pu()
	t.color(bgfgcolor[1])
	t.setpos(0,60)
	t.pd()
	t.write("Choose your path with the corresponding number: ", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.pu()
	t.setpos(-150,-50)
	t.pd()
	t.begin_fill()
	t.color("red")
	t.circle(50)
	t.end_fill()
	t.pu()
	t.setpos(-150,-80)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("[1] Circle Solver", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.pu()
	t.setpos(140,-50)
	t.bk(50)
	t.pd()
	t.color("green")
	t.begin_fill()
	for i in range(3):
		t.fd(100)
		t.left(120)
	t.end_fill()
	t.pu()
	t.setpos(140,-80)
	t.color(bgfgcolor[1])
	t.write("[2] Triangle Solver", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.pu()
	t.setpos(0,-200)
	t.left(90)
	t.fd(50)
	t.left(90)
	t.forward(50)
	t.left(180)
	t.pd()
	t.color("magenta")
	t.begin_fill()
	for i in range(4):
		t.fd(45)
		t.left(90)
	t.end_fill()
	t.pu()
	t.fd(65)
	t.pd()
	t.begin_fill()
	for i in range(5):
		t.forward(35)
		t.left(72)
	t.end_fill()
	t.pu()
	t.setpos(0,-210)
	t.bk(14)
	t.pd()
	t.begin_fill()
	for i in range(6):
		t.forward(28)
		t.left(60)
	t.end_fill()
	t.pu()
	t.setpos(0,-235)
	t.color(bgfgcolor[1])
	t.write("[3] Regular Polygon Solver", move = False, align = "center", font = ("Arial", 18, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def geometric_circle_input_screen(bgfgcolor):
	if bgfgcolor[0] == "black":
		circle_fill_color = "grey"
		perimeter_color = "white"
	elif bgfgcolor[0] == "white":
		circle_fill_color = "light grey"
		perimeter_color = "black"
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(0,210)
	t.left(180)
	t.pd()
	t.pensize(5)
	t.pu()
	t.color(circle_fill_color)
	t.begin_fill()
	t.circle(100)
	t.end_fill()
	t.pd()
	t.color(bgfgcolor[1])
	t.circle(100,270)
	t.color("red")
	t.circle(100,60)
	t.pu()
	t.pd()
	t.color(bgfgcolor[1])
	t.circle(100,30)
	t.circle(100,270)
	t.pd()
	t.color("green")
	t.left(90)
	t.forward(200)
	t.color("magenta")
	t.pu()
	t.bk(100)
	t.pd()
	t.right(120)
	t.forward(100)
	t.pu()
	t.left(90)
	t.circle(100,270)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.color("orange")
	t.circle(30,30)
	t.pd()
	t.circle(30,60)
	t.pu()
	t.color(bgfgcolor[1])
	t.setpos(0,-100)
	t.setheading(0)
	t.pensize(1)
	t.pd()
	t.write("[1] Radius (pink).\n[2] Circumference (" + perimeter_color + ").\n[3] Area (grey).\n[4] Arc (red) + Angle Measure Of The Arc (orange).\n[5] Arc (red) + Measure Of The Arc (red)", move = False, align = "center", font = ("Arial", 16, "normal"))
	t.pu()
	t.setpos(0,-175)
	t.write("Choose your path with the corresponding\nnumber depending on which values you have: ", move = False, align = "center", font = ("Arial", 20, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def geometric_circle_input_type_screen(bgfgcolor, circleinputchoice):
	if bgfgcolor[0] == "black":
			circle_fill_color = "grey"
			perimeter_color = "white"
	elif bgfgcolor[0] == "white":
			circle_fill_color = "light grey"
			perimeter_color = "black"
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(0,210)
	t.left(180)
	t.pd()
	t.pensize(5)
	t.pu()
	t.color(circle_fill_color)
	t.begin_fill()
	t.circle(100)
	t.end_fill()
	t.pd()
	t.color(bgfgcolor[1])
	t.circle(100,270)
	t.color("red")
	t.circle(100,60)
	t.pu()
	t.pd()
	t.color(bgfgcolor[1])
	t.circle(100,30)
	t.circle(100,270)
	t.pd()
	t.color("green")
	t.left(90)
	t.forward(200)
	t.color("magenta")
	t.pu()
	t.bk(100)
	t.pd()
	t.right(120)
	t.forward(100)
	t.pu()
	t.left(90)
	t.circle(100,270)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.color("orange")
	t.circle(30,30)
	t.pd()
	t.circle(30,60)
	t.pu()
	t.color(bgfgcolor[1])
	t.setpos(0,-50)
	t.setheading(0)
	t.pensize(1)
	t.write("Enter the value of the " + str(circleinputchoice) + ": ", move = False, align = "center", font = ("Arial", 26, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def geometric_circle_answer_screen(bgfgcolor, cradius, ccircumference, carea):
	if bgfgcolor[0] == "black":
		circle_fill_color = "grey"
		perimeter_color = "white"
	elif bgfgcolor[0] == "white":
		circle_fill_color = "light grey"
		perimeter_color = "black"
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(0,210)
	t.left(180)
	t.pd()
	t.pensize(5)
	t.pu()
	t.color(circle_fill_color)
	t.begin_fill()
	t.circle(100)
	t.end_fill()
	t.pd()
	t.color(bgfgcolor[1])
	t.circle(100,270)
	t.color("red")
	t.circle(100,60)
	t.pu()
	t.pd()
	t.color(bgfgcolor[1])
	t.circle(100,30)
	t.circle(100,270)
	t.pd()
	t.color("green")
	t.left(90)
	t.forward(200)
	t.color("magenta")
	t.pu()
	t.bk(100)
	t.pd()
	t.right(120)
	t.forward(100)
	t.pu()
	t.left(90)
	t.circle(100,270)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.color("orange")
	t.circle(30,30)
	t.pd()
	t.circle(30,60)
	t.pu()
	t.color(bgfgcolor[1])
	t.setpos(0,-55)
	t.setheading(0)
	t.pensize(1)
	t.pd()
	t.write("Radius (pink) = " + str(cradius) + "\nCircumference (" + perimeter_color + ") = " + str(ccircumference) + "\nArea (grey) = " + str(carea), move = False, align = "center", font = ("Arial", 16, "normal"))
	t.pu()
	t.setpos(0,-225)
	t.pd()
	t.write("[1] Radius (pink).\n[2] Circumference (" + perimeter_color + ").\n[3] Area (grey).\n[4] Arc (red) + Angle Measure Of The Arc (orange).\n[5] Arc (red) + Measure Of The Arc (red)", move = False, align = "center", font = ("Arial", 16, "normal"))
	t.pu()
	t.setpos(0,-128)
	t.write("To solve another circle enter the number\ncorresponding to the value you have:\n(Or return to geometric menu with 'back')", move = False, align = "center", font = ("Arial", 20, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def geometric_triangle_path_screen(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pensize(5)
	t.pu()
	t.setpos(-120,62.5)
	t.pd()
	t.color("red")
	t.forward(120)
	t.right(90)
	t.pu()
	t.forward(30)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("side b", move = False, align = "center", font = ("Arial", 20, "normal"))
	t.pu()
	t.color("red")
	t.backward(30)
	t.left(90)
	t.pd()
	t.forward(120)
	t.left(150)
	t.color("green")
	t.forward(138.6)
	t.pu()
	t.right(90)
	t.fd(15)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("side c", move = False, align = "center", font = ("Arial", 20, "normal"))
	t.pu()
	t.color("green")
	t.bk(15)
	t.left(90)
	t.pd()
	t.forward(138.6)
	t.left(120)
	t.color("orange")
	t.forward(69.3)
	t.pu()
	t.right(90)
	t.fd(30)
	t.left(90)
	t.fd(10)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("side a", move = False, align = "center", font = ("Arial", 20, "normal"))
	t.color("orange")
	t.pu()
	t.bk(10)
	t.right(90)
	t.bk(30)
	t.left(90)
	t.pd()
	t.fd(69.3)
	t.left(90)
	t.pu()
	t.fd(240)
	t.left(150)
	t.fd(60)
	t.left(90)
	t.pd()
	t.circle(60,15)
	t.pu()
	t.right(90)
	t.fd(35)
	t.left(90)
	t.fd(18)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("angle a", move = False, align = "center", font = ("Arial", 20, "normal"))
	t.pu()
	t.color("orange")
	t.bk(18)
	t.right(90)
	t.bk(35)
	t.left(90)
	t.pd()
	t.circle(60,15)
	t.pu()
	t.circle(60,330)
	t.right(90)
	t.forward(217.2)
	t.left(120)
	t.fd(50)
	t.pd()
	t.left(90)
	t.color("red")
	t.pd()
	t.circle(50,30)
	t.right(90)
	t.pu()
	t.fd(40)
	t.left(90)
	t.fd(5)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("angle b", move = False, align = "center", font = ("Arial", 20, "normal"))
	t.pu()
	t.color("red")
	t.bk(5)
	t.right(90)
	t.bk(40)
	t.left(90)
	t.pd()
	t.circle(50,30)
	t.pu()
	t.circle(50,300)
	t.right(90)
	t.fd(88.6)
	t.left(90)
	t.fd(35)
	t.left(90)
	t.pd()
	t.color("green")
	t.circle(35,45)
	t.right(135)
	t.pu()
	t.fd(35)
	t.color(bgfgcolor[1])
	t.write("angle c", move = False, align = "center", font = ("Arial", 20, "normal"))
	t.bk(35)
	t.color("green")
	t.left(135)
	t.pd()
	t.circle(35,45)
	t.pu()
	t.color(bgfgcolor[1])
	t.setpos(0,0)
	t.write("Choose your path depending on which values you have:", move = False, align = "center", font = ("Arial", 18, "normal"))
	t.setpos(-125,-110)
	t.pd()
	t.pensize(1)
	t.write("[1] Law Of Sines:\nTwo Sides, One Angle Opposite\n(Example: Side A, Side B, Angle A)\nor\nTwo Angles, One Side Opposite\n(Example: Angle A, Angle B, Side B)", move = False, align = "center", font = ("Arial", 14, "normal"))
	t.pu()
	t.setpos(125,-110)
	t.pd()
	t.write("[2] Law Of Cosines:\nTwo Sides, One Angle Inbetween\n(Example: Side A, Side B, Angle C)\nor\nThree Side Lengths\n(Example: Side A, Side B, Side C)", move = False, align = "center", font = ("Arial", 14, "normal"))
	t.pu()
	t.setpos(0,-225)
	t.pd()
	t.write("[3] Pythagorean Theorem:\nTwo Sides, Both Non-Hypotenuse\n(Example: Side A, Side B)\nor\nOne Side Length, One Hypotenuse Length\n(Example: Side A or Side B, Side C)", move = False, align = "center", font = ("Arial", 14, "normal"))
	t.setheading(0)
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def geometric_triangle_pathinpath_screen(bgfgcolor, currenttrianglepath, triangle_option_1, triangle_option_2):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.color(bgfgcolor[1])
		t.pensize(5)
		t.pu()
		t.setpos(-120,62.5)
		t.pd()
		t.color("red")
		t.forward(120)
		t.right(90)
		t.pu()
		t.forward(30)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side b", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("red")
		t.backward(30)
		t.left(90)
		t.pd()
		t.forward(120)
		t.left(150)
		t.color("green")
		t.forward(138.6)
		t.pu()
		t.right(90)
		t.fd(15)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side c", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("green")
		t.bk(15)
		t.left(90)
		t.pd()
		t.forward(138.6)
		t.left(120)
		t.color("orange")
		t.forward(69.3)
		t.pu()
		t.right(90)
		t.fd(30)
		t.left(90)
		t.fd(10)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side a", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.color("orange")
		t.pu()
		t.bk(10)
		t.right(90)
		t.bk(30)
		t.left(90)
		t.pd()
		t.fd(69.3)
		t.left(90)
		t.pu()
		t.fd(240)
		t.left(150)
		t.fd(60)
		t.left(90)
		t.pd()
		t.circle(60,15)
		t.pu()
		t.right(90)
		t.fd(35)
		t.left(90)
		t.fd(18)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("angle a", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("orange")
		t.bk(18)
		t.right(90)
		t.bk(35)
		t.left(90)
		t.pd()
		t.circle(60,15)
		t.pu()
		t.circle(60,330)
		t.right(90)
		t.forward(217.2)
		t.left(120)
		t.fd(50)
		t.pd()
		t.left(90)
		t.color("red")
		t.pd()
		t.circle(50,30)
		t.right(90)
		t.pu()
		t.fd(40)
		t.left(90)
		t.fd(5)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("angle b", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("red")
		t.bk(5)
		t.right(90)
		t.bk(40)
		t.left(90)
		t.pd()
		t.circle(50,30)
		t.pu()
		t.circle(50,300)
		t.right(90)
		t.fd(88.6)
		t.left(90)
		t.fd(35)
		t.left(90)
		t.pd()
		t.color("green")
		t.circle(35,45)
		t.right(135)
		t.pu()
		t.fd(35)
		t.color(bgfgcolor[1])
		t.write("angle c", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.bk(35)
		t.color("green")
		t.left(135)
		t.pd()
		t.circle(35,45)
		t.pu()
		t.color(bgfgcolor[1])
		t.setpos(0,-25)
		t.write("Triangle Solving Using " + str(currenttrianglepath) + ";\nChoose your path with the values you have:", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.setpos(0,-100)
		t.pd()
		t.pensize(1)
		t.write(triangle_option_1, move = False, align = "center", font = ("Arial", 18, "normal"))
		t.pu()
		t.setpos(0,-175)
		t.pd()
		t.write(triangle_option_2, move = False, align = "center", font = ("Arial", 18, "normal"))
		t.pu()
		t.setheading(0)
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates

def geometric_triangle_input_screen(bgfgcolor, currenttrianglepath, triangle_option_1):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.color(bgfgcolor[1])
		t.pensize(5)
		t.pu()
		t.setpos(-120,62.5)
		t.pd()
		t.color("red")
		t.forward(120)
		t.right(90)
		t.pu()
		t.forward(30)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side b", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("red")
		t.backward(30)
		t.left(90)
		t.pd()
		t.forward(120)
		t.left(150)
		t.color("green")
		t.forward(138.6)
		t.pu()
		t.right(90)
		t.fd(15)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side c", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("green")
		t.bk(15)
		t.left(90)
		t.pd()
		t.forward(138.6)
		t.left(120)
		t.color("orange")
		t.forward(69.3)
		t.pu()
		t.right(90)
		t.fd(30)
		t.left(90)
		t.fd(10)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side a", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.color("orange")
		t.pu()
		t.bk(10)
		t.right(90)
		t.bk(30)
		t.left(90)
		t.pd()
		t.fd(69.3)
		t.left(90)
		t.pu()
		t.fd(240)
		t.left(150)
		t.fd(60)
		t.left(90)
		t.pd()
		t.circle(60,15)
		t.pu()
		t.right(90)
		t.fd(35)
		t.left(90)
		t.fd(18)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("angle a", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("orange")
		t.bk(18)
		t.right(90)
		t.bk(35)
		t.left(90)
		t.pd()
		t.circle(60,15)
		t.pu()
		t.circle(60,330)
		t.right(90)
		t.forward(217.2)
		t.left(120)
		t.fd(50)
		t.pd()
		t.left(90)
		t.color("red")
		t.pd()
		t.circle(50,30)
		t.right(90)
		t.pu()
		t.fd(40)
		t.left(90)
		t.fd(5)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("angle b", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("red")
		t.bk(5)
		t.right(90)
		t.bk(40)
		t.left(90)
		t.pd()
		t.circle(50,30)
		t.pu()
		t.circle(50,300)
		t.right(90)
		t.fd(88.6)
		t.left(90)
		t.fd(35)
		t.left(90)
		t.pd()
		t.color("green")
		t.circle(35,45)
		t.right(135)
		t.pu()
		t.fd(35)
		t.color(bgfgcolor[1])
		t.write("angle c", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.bk(35)
		t.color("green")
		t.left(135)
		t.pd()
		t.circle(35,45)
		t.pu()
		t.setheading(0)
		t.color(bgfgcolor[1])
		t.setpos(0,-25)
		t.write("Triangle Solving Using " + str(currenttrianglepath) + ";", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.setpos(0,-125)
		t.pd()
		t.pensize(1)
		t.write(current_triangle_path_option1, move = False, align = "center", font = ("Arial", 24, "normal"))
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state

def geometric_triangle_answer_screen(bgfgcolor, tri_sid_a, tri_sid_b, tri_sid_c, tri_ang_a, tri_ang_b, tri_ang_c):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.color(bgfgcolor[1])
		t.pensize(5)
		t.pu()
		t.setpos(-120,62.5)
		t.pd()
		t.color("red")
		t.forward(120)
		t.right(90)
		t.pu()
		t.forward(30)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side b", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("red")
		t.backward(30)
		t.left(90)
		t.pd()
		t.forward(120)
		t.left(150)
		t.color("green")
		t.forward(138.6)
		t.pu()
		t.right(90)
		t.fd(15)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side c", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("green")
		t.bk(15)
		t.left(90)
		t.pd()
		t.forward(138.6)
		t.left(120)
		t.color("orange")
		t.forward(69.3)
		t.pu()
		t.right(90)
		t.fd(30)
		t.left(90)
		t.fd(10)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("side a", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.color("orange")
		t.pu()
		t.bk(10)
		t.right(90)
		t.bk(30)
		t.left(90)
		t.pd()
		t.fd(69.3)
		t.left(90)
		t.pu()
		t.fd(240)
		t.left(150)
		t.fd(60)
		t.left(90)
		t.pd()
		t.circle(60,15)
		t.pu()
		t.right(90)
		t.fd(35)
		t.left(90)
		t.fd(18)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("angle a", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("orange")
		t.bk(18)
		t.right(90)
		t.bk(35)
		t.left(90)
		t.pd()
		t.circle(60,15)
		t.pu()
		t.circle(60,330)
		t.right(90)
		t.forward(217.2)
		t.left(120)
		t.fd(50)
		t.pd()
		t.left(90)
		t.color("red")
		t.pd()
		t.circle(50,30)
		t.right(90)
		t.pu()
		t.fd(40)
		t.left(90)
		t.fd(5)
		t.pd()
		t.color(bgfgcolor[1])
		t.write("angle b", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.pu()
		t.color("red")
		t.bk(5)
		t.right(90)
		t.bk(40)
		t.left(90)
		t.pd()
		t.circle(50,30)
		t.pu()
		t.circle(50,300)
		t.right(90)
		t.fd(88.6)
		t.left(90)
		t.fd(35)
		t.left(90)
		t.pd()
		t.color("green")
		t.circle(35,45)
		t.right(135)
		t.pu()
		t.fd(35)
		t.color(bgfgcolor[1])
		t.write("angle c", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.bk(35)
		t.color("green")
		t.left(135)
		t.pd()
		t.circle(35,45)
		t.pu()

		t.color(bgfgcolor[1])
		t.setpos(-125,-75)
		t.write("side a =" + str(tri_sid_a) + "\nside b =" + str(tri_sid_b) + "\nside c =" + str(tri_sid_c), move = False, align = "center", font = ("Arial", 20, "normal"))
		t.setpos(125,-75)
		t.write("angle a =" + str(tri_ang_a) + "\nangle b =" + str(tri_ang_b) + "\nangle c =" + str(tri_ang_c), move = False, align = "center", font = ("Arial", 20, "normal"))
		t.setpos(0,-175)
		t.write("To solve another triangle, choose a path:\n[1]Law Of Sines, [2] Law Of Cosines, [3] Pythagorean Theorem\n(Use 'back' to return to geometric menu or 'quit' for main menu)", move = False, align = "center", font = ("Arial", 16, "normal"))        
		t.pd()
		t.pensize(1)
		t.setheading(0)
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state

def geometric_polygon_angle_measure_screen(bgfgcolor):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.color(bgfgcolor[1])
		t.pu()
		t.setpos(0,65)
		t.pd()
		t.pensize(5)
		t.bk(45)
		for i in range(5):
				t.fd(90)
				t.left(72)
		t.fd(25)
		t.left(90)
		t.color("red")
		t.circle(25,108)
		t.color("green")
		t.circle(25,72)
		t.pensize(5)
		t.color(bgfgcolor[1])
		t.left(90)
		t.bk(15)
		t.fd(130)
		t.left(126)
		t.fd(77)
		t.right(108)
		t.fd(77)
		t.right(126)
		t.fd(90)
		t.right(126)
		t.fd(47)
		t.right(90)
		t.color("orange")
		t.circle(30,70)
		t.pu()
		t.color(bgfgcolor[1])
		t.setpos(160,140)
		t.write("(Example Polygon)", move = False, align = "center", font = ("Arial", 16, "normal"))
		t.setpos(0,-25)
		t.color(bgfgcolor[1])
		t.pd()
		t.write("Choose whichever value you have\nto begin solving a polygon:", move = False, align = "center", font = ("Arial", 24, "normal"))
		t.pu()
		t.setpos(0,-140)
		t.pd()
		t.write("[1] Interior Angle (red)\n[2] Exterior Angle (green)\n[3] Central Angle (orange)\n[4] Number Of Sides", move = False, align = "center", font = ("Arial", 20, "normal"))
		t.setheading(0)
		w.tracer(True) #Returns the screen animations to the standard state

def geometric_polygon_angle_input_screen(bgfgcolor, currentpolypath):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.color(bgfgcolor[1])
		t.pu()
		t.setpos(0,65)
		t.pd()
		t.pensize(5)
		t.bk(45)
		for i in range(5):
			t.fd(90)
			t.left(72)
		t.fd(25)
		t.left(90)
		t.color("red")
		t.circle(25,108)
		t.color("green")
		t.circle(25,72)
		t.pensize(5)
		t.color(bgfgcolor[1])
		t.left(90)
		t.bk(15)
		t.fd(130)
		t.left(126)
		t.fd(77)
		t.right(108)
		t.fd(77)
		t.right(126)
		t.fd(90)
		t.right(126)
		t.fd(47)
		t.right(90)
		t.color("orange")
		t.circle(30,70)
		t.pu()
		t.color(bgfgcolor[1])
		t.setpos(160,140)
		t.write("(Example Polygon)", move = False, align = "center", font = ("Arial", 16, "normal"))
		t.setpos(0,-50)
		t.pd()
		t.write("Enter the value of " + str(currentpolypath) + ":", move = False, align = "center", font = ("Arial", 24, "normal"))
		t.setheading(0)
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state

def geometric_polygon_measure_choice_in_choice_screen(bgfgcolor, polychoi1, polychoi2, polychoi3):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.color(bgfgcolor[1])
		t.pu()
		t.setpos(0,65)
		t.pd()
		t.pensize(5)
		t.bk(45)
		for i in range(5):
			t.fd(90)
			t.left(72)
		t.fd(25)
		t.left(90)
		t.color("red")
		t.circle(25,108)
		t.color("green")
		t.circle(25,72)
		t.pensize(5)
		t.color(bgfgcolor[1])
		t.left(90)
		t.bk(15)
		t.fd(130)
		t.left(126)
		t.fd(77)
		t.right(108)
		t.fd(77)
		t.right(126)
		t.fd(90)
		t.right(126)
		t.fd(47)
		t.right(90)
		t.color("orange")
		t.circle(30,70)
		t.pu()
		t.color(bgfgcolor[1])
		t.setpos(160,140)
		t.write("(Example Polygon)", move = False, align = "center", font = ("Arial", 16, "normal"))
		t.setpos(0,-50)
		t.write("Choose your path with the\ncorresponding value: ", move = False, align = "center", font = ("Arial", 24, "normal"))
		t.setpos(0,-150)
		t.pd()
		t.write("[1] " + polychoi1 + "\n[2] " + polychoi2 + "\n[3] " + polychoi3, move = False, align = "center", font = ("Arial", 24, "normal"))
		t.setheading(0)
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state

def geometric_polygon_measure_choice_screen(bgfgcolor):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		if bgfgcolor[0] == "black":
			circle_fill_color = "grey"
			perimeter_color = "white"
		elif bgfgcolor[0] == "white":
			circle_fill_color = "light grey"
			perimeter_color = "black"
		t.color(bgfgcolor[1])
		t.pu()
		t.setpos(160,140)
		t.write("(Example Polygon)", move = False, align = "center", font = ("Arial", 16, "normal"))
		t.setpos(0,65)
		t.bk(45)
		t.color(circle_fill_color)
		t.begin_fill()
		for i in range(5):
			t.fd(90)
			t.left(72)
		t.end_fill()
		t.color(perimeter_color)
		t.pd()
		t.pensize(5)
		t.color("magenta")
		t.fd(90)
		t.left(72)
		t.color(perimeter_color)
		for i in range(4):
			t.fd(90)
			t.left(72)
		t.left(54)
		t.color("red")
		t.fd(75)
		t.right(144)
		t.color("green")
		t.fd(60)
		t.pu()
		t.color(bgfgcolor[1])
		t.setheading(0)
		t.setpos(0,25)
		t.pd()
		t.write("Choose your path depending on which values you have: ", move = False, align = "center", font = ("Arial", 18, "normal"))
		t.pu()
		t.setpos(0,-230)
		t.write("[1] Apothem (green) AND either\nSide Length (pink), Perimeter (pink + " + perimeter_color + ") or Area (grey)\n\n[2] Radius (red)\n\n[3] Area(grey) AND either\nSide Length (pink), Perimeter (pink + white) or Apothem (green)\n\n[4] Show Angle Measures Of Polygon Without Other Measures\n\n\nOther trigonometry related methods can be accessed in Triangle Solving.\nUse 'back' to return to polygon menu", move = False, align = "center", font = ("Arial", 16, "normal"))
		t.setheading(0)
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient 
		w.tracer(True) #Returns the screen animations to the standard state 

def geometric_polygon_draw_polygon(bgfgcolor, polynumofsides, polyinteriorang, polycentralang, polyexteriorang,polyradius,polyapothem,polysidelength):

		if bgfgcolor[0] == "black":
			circle_fill_color = "grey"
			perimeter_color = "white"
		elif bgfgcolor[0] == "white":
			circle_fill_color = "light grey"
			perimeter_color = "black"
		t.pu()
		t.pensize(5)
		t.setpos(0,50)
		t.bk(polysidelength/2)
		t.pu()
		t.color(circle_fill_color)
		t.begin_fill()
		for i in range(polynumofsides):
			t.fd(polysidelength)
			t.left(180)
			t.right(polyinteriorang)
		t.end_fill()
		t.color("magenta")
		t.pd()
		t.fd(polysidelength)
		t.left(180)
		t.right(polyinteriorang)
		t.color(bgfgcolor[1])
		for i in range(polynumofsides - 1):
			t.fd(polysidelength)
			t.left(180)
			t.right(polyinteriorang)
		t.left(180)
		t.right(polyinteriorang/2+polyexteriorang)
		t.color("red")
		t.fd(polyradius)
		t.left(180)
		t.left(polycentralang/2)
		t.color("green")
		t.fd(polyapothem)
		t.pu()
		t.left(90)
		t.fd(polysidelength/2)
		t.left(180)
		t.right(polyinteriorang)
		t.fd(polysidelength)
		t.color(bgfgcolor[1])
		t.pd()
		t.fd(40)
		t.bk(15)
		t.left(90)
		t.color("orange")
		t.circle(25,polyexteriorang)
		t.color("cornflower blue")
		t.circle(25,polyinteriorang)
		t.pu()
		t.setpos(0,50)
		t.setheading(0)
		t.bk(polysidelength/2)
		for i in range(2):
			t.fd(polysidelength)
			t.left(180)
			t.right(polyinteriorang)
		t.left(180)
		t.right(polyinteriorang/2+polyexteriorang)
		t.pd()
		t.color(bgfgcolor[1])
		t.fd(polyradius)
		t.left(180)
		t.left(polycentralang)
		t.fd(polyradius)
		t.bk(polyradius-25)
		t.left(90)
		t.pu()
		t.circle(25,360-polyexteriorang)
		t.color("light green")
		t.pd()
		t.circle(25,polyexteriorang)
		t.pu()
		t.color(bgfgcolor[1])
		t.setheading(0)
        
def geometric_polygon_answer_screen(bgfgcolor, polyradius, polyapothem, polysidelength, polyperimeter, polyarea, polyintang, polyextang, polycenang, polynumberofsides):
	if bgfgcolor[0] == "black":
		circle_fill_color = "grey"
		perimeter_color = "white"
	elif bgfgcolor[0] == "white":
		circle_fill_color = "light grey"
		perimeter_color = "black"
	t.setpos(-240,-75)
	t.write("radius (red) = " + str(polyradius) + "\napothem (green) = " + str(polyapothem) + "\nside length (pink) = " + str(polysidelength) + "\nperimeter = " + str(polyperimeter) + "\narea (grey) = " + str(polyarea), move = False, align = "left", font = ("Arial", 16, "normal"))
	t.setpos(0,-75)
	t.write("interior angle (blue) = " + str(polyintang) + "\nexterior angle (orange) = " + str(polyextang) + "\ncentral angle (light green) = " + str(polycenang) + "\nnumber of sides = " + str(polynumberofsides), move = False, align = "left", font = ("Arial", 16, "normal"))
	t.setpos(0,-215)
	t.write("To solve another polygon, choose your\npath with the corresponding number:\n[1] Interior Angle (blue)\n[2] Exterior Angle (orange)\n[3] Central Angle (light green)\n[4] Number Of Sides", move = False, align = "center", font = ("Arial", 18, "normal"))

def geometric_polygon_get_measures(bgfgcolor, polynumofsides, polycentralangle):
	polygon_radius_length_for_drawing = 80.0
	polygon_number_of_sides_for_drawing = polynumofsides
	polygon_side_length_for_drawing = math.sqrt((polygon_radius_length_for_drawing**2 + polygon_radius_length_for_drawing**2 - 2 * polygon_radius_length_for_drawing * polygon_radius_length_for_drawing * math.cos(math.radians(polycentralangle))))
	polygon_perimeter_length_for_drawing = polygon_side_length_for_drawing * polygon_number_of_sides_for_drawing
	polygon_apothem_length_for_drawing = math.sqrt(polygon_radius_length_for_drawing**2 - (polygon_side_length_for_drawing / 2)**2)
	polygon_area_measure_for_drawing = (polygon_perimeter_length_for_drawing * polygon_apothem_length_for_drawing) / 2

	polygon_radius_length_for_drawing = round_answer(polygon_radius_length_for_drawing)
	polygon_apothem_length_for_drawing = round_answer(polygon_apothem_length_for_drawing)
	polygon_side_length_for_drawing = round_answer(polygon_side_length_for_drawing)
	polygon_perimeter_length_for_drawing = round_answer(polygon_perimeter_length_for_drawing)
	polygon_area_measure_for_drawing = round_answer(polygon_area_measure_for_drawing)

	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates

	geometric_polygon_draw_polygon(bgfgcolor,polygon_number_of_sides,polygon_interior_angle,polygon_central_angle,polygon_exterior_angle,polygon_radius_length_for_drawing,polygon_apothem_length_for_drawing,polygon_side_length_for_drawing)
	geometric_polygon_answer_screen(bgfgcolor, polygon_radius_length,polygon_apothem_length, polygon_side_length,polygon_perimeter_length,polygon_area_measure,polygon_interior_angle,polygon_exterior_angle,polygon_central_angle,polygon_number_of_sides)

	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def graphing_main_menu(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.setpos(0,125)
	main_menu_graphing_icon(bgfgcolor)
	t.color(bgfgcolor[1])
	t.setpos(0,-50)
	t.write("Choose your path with the\ncorresponding values:", move = False, align = "center", font = ("Arial", 26, "normal"))
	t.setpos(-120,-100)
	t.write("[1] Graphing a point", move = False, align = "center", font = ("Arial", 22, "normal"))
	t.setpos(120,-100)
	t.write("[2] Graphing a slope", move = False, align = "center", font = ("Arial", 22, "normal"))
	t.setpos(0,-150)
	t.write("[3] Finding the distance between points", move = False, align = "center", font = ("Arial", 22, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def graphing_graph_template(bgfgcolor):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		t.pu()
		t.setpos(0,50)
		t.color(bgfgcolor[1])
		t.pd()
		for i in range(4):
			for i in range(15):
				t.pensize(5)
				t.fd(10)
				t.pensize(2)
				t.left(90)
				t.fd(4)
				t.bk(8)
				t.fd(4)
				t.right(90)
			t.pensize(5)
			t.fd(10)
			t.left(135)
			t.fd(10)
			t.bk(10)
			t.right(270)
			t.fd(10)
			t.bk(10)
			t.left(135)
			t.bk(160)
			t.left(90)
		t.setheading(0)
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state
		t.ht()

def graphing_input_screen(bgfgcolor, currentgraphingpath):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(0,0)
	t.pd()
	graphing_graph_template(bgfgcolor)
	t.pu()
	t.setpos(0,-175)
	t.pd()
	t.write("Enter the value of\n" + currentgraphingpath + ":", move = False, align = "center", font = ("Arial", 22, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def graphing_point_on_graph(bgfgcolor, pointcoordinatex, pointcoordinatey):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		graphing_graph_template(bgfgcolor)
		t.pu()
		t.color("red")
		t.setpos(pointcoordinatex*5,(pointcoordinatey*5)+50)
		t.bk(5)
		t.begin_fill()
		t.right(90)
		t.circle(5)
		t.end_fill()
		t.color(bgfgcolor[1])
		t.setheading(0)
		t.setpos(125,-100)
		t.bk(10)
		t.write("The red point is on (" + str(pointcoordinatex) + "," + str(pointcoordinatey) + ")\n*Drawn to scale", move = False, align = "center", font = ("Arial", 14, "normal"))
		t.setpos(0,-200)
		t.write("Enter another point in x,y format to graph it\nor return to graphing menu by inputting 'back'", move = False, align = "center", font = ("Arial", 20, "normal"))
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state

def graphing_slope_on_graph(bgfgcolor, full_slope_eq, yintercept, xpoint1, ypoint1, xpoint2, ypoint2):
	t.clear() #Clears all previous drawings by turtle
	t.ht()
	t.setheading(0)
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	graphing_graph_template(bgfgcolor)
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.pu()
	t.color("red")
	t.setpos(0,0) #moves turtle to 0,0
	t.setpos(xpoint2,ypoint2) #moves turtle to the second x,y coordinate
	t.setheading(turtle.towards(xpoint1,ypoint1)) #points turtle towards the first point
	if yintercept == 0:
		t.sety(t.ycor()+50)
	else:
		t.sety(t.ycor()+(yintercept*5+50))
	t.pu()
	forward_slope = True
	while forward_slope == True:
		if float(t.xcor()) < 140 and float(t.xcor()) > -140 and float(t.ycor()) < 190 and float(t.ycor()) > -90:
			t.fd(1)
		else:
			t.pu()
			t.bk(3)
			t.pd()
			forward_slope = False
			backward_slope = True
	while backward_slope == True:
		if float(t.xcor()) < 140 and float(t.xcor()) > -140 and float(t.ycor()) < 190 and float(t.ycor()) > -90:
			t.pd()
			t.bk(1)
		else:
			t.pu()
			break
	t.color(bgfgcolor[1])
	t.setheading(0)
	t.setpos(0,-155)
	t.write("Slope " + full_slope_eq + " graphed in red\n*Drawn to scale", move = False, align = "center", font = ("Arial", 16, "normal"))
	t.setpos(0,-225)
	t.write("To graph another slope enter an equation\nin y = mx + b format\nOr return to graphing menu by inputting 'back'", move = False, align = "center", font = ("Arial", 18, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def graphing_distance_point_on_graph(bgfgcolor, pointcoordinatex1, pointcoordinatey1, pointcoordinatex2, pointcoordinatey2, distbetweenpoints):
		t.clear() #Clears all previous drawings by turtle
		w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
		graphing_graph_template(bgfgcolor)
		t.pu()
		t.pensize(5)
		t.color("red")
		t.setpos(pointcoordinatex1*5,pointcoordinatey1*5+50)
		t.bk(5)
		t.begin_fill()
		t.right(90)
		t.circle(5)
		t.end_fill()
		t.setheading(0)
		t.setpos(pointcoordinatex2*5,pointcoordinatey2*5+50)
		t.bk(5)
		t.begin_fill()
		t.right(90)
		t.circle(5)
		t.end_fill()
		t.color("green")
		t.pensize(3)
		t.fd(5)
		t.pd()
		t.setpos(pointcoordinatex1*5,pointcoordinatey1*5+50)
		t.color(bgfgcolor[1])
		t.setheading(0)
		t.pu()
		t.setpos(0,-155)
		t.bk(10)
		t.pu()
		t.write("The distance between the points " + str(pointcoordinatex1) + "," + str(pointcoordinatey1) + " and " + str(pointcoordinatex2) + "," + str(pointcoordinatey2) + " is " + str(distbetweenpoints) + "\n*Drawn to scale", move = False, align = "center", font = ("Arial", 14, "normal"))        
		t.setpos(0,-215)
		t.write("Enter another point in x,y format to find the distance between 2 points\nOr input 'back' to return to graphing menu", move = False, align = "center", font = ("Arial", 16, "normal")) 
		w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
		w.tracer(True) #Returns the screen animations to the standard state

def settings_screen(bgfgcolor):
	t.clear() #Clears all previous drawings by turtle
	w.tracer(False) #Turns Off Turtle Animation, Runs Following Drawings Without Screen Updates
	t.pu()
	t.color(bgfgcolor[1])
	t.setpos(0,110)
	t.pd()
	main_menu_settings_icon(background_foreground_color)
	t.pu()
	t.setpos(0,-125)
	t.pd()
	t.color(bgfgcolor[1])
	t.write("To enable dark mode, input '1'.\nTo enable light mode, input '2'.\n\nUse 'back' or 'quit' to return to\nthe main menu.", move = False, align = "center", font = ("Arial", 26, "normal"))
	w.update() #Manually refreshes screen, makes drawings made previously appear along with this refresh, this makes the drawing faster, as it doesn't constantly update to show progress, and makes it more efficient
	w.tracer(True) #Returns the screen animations to the standard state

def navigation_screen(bgfgcolor):
	t.clear()
	w.tracer(False)
	t.color(bgfgcolor[1])
	t.pu()
	t.setpos(0,-50)
	t.write("To enter a mode input the corresponding number.\nTo return to the previous screen input 'back'.\nTo return to the main menu input 'quit'.\nTo switch to the most recent mode used input 'switch'.\nTo exit input screens if first 'back' doesn't work, input it again.\nTo change color scheme go to settings.\nTo turn off calculator input 'quit' on main menu.", move = False, align = "center", font = ("Arial", 17, "normal"))        
	w.update()
	w.tracer(True)

#defining non-turtle functions
def format_input(stringinput):
	stringinput = stringinput.lower() #makes input lowercase
	stringinput = stringinput.replace(" ", "") #removes all whitespace between characters in the input
	return stringinput #returns the formatted string

def round_answer(answerinput):
	if type(answerinput) == float: #rounds values depending on how many digits are before the decimal point, if there are 9 or more it defaults to rounding to one digit, anything less will round to the digit that will keep the answer 11 digits long in total
		answerinput = str(answerinput)
		if len(answerinput[:answerinput.find(".")]) >= 9:
			answerinput = round(float(answerinput), 1)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 8:
			answerinput = round(float(answerinput), 2)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 7:
			answerinput = round(float(answerinput), 3)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 6:
			answerinput = round(float(answerinput), 4)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 5:
			answerinput = round(float(answerinput), 5)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 4:
			answerinput = round(float(answerinput), 6)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 3:
			answerinput = round(float(answerinput), 7)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 2:
			answerinput = round(float(answerinput), 8)
			return answerinput
		elif len(answerinput[:answerinput.find(".")]) == 1:
			answerinput = round(float(answerinput), 9)
			return answerinput
	else:
		return answerinput #if the answer is not a float, no rounding can be done, so it prints to float

while calc_start == True: #starts the calculator looping process
	if path == "undefined": #asks for input for path only if the path is undefined, allowing for automated switching between modes
		main_menu_screen(background_foreground_color) #draws main menu screen
		turtle_title = "Calculator Main Menu" #defines the title for the mode
		title_for_mode(turtle_title, background_foreground_color) #draws the title using previously defined string
		path = input("Choose your path with the corresponding number: ") #asks the user for path input
		path = format_input(path) #formats input

		#paths for the current choice
		"""
		1 - Algebraic Calculator
		2 - Geometric Calculator
		3 - Graphing Calculator
		4 - Settings

		"""

	#Algebraic Calculator
	if path == "1": #Equality Solver, Inequality Solver, Standard Calculator
		algebraic_calc = True #while this value is true, this mode of calculator will loop
		turtle_title = "Algebraic Calculator" #defines the title for the mode
		title_for_mode(turtle_title, background_foreground_color) #draws the title using previously defined string
		algebraic_input_screen(background_foreground_color) #draws algebraic input screen
		while algebraic_calc == True: #starts the looping process
			algebraic_equation = input("(Algebraic Equation) Enter the equation you would like to solve:\n") #asks the user to enter an equation
			algebraic_equation = format_input(algebraic_equation) #formats this equation so that sorting is easier and has less errors

			#paths for current choice (it is automatically decided by looking at the input, no path choice is needed)
			"""
			* - Equality Solver
			* - Inequality Solver
			* - Standard Calculator

			"""

			if algebraic_equation == "back" or algebraic_equation == "quit": #makes sure you can exit the mode by checking the input for exit keywords
				path = "undefined" #sets the path for the main menu to undefined, requiring the user to choose a path again
				prev_path = "1" #sets previous path to '1' for algebraic mode
				break #breaks out of loop

			if algebraic_equation == "switch": #switches to the most recent mode when 'switch' is entered
				path = prev_path #sets the path for the main menu to the previous path, not requiring the user to choose a path again
				prev_path = "1" #sets previous path to '1' for algebraic mode
				break #breaks out of loop

			else:
				if "ans" in algebraic_equation: #replaces ans with the answer to the previous equation, default value of ans is '1'
					algebraic_equation = algebraic_equation.replace("ans", str(ans))
				if "v" in algebraic_equation: #replaces 'v' with math.sqrt, this is for ease of use, math.sqrt still works
					algebraic_equation = algebraic_equation.replace("v", "math.sqrt")
				if "^" in algebraic_equation: #replaces 'v' with math.sqrt, this is for ease of use, ** still works
					algebraic_equation = algebraic_equation.replace("^", "**")
				if "pi" in algebraic_equation: #replaces 'pi' with math.pi, this is for ease of use, math.pi still works
					algebraic_equation = algebraic_equation.replace("pi", "math.pi")

				if algebraic_equation[0] == "x": #puts a '1' before x if x is the first digit of the equation, this is needed when solving for x
					algebraic_equation = "1" + algebraic_equation

				for i in range(len(algebraic_equation)): #for every character in the input, it checks if the value before x is a number, if it isn't, it adds a '1', this is needed when solving for x
					if algebraic_equation[i] == "x":
						character_before_x = algebraic_equation[i-1]
						if character_before_x.isdigit() == False:
							algebraic_equation = algebraic_equation[:i] + "1" + algebraic_equation[i:]


				#Equality Solver
				if algebraic_equation.find("=") != -1 and algebraic_equation.find("<") == -1 and algebraic_equation.find(">") == -1 and algebraic_equation.find("x") != -1: #checks to see if the equation has only an '=' sign and no other inequality signs, if true the equation is treated as an equality
					try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely 
						turtle_title = "Algebraic Calculator: Equality Equation"
						title_for_mode(turtle_title, background_foreground_color)
						algebraic_equation = algebraic_equation.strip() #strips the input of whitespace preceeding or following actual text
						equality = True #sets equality to True so that the process needed to solve for x can take place

						split_equation1 = algebraic_equation[:algebraic_equation.find("=")] #splits the equation into 2 sides, the part before the equals sign, and after the equals sign 
						split_equation2 = algebraic_equation[algebraic_equation.find("=")+1:]
		
						x_value = 0 #sets default x value to 0, the x value is the value that is guessed
						prev_num_dif = 10000 #sets the previous number difference to a high number that shouldn't interfere with the program
						prev_prev_num_dif = 100000 #sets the number difference before the previous number difference to a high number that shouldn't interfere with the program

						while equality == True:
							num1 = split_equation1.replace("x", "*" + str(x_value)) #replaces the x value with '*' and the current x value, x needs a coefficient before it for this equation to work
							num2 = split_equation2.replace("x", "*" + str(x_value)) #replaces the x value with '*' and the current x value, x needs a coefficient before it for this equation to work
							ans1 = eval(num1) #evaluates both sides of the equation
							ans2 = eval(num2) #evaluates both sides of the equation
							if ans1 != ans2:  #while the answers aren't equal, it runs the following code
								num_dif = abs(ans1 - ans2) #it finds the number difference between the two numbers
								if prev_prev_num_dif == num_dif: #to stop it from looping, if the current number difference is the same as the previous, previous number difference, then it sets the x value to -1 (i did the math and it needs to do this because if x is  a negative value, the program cant solve it and begins looping, this  fixes the looping)
									x_value = -1
								if x_value < 0: #if the x value is below 0 the process for finding x reverses, where if the number difference is less, the x value gets subtracted from and if it is more it gets added to
									if num_dif < prev_num_dif:
										x_value = x_value - 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
									elif num_dif > prev_num_dif:
										x_value = x_value + 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
								else:  #if the x value is above 0 the process for finding x is as usual, where if the number difference is less, the x value gets added to and if it is more it gets subtracted from
									if num_dif < prev_num_dif:
										x_value = x_value + 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
									elif num_dif > prev_num_dif:
										x_value = x_value - 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
							elif ans1 == ans2: #until the both sides are equal to each other, the process above loops, when the value for x is found, this  process is finished
								equality = False
						ans = x_value #sets the value for the previous answer to the current value of x
						ans_on_screen = ("x = " + str(x_value)) #the answer that is displayed on the turtle screen
						type_of_algebraic_equation = "Equality" #the type of equation completed
						algebraic_answer_screen(background_foreground_color)  #draws the turtle screen for the answer
					except SyntaxError: #error handling
						print("syntax error")
					except NameError: #error handling
						print("name error")
					except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
						print("unknown error")

				#Inequality Solver
				elif algebraic_equation.find("<") != -1 or algebraic_equation.find(">") != -1 or algebraic_equation.find("<=") != -1 or algebraic_equation.find(">=") != -1 and algebraic_equation.find("x") != -1:
					try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
						turtle_title = "Algebraic Calculator: Inequality Equation" #title for the turtle title
						title_for_mode(turtle_title, background_foreground_color) #draws the title on screen
						algebraic_equation = algebraic_equation.strip() #strips the equation of preceeding and proceeding whitespace

						if algebraic_equation.find("<") != -1 and algebraic_equation.find("=") == -1: #depending on which characters the input has, it sorts through to determine the sign of the inequality
							inequality_symbol = "<"
							split_equation1 = algebraic_equation[:algebraic_equation.find(str(inequality_symbol))]
							split_equation2 = algebraic_equation[algebraic_equation.find(str(inequality_symbol))+1:]
						elif algebraic_equation.find(">") != -1 and algebraic_equation.find("=") == -1:
							inequality_symbol = ">"
							split_equation1 = algebraic_equation[:algebraic_equation.find(str(inequality_symbol))]
							split_equation2 = algebraic_equation[algebraic_equation.find(str(inequality_symbol))+1:]
						elif algebraic_equation.find("<") != -1 and algebraic_equation.find("=") != -1:
							inequality_symbol = "<="
							split_equation1 = algebraic_equation[:algebraic_equation.find(str(inequality_symbol))]
							split_equation2 = algebraic_equation[algebraic_equation.find(str(inequality_symbol))+2:]
						elif algebraic_equation.find(">") != -1 and algebraic_equation.find("=") != -1:
							inequality_symbol = ">="
							split_equation1 = algebraic_equation[:algebraic_equation.find(str(inequality_symbol))]
							split_equation2 = algebraic_equation[algebraic_equation.find(str(inequality_symbol))+2:]

						if split_equation1[0] == "x": #adds '1' in front of x if x is the first value in the string
							split_equation1 = split_equation1.replace("x", "1x")
						if split_equation1[0] == "=":
							split_equation1 = split_equation1[1:]

						if split_equation2[0] == "x":
							split_equation2 = split_equation2.replace("x", "1x")
						if split_equation2[0] == "=":
							split_equation2 = split_equation2[1:]

						x_value = 0 #sets default x value to 0, the x value is the value that is guessed
						prev_num_dif = 10000 #sets the previous number difference to a high number that shouldn't interfere with the program
						prev_prev_num_dif = 100000 #sets the number difference before the previous number difference to a high number that shouldn't interfere with the program

						equality = True #treats the inequality as an equality in the first instance, to solve for the base or max value of x
						while equality == True: #see lines about  equality for info on this, same process up until the end
							num1 = split_equation1.replace("x", "*" + str(x_value)) 
							num2 = split_equation2.replace("x", "*" + str(x_value))
							ans1 = eval(num1)
							ans2 = eval(num2)
							if ans1 != ans2:
								num_dif = abs(ans1 - ans2)
								if prev_prev_num_dif == num_dif:
									x_value = -1
								if x_value < 0:
									if num_dif < prev_num_dif:
										x_value = x_value - 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
									elif num_dif > prev_num_dif:
										x_value = x_value + 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
								else:
									if num_dif < prev_num_dif:
										x_value = x_value + 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
									elif num_dif > prev_num_dif:
										x_value = x_value - 1
										prev_prev_num_dif = prev_num_dif
										prev_num_dif = num_dif
							elif ans1 == ans2:
								equality = False
						num1 = split_equation1.replace("x", "*" + str(x_value)) #replaces the x with the current x value
						num2 = split_equation2.replace("x", "*" + str(x_value)) #replaces the x with the current x value
						ans1 = eval(num1) #evaluates one side of the expression
						ans2 = eval(num2) #evaluates one side of the expression
						inequality_equation = str(ans1) + str(inequality_symbol) + str(ans2) #defines the inequality expression
						if eval(inequality_equation) == True: #if the inequality expression is true in its current state it finds out that x must be equal to or greater/lesser
							equal_to_inequality = True
						elif eval(inequality_equation) == False: #if the inequality expression is false in its current state it finds out that x cannot be equal to and must be greater or lesser
							equal_to_inequality = False
						x_value = x_value + 1 #adds '1' to the x value to see if x is greater or lesser in the inequality
						num1 = split_equation1.replace("x", "*" + str(x_value))
						num2 = split_equation2.replace("x", "*" + str(x_value))
						ans1 = eval(num1)
						ans2 = eval(num2)
						inequality_equation = str(ans1) + str(inequality_symbol) + str(ans2)
						if eval(inequality_equation) == True: #if x+1 is true then x is larger than the other side of the equation
							x_value = x_value - 1 #returns x to its correct value
							if equal_to_inequality == True: #depending on whether or not the previous process found the inequality to be equal to or greater/lesser than it prints with the correct signs in front of x
								ans_on_screen = ("x >= " + str(x_value))
							elif equal_to_inequality == False:#depending on whether or not the previous process found the inequality to be equal to or greater/lesser than it prints with the correct signs in front of x
								ans_on_screen = ("x > " + str(x_value))
						else: #if x+1 is false then x is smaller than the other side of the equation
							turtle_title = "Algebraic Calculator: Standard Equation"
							title_for_mode(turtle_title, background_foreground_color)
							x_value = x_value - 1 #returns x to its correct value
							if equal_to_inequality == True:#depending on whether or not the previous process found the inequality to be equal to or greater/lesser than it prints with the correct signs in front of x
								ans_on_screen = ("x <= " + str(x_value))
							elif equal_to_inequality == False:#depending on whether or not the previous process found the inequality to be equal to or greater/lesser than it prints with the correct signs in front of x
								ans_on_screen = ("x < " + str(x_value))
						type_of_algebraic_equation = "Inequality" #sets the type of equation on screen
						algebraic_answer_screen(background_foreground_color) #draws the answers on screen
					except SyntaxError: #error handling
						print("syntax error")
					except NameError: #error handling
						print("name error")
					except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
						print("unknown error")

				#Standard Calculator			
				else:
					try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
						solution = eval(algebraic_equation)
						solution = round_answer(solution)
						ans = solution
						ans_on_screen = ("=" + str(solution))
						type_of_algebraic_equation = 'Standard Equation'
						algebraic_answer_screen(background_foreground_color)
					except SyntaxError: #error handling
						print("syntax error")
					except NameError: #error handling
						print("name error")
					except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
						print("unknown error")

	#Geometric Calculator
	if path == "2": #Circle Solver, Triangle Solver, Regular Polygon Solver
		geometric_calc = True #begins the geometric calculator process
		geometric_path = "undefined" #sets input to undefined to that the input is asked for
		while geometric_calc == True: #while true, following code loops
			if geometric_path == "undefined":
				turtle_title = "Geometric Calculator: Main Menu" #title of screen
				title_for_mode(turtle_title, background_foreground_color) #draws title on screen
				geometric_menu_screen(background_foreground_color) #draws the menu screen for the geometric mode
				geometric_path = input("(Geometric Solver) Choose your path with the corresponding number: ") #asks for user input on path
				geometric_path = format_input(geometric_path) #formats path

			#possible path choices
			"""
			1 - Circle Solver
			2 - Triangle Solver
			3 - Regular Polygon Solver

			"""

			if geometric_path == "back" or geometric_path == "quit": #allows user to exit out of mode
				path = "undefined"
				prev_path = "2"
				break
			if geometric_path == "switch": #allows user to switch out of mode
				path = prev_path
				prev_path = "2"
				break

			if geometric_path == "1": #Circle Solver: Radius, Circumference, Area, Arc Measure and Central Angle, Arc Area and Central Angle
				circle_solver = True #begins circle solver process
				geometric_circle_input_screen(background_foreground_color) #draws the screen for circle input
				while circle_solver == True:
					turtle_title = "Geometric Calculator: Circle Solver" #defines the title for the screen
					title_for_mode(turtle_title, background_foreground_color) #draws the title for the screen
					type_of_circle_input = input("(Circle Solver) Choose the value you have with the corresponding number: ") #asks the user for input on path
					type_of_circle_input = format_input(type_of_circle_input) #formats input

					if type_of_circle_input == "back": #allows user to exit out of mode
						geometric_path = "undefined"
						prev_path = "2"
						break

					if type_of_circle_input == "quit": #allows user to exit out of mode
						geometric_path = "quit"
						path = "undefined"
						break

					if type_of_circle_input == "switch": #allows user to switch out of mode
						path = prev_path
						prev_path = "2"
						geometric_path = "quit"
						break

					#possible path choices
					"""
					1 - Radius
					2 - Circumference
					3 - Area
					4 - Arc Measure and Central Angle
					5 - Arc Area and Central Angle

					"""
	
					if type_of_circle_input == "1": #Radius
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							circle_input_choice = "radius" #defines the choice by the user
							turtle_title = "Geometric Calculator: Circle Solver Using Radius" #defines the title of the mode
							title_for_mode(turtle_title, background_foreground_color) #draws title for mode
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice) #draws the screen for the input type
							circle_radius = input("Enter the value of the radius: ") #solving circles with the corresponding formulas
							circle_circumference = eval("2 * math.pi * " + str(circle_radius)) #solving circles with the corresponding formulas
							circle_area = eval("math.pi*(" + str(circle_radius) + " * " + str(circle_radius) + " )") #solving circles with the corresponding formulas
							
							circle_radius = round_answer(circle_radius) #rounds answers
							circle_circumference = round_answer(circle_circumference) #rounds answers
							circle_area = round_answer(circle_area) #rounds answers

							geometric_circle_answer_screen(background_foreground_color, circle_radius, circle_circumference, circle_area)

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif type_of_circle_input == "2": #Circumference
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							circle_input_choice = "circumference"
							turtle_title = "Geometric Calculator: Circle Solver Using Circumference"
							title_for_mode(turtle_title, background_foreground_color)
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice)
							circle_circumference = input("Enter the value of the circumference: ") #solving circles with the corresponding formulas
							circle_area = eval("( " + str(circle_circumference) + " / (2 * math.pi)) * ( " + str(circle_circumference) + " / (2 * math.pi)) * math.pi") #solving circles with the corresponding formulas
							circle_radius = eval("( " + str(circle_circumference) + " / (2 * math.pi))") #solving circles with the corresponding formulas

							circle_radius = round_answer(circle_radius) #rounds answers
							circle_circumference = round_answer(circle_circumference) #rounds answers
							circle_area = round_answer(circle_area) #rounds answers
							
							geometric_circle_answer_screen(background_foreground_color, circle_radius, circle_circumference, circle_area)

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif type_of_circle_input == "3": #Area
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							circle_input_choice = "area"
							turtle_title = "Geometric Calculator: Circle Solver Using Area"
							title_for_mode(turtle_title, background_foreground_color)
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice)
							circle_area = input("Enter the value of the area: ") #solving circles with the corresponding formulas
							circle_radius = eval("math.sqrt((" + str(circle_area) + "/math.pi))") #solving circles with the corresponding formulas
							circle_circumference = eval("(math.sqrt((" + str(circle_area) + " / math.pi))) * math.pi * 2") #solving circles with the corresponding formulas

							circle_radius = round_answer(circle_radius) #rounds answers
							circle_circumference = round_answer(circle_circumference) #rounds answers
							circle_area = round_answer(circle_area) #rounds answers
							
							geometric_circle_answer_screen(background_foreground_color, circle_radius, circle_circumference, circle_area)

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif type_of_circle_input == "4": #Arc Length and Measure
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							circle_input_choice = "arc length"
							turtle_title = "Geometric Calculator: Circle Solver Using Arc Length and Measure"
							title_for_mode(turtle_title, background_foreground_color)
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice)
							circle_arc_length = input("Enter the value of the arc length: ")
							circle_input_choice = "arc angle measure"
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice)
							circle_arc_measure = input("Enter the value of the arc measure in degrees:")
							circle_radius = eval("( " + str(circle_arc_length) + " * 360 / " + str(circle_arc_measure) + " ) / (2 * math.pi)") #solving circles with the corresponding formulas
							circle_circumference = eval("2 * math.pi * " + str(circle_radius)) #solving circles with the corresponding formulas
							circle_area = eval("math.pi*(" + str(circle_radius) + " * " + str(circle_radius) + " )") #solving circles with the corresponding formulas

							circle_radius = round_answer(circle_radius) #rounds answers
							circle_circumference = round_answer(circle_circumference) #rounds answers
							circle_area = round_answer(circle_area) #rounds answers
							
							geometric_circle_answer_screen(background_foreground_color, circle_radius, circle_circumference, circle_area)

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif type_of_circle_input == "5": #Arc Area and Measure
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							circle_input_choice = "arc area"
							turtle_title = "Geometric Calculator: Circle Solver Using Arc Area and Measure"
							title_for_mode(turtle_title, background_foreground_color)
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice)
							circle_arc_area = input("Enter the value of the arc area: ")
							circle_input_choice = "arc angle measure"
							geometric_circle_input_type_screen(background_foreground_color, circle_input_choice)
							circle_arc_measure = input("Enter the value of the arc measure in degrees:")
							circle_radius = eval("math.sqrt((( " + str(circle_arc_area) + " * 360 / " + str(circle_arc_measure) + " ) / math.pi ))")#solving circles with the corresponding formulas
							circle_circumference = eval("2 * math.pi * " + str(circle_radius)) #solving circles with the corresponding formulas
							circle_area = eval("math.pi*(" + str(circle_radius) + " * " + str(circle_radius) + " )") #solving circles with the corresponding formulas

							circle_radius = round_answer(circle_radius) #rounds answers
							circle_circumference = round_answer(circle_circumference) #rounds answers
							circle_area = round_answer(circle_area) #rounds answers
							
							geometric_circle_answer_screen(background_foreground_color, circle_radius, circle_circumference, circle_area)

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif type_of_circle_input != "1" or type_of_circle_input != "2" or type_of_circle_input != "3" or type_of_circle_input != "4" or type_of_circle_input != "5" or type_of_circle_input != "back" or type_of_circle_input != "switch" or type_of_circle_input != "quit": #False Input
						print("bad input")

			elif geometric_path == "2": #Triangle Solver: Law Of Sines, Law Of Cosines, Pythagorean Theorem
				triangle_solver = True #begins triangle solver process
				geometric_triangle_path_screen(background_foreground_color) #draws the screen for triangle path options
				while triangle_solver == True:
					turtle_title = "Geometric Calculator: Triangle Solver" #defines title of screen
					title_for_mode(turtle_title, background_foreground_color) #draws title of screen
					type_of_triangle_input = input("(Triangle Solver) Choose your path depending on which values you have with the corresponding number: ") #asks the user for input on path=
					type_of_triangle_input = format_input(type_of_triangle_input) #formats input

					if type_of_triangle_input == "back": #allows user to exit out of mode
						geometric_path = "undefined"
						break

					if type_of_triangle_input == "quit": #allows user to exit out of mode
						geometric_path = "quit"
						path = "undefined"
						break

					if type_of_triangle_input == "switch": #allows user to switch out of mode
						path = prev_path
						prev_path = "2"
						geometric_path = "quit"
						break

					#possible path options
					"""
					1 - Law Of Sines
					2 - Law Of Cosines
					3 - Pythagorean Theorem

					"""

					if type_of_triangle_input == "1": #Law Of Sines: Two Side Lengths and One Angle, Two Angle Measures and One Side Length
						turtle_title = "Geometric Calculator: Law Of Sines" #defines the title
						current_triangle_path = "Law Of Sines" #defines the current path of triangle solving
						current_triangle_path_option1 = "[1] Two Side Lengths, One Angle Opposite\nOne Of The Side Lengths\n(Example: Side A, Side B, Angle A)" #gives two possible options
						current_triangle_path_option2 = "[2] Two Angle Measures, One Side Opposite\nOne Of The Angle Measures\n(Example: Angle A, Angle B, Side B)" #gives two possible options
						geometric_triangle_pathinpath_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1,current_triangle_path_option2)
						title_for_mode(turtle_title, background_foreground_color) #draws title
						triangle_sine_law_input = input("(Sine Law) Choose your path depending on which values you have with the corresponding number: ") #asks input for path
						triangle_sine_law_input = format_input(triangle_sine_law_input)

						if triangle_sine_law_input == "back":
							geometric_path = "undefined"
							break

						if triangle_sine_law_input == "quit":
							geometric_path = "quit"
							path = "undefined"
							break
							
						if triangle_sine_law_input == "switch":
							path = prev_path
							prev_path = "2"
							geometric_path = "quit"
							break

						#path options
						"""
						1 - Two Side Lengths and One Angle (across from one of the sides)
						2 - Two Angle Measures and One Side Length (across from one of the angles)

						"""

						if triangle_sine_law_input == "1": #Two Side Lengths, One Angle
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								current_triangle_path_option1 = "Enter the measure of side a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_a = float(input("Enter the measure of side a: "))
								current_triangle_path_option1 = "Enter the measure of angle a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_angle_a = float(input("Enter the measure of angle a: "))
								current_triangle_path_option1 = "Enter the measure of side b: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_b = float(input("Enter the measure of side b: "))
								triangle_angle_b = math.degrees(math.asin(((triangle_side_b) * math.sin(math.radians(triangle_angle_a))) / triangle_side_a)) #uses trigonometry functions to solve for values
								triangle_side_c = ((triangle_side_b) * math.sin(math.radians(180 - (triangle_angle_a + triangle_angle_b)))) / math.sin(math.radians(triangle_angle_b)) #uses trigonometry functions to solve for values
								triangle_angle_c = 180 - (triangle_angle_a + triangle_angle_b) #uses trigonometry functions to solve for values

								triangle_side_a = round_answer(triangle_side_a) #rounding answers
								triangle_side_b = round_answer(triangle_side_b)
								triangle_side_c = round_answer(triangle_side_c)
								triangle_angle_a = round_answer(triangle_angle_a)
								triangle_angle_b = round_answer(triangle_angle_b)
								triangle_angle_c = round_answer(triangle_angle_c)

								geometric_triangle_answer_screen(background_foreground_color,triangle_side_a,triangle_side_b,triangle_side_c,triangle_angle_a,triangle_angle_b,triangle_angle_c) #prints answer to screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif triangle_sine_law_input == "2": #Two Angles, One Side Length
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								current_triangle_path_option1 = "Enter the measure of angle a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_angle_a = float(input("Enter the measure of angle a: "))
								current_triangle_path_option1 = "Enter the measure of side a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_a = float(input("Enter the measure of side a: "))
								current_triangle_path_option1 = "Enter the measure of angle b: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_angle_b = float(input("Enter the measure of angle b: "))
								triangle_side_b = ((triangle_side_a) * math.sin(math.radians(triangle_angle_b))) / math.sin(math.radians(triangle_angle_a)) #uses trigonometry functions to solve for values
								triangle_angle_c = 180 - (triangle_angle_a + triangle_angle_b) #uses trigonometry functions to solve for values
								triangle_side_c = ((triangle_side_b) * math.sin(math.radians(triangle_angle_c))) / math.sin(math.radians(triangle_angle_b)) #uses trigonometry functions to solve for values

								triangle_side_a = round_answer(triangle_side_a) #rounding answers
								triangle_side_b = round_answer(triangle_side_b)
								triangle_side_c = round_answer(triangle_side_c)
								triangle_angle_a = round_answer(triangle_angle_a)
								triangle_angle_b = round_answer(triangle_angle_b)
								triangle_angle_c = round_answer(triangle_angle_c)

								geometric_triangle_answer_screen(background_foreground_color,triangle_side_a,triangle_side_b,triangle_side_c,triangle_angle_a,triangle_angle_b,triangle_angle_c) #prints answer to screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif triangle_sine_law_input != "1" or triangle_sine_law_input != "2" or triangle_sine_law_input != "back" or triangle_sine_law_input != "switch" or triangle_sine_law_input != "quit": #False Input
							print("bad input")
					
					elif type_of_triangle_input == "2": #Law Of Cosines
						turtle_title = "Geometric Calculator: Law Of Cosines"
						current_triangle_path = "Law Of Cosines"
						current_triangle_path_option1 = "[1] Two Side Lengths, One Angle Inbetween\nThe Two Side Lengths\n(Example: Side A, Side B, Angle C)"
						current_triangle_path_option2 = "[2] All Three Side Lengths Of The Triangle\n(Example: Side A, Side B, Side C)"
						geometric_triangle_pathinpath_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1,current_triangle_path_option2)
						title_for_mode(turtle_title, background_foreground_color)
						triangle_cosine_law_input = input("(Cosine Law)Choose your path depending on which values you have with the corresponding number: ")
						triangle_cosine_law_input = format_input(triangle_cosine_law_input)

						if triangle_cosine_law_input == "back":
							geometric_path = "undefined"
							break

						if triangle_cosine_law_input == "quit":
							geometric_path = "quit"
							path = "undefined"
							break
							
						if triangle_cosine_law_input == "switch":
							path = prev_path
							prev_path = "2"
							geometric_path = "quit"
							break


						"""
						1 - Two Side Lengths and Angle (angle between sides)
						2 - Three Side Lengths

						"""

						if triangle_cosine_law_input == "1": #Two Side Lengths, One Angle Inbetween
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								current_triangle_path_option1 = "Enter the measure of side a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_a = float(input("Enter the measure of side a: "))
								current_triangle_path_option1 = "Enter the measure of side b: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_b = float(input("Enter the measure of side b: "))
								current_triangle_path_option1 = "Enter the measure of side c: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_angle_c = float(input("Enter the measure of angle c: "))
								triangle_side_c = math.sqrt((triangle_side_a**2 + triangle_side_b**2 - 2 * triangle_side_a * triangle_side_b * math.cos(math.radians(triangle_angle_c)))) #uses trigonometry functions to solve for values
								triangle_angle_b = math.degrees(math.asin(((triangle_side_b) * math.sin(math.radians(triangle_angle_c))) / triangle_side_c)) #uses trigonometry functions to solve for values
								triangle_angle_a = 180 - (triangle_angle_b + triangle_angle_c) #uses trigonometry functions to solve for values

								triangle_side_a = round_answer(triangle_side_a) #rounding answers
								triangle_side_b = round_answer(triangle_side_b)
								triangle_side_c = round_answer(triangle_side_c)
								triangle_angle_a = round_answer(triangle_angle_a)
								triangle_angle_b = round_answer(triangle_angle_b)
								triangle_angle_c = round_answer(triangle_angle_c)

								geometric_triangle_answer_screen(background_foreground_color,triangle_side_a,triangle_side_b,triangle_side_c,triangle_angle_a,triangle_angle_b,triangle_angle_c) #prints answer to screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif triangle_cosine_law_input == "2": #Three Side Lengths
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								current_triangle_path_option1 = "Enter the measure of side a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_a = float(input("Enter the measure of side a: "))
								current_triangle_path_option1 = "Enter the measure of side b: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_b = float(input("Enter the measure of side b: "))
								current_triangle_path_option1 = "Enter the measure of side c: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_c = float(input("Enter the measure of side c: "))
								triangle_angle_a = math.degrees(math.acos(((triangle_side_b**2 + triangle_side_c**2 - triangle_side_a**2) / (2 * triangle_side_b * triangle_side_c)))) #uses trigonometry functions to solve for values
								triangle_angle_b = math.degrees(math.acos(((triangle_side_c**2 + triangle_side_a**2 - triangle_side_b**2) / (2 * triangle_side_c * triangle_side_a)))) #uses trigonometry functions to solve for values
								triangle_angle_c = math.degrees(math.acos(((triangle_side_a**2 + triangle_side_b**2 - triangle_side_c**2) / (2 * triangle_side_a * triangle_side_b)))) #uses trigonometry functions to solve for values

								triangle_side_a = round_answer(triangle_side_a) #rounding answers
								triangle_side_b = round_answer(triangle_side_b)
								triangle_side_c = round_answer(triangle_side_c)
								triangle_angle_a = round_answer(triangle_angle_a)
								triangle_angle_b = round_answer(triangle_angle_b)
								triangle_angle_c = round_answer(triangle_angle_c)
								
								geometric_triangle_answer_screen(background_foreground_color,triangle_side_a,triangle_side_b,triangle_side_c,triangle_angle_a,triangle_angle_b,triangle_angle_c) #prints answer to screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif triangle_cosine_law_input != "1" or triangle_cosine_law_input != "2" or triangle_cosine_law_input != "back" or triangle_cosine_law_input != "switch" or triangle_cosine_law_input != "quit": #False Input
							print("bad input")

					elif type_of_triangle_input == "3": #Pythagorean Theorem: Two Side Lengths, One Side Length and Hypotenuse Length
						turtle_title = "Geometric Calculator: Pythagorean Theorem"
						current_triangle_path = "Pythagorean Theorem"
						current_triangle_path_option1 = "[1] Two Side Lengths, Neither Of Which Are\nThe Hypotenuse (Side C)\n(Example: Side A, Side B)"
						current_triangle_path_option2 = "[2] One Side Length, And The Hypotenuse\n(Side C)\n(Example: Side A or Side B, Side C)"
						geometric_triangle_pathinpath_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1,current_triangle_path_option2)
						title_for_mode(turtle_title, background_foreground_color)
						triangle_pythagorean_input = input("(Pythagorean) Choose your path depending on which values you have with the corresponding number: ")
						triangle_pythagorean_input = format_input(triangle_pythagorean_input)

						if triangle_pythagorean_input == "back":
							geometric_path = "undefined"
							break

						if triangle_pythagorean_input == "quit":
							geometric_path = "quit"
							path = "undefined"
							break
							
						if triangle_pythagorean_input == "switch":
							path = prev_path
							prev_path = "2"
							geometric_path = "quit"
							break

						"""
						1 - Two Side Lengths
						2 - A Side Length and the Hypotenuse Length

						"""

						if triangle_pythagorean_input == "1": #Two Side Lengths
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								current_triangle_path_option1 = "Enter the measure of side a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_a = float(input("Enter the measure of side a: "))
								current_triangle_path_option1 = "Enter the measure of side b: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_b = float(input("Enter the measure of side b: "))
								triangle_angle_c = 90.0
								triangle_side_c = math.sqrt(triangle_side_a**2 + triangle_side_b**2) #uses trigonometry functions to solve for values
								triangle_angle_a = math.degrees(math.asin(((triangle_side_a) * math.sin(math.radians(triangle_angle_c))) / triangle_side_c)) #uses trigonometry functions to solve for values
								triangle_angle_b = 180 - (triangle_angle_a + triangle_angle_c) #uses trigonometry functions to solve for values

								triangle_side_a = round_answer(triangle_side_a) #rounding answers
								triangle_side_b = round_answer(triangle_side_b)
								triangle_side_c = round_answer(triangle_side_c)
								triangle_angle_a = round_answer(triangle_angle_a)
								triangle_angle_b = round_answer(triangle_angle_b)
								triangle_angle_c = round_answer(triangle_angle_c)

								geometric_triangle_answer_screen(background_foreground_color,triangle_side_a,triangle_side_b,triangle_side_c,triangle_angle_a,triangle_angle_b,triangle_angle_c) #prints answer to screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif triangle_pythagorean_input == "2": #A Side Length and the Hypotenuse
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								current_triangle_path_option1 = "Enter the measure of side a: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_a = float(input("Enter the measure of side a: "))
								current_triangle_path_option1 = "Enter the measure of side c: "
								geometric_triangle_input_screen(background_foreground_color,current_triangle_path,current_triangle_path_option1)
								triangle_side_c = float(input("Enter the measure of side c: "))
								triangle_angle_c = 90.0 
								triangle_side_b = math.sqrt(triangle_side_c**2 - triangle_side_a**2) #uses trigonometry functions to solve for values
								triangle_angle_a = math.degrees(math.asin(((triangle_side_a) * math.sin(math.radians(triangle_angle_c))) / triangle_side_c)) #uses trigonometry functions to solve for values
								triangle_angle_b = 180 - (triangle_angle_a + triangle_angle_c) #uses trigonometry functions to solve for values

								triangle_side_a = round_answer(triangle_side_a) #rounding answers
								triangle_side_b = round_answer(triangle_side_b)
								triangle_side_c = round_answer(triangle_side_c)
								triangle_angle_a = round_answer(triangle_angle_a)
								triangle_angle_b = round_answer(triangle_angle_b)
								triangle_angle_c = round_answer(triangle_angle_c)

								geometric_triangle_answer_screen(background_foreground_color,triangle_side_a,triangle_side_b,triangle_side_c,triangle_angle_a,triangle_angle_b,triangle_angle_c) #prints answer to screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif triangle_pythagorean_input != "1" or triangle_pythagorean_input != "2" or triangle_pythagorean_input != "back" or triangle_pythagorean_input != "switch" or triangle_pythagorean_input != "quit": #False Input
							print("bad input")

					elif type_of_triangle_input != "1" or type_of_triangle_input != "2" or type_of_triangle_input != "3":
						print("bad input")

			elif geometric_path == "3": #Regular Polygon Solver: Interior Angle, Exterior Angle, Central Angle, Number Of Sides
				polygon_solver = True #begins the polygon solver process
				polygon_measure_input = False #needs to be defined for future use
				geometric_polygon_angle_measure_screen(background_foreground_color) #draws screen for input
				while polygon_solver == True: #loops text within the while loop
					turtle_title = "Geometric Calculator: Polygon Solver" #title
					title_for_mode(turtle_title, background_foreground_color) #draw title
					polygon_side_or_angle_input = input("(Polygon Solver) Choose your path depending on which values you have with the corresponding number: ") #user input for path
					polygon_side_or_angle_input = format_input(polygon_side_or_angle_input) #formatting user input

					if polygon_side_or_angle_input == "back": #back out of mode
						geometric_path = "undefined"
						polygon_solver = False
						break

					if polygon_side_or_angle_input == "quit": #back out of mode
						geometric_path = "quit"
						path = "undefined"
						polygon_solver = False
						break
						
					if polygon_side_or_angle_input == "switch": #switch out of mode
						path = prev_path
						prev_path = "2"
						geometric_path = "quit"
						polygon_solver = False
						break

					"""
					1 - Interior Angle
					2 - Exterior Angle
					3 - Central Angle
					4 - Number Of Sides

					"""

					if polygon_side_or_angle_input == "1": #Interior Angle
						current_polygon_path = "the interior angle" #define path for screen
						geometric_polygon_angle_input_screen(background_foreground_color,current_polygon_path) #draws input screen
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely	
							polygon_interior_angle = float(input("Enter the value of the interior angle: "))
							polygon_exterior_angle = 180 - polygon_interior_angle #uses the rules of polygons to solve other values
							polygon_number_of_sides = 360 / polygon_exterior_angle
							polygon_central_angle = 360 / polygon_number_of_sides

							polygon_interior_angle = round_answer(polygon_interior_angle) #rounds values
							polygon_exterior_angle = round_answer(polygon_exterior_angle)
							polygon_central_angle = round_answer(polygon_central_angle)
							polygon_number_of_sides = round_answer(polygon_number_of_sides)

							if (polygon_number_of_sides).is_integer() == False or polygon_number_of_sides <= 2: #checks to make sure polygon is actually drawabale, not 2d or irregular ect.
								print("Error with entered values; check input and try again.")
							else:
								polygon_number_of_sides = int(polygon_number_of_sides) #converts number of sides to integer for later use
								polygon_measure_input = True #begins the solving with actual measures process

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif polygon_side_or_angle_input == "2": #Exterior Angle
						current_polygon_path = "the exterior angle"				
						geometric_polygon_angle_input_screen(background_foreground_color,current_polygon_path)
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely	
							polygon_exterior_angle = float(input("Enter the value of the exterior angle: "))
							polygon_interior_angle = 180 - polygon_exterior_angle #uses the rules of polygons to solve other values
							polygon_number_of_sides = 360 / polygon_exterior_angle
							polygon_central_angle = 360 / polygon_number_of_sides

							polygon_interior_angle = round_answer(polygon_interior_angle) #rounds values
							polygon_exterior_angle = round_answer(polygon_exterior_angle)
							polygon_central_angle = round_answer(polygon_central_angle)
							polygon_number_of_sides = round_answer(polygon_number_of_sides)

							if (polygon_number_of_sides).is_integer() == False or polygon_number_of_sides <= 2: #checks to make sure polygon is actually drawabale, not 2d or irregular ect.
								print("Error with entered values; check input and try again.")
							else:
								polygon_number_of_sides = int(polygon_number_of_sides) #converts number of sides to integer for later use
								polygon_measure_input = True #begins the solving with actual measures process

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif polygon_side_or_angle_input == "3": #Central Angle
						current_polygon_path = "the central angle"		
						geometric_polygon_angle_input_screen(background_foreground_color,current_polygon_path)
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							polygon_central_angle = float(input("Enter the value of the central angle: "))
							polygon_number_of_sides = 360 / polygon_central_angle #uses the rules of polygons to solve other values
							polygon_exterior_angle = 360 / polygon_number_of_sides
							polygon_interior_angle = 180 - polygon_exterior_angle

							polygon_interior_angle = round_answer(polygon_interior_angle) #rounds values
							polygon_exterior_angle = round_answer(polygon_exterior_angle)
							polygon_central_angle = round_answer(polygon_central_angle)
							polygon_number_of_sides = round_answer(polygon_number_of_sides)

							if (polygon_number_of_sides).is_integer() == False or polygon_number_of_sides <= 2: #checks to make sure polygon is actually drawabale, not 2d or irregular ect.
								print("Error with entered values; check input and try again.")
							else:
								polygon_number_of_sides = int(polygon_number_of_sides) #converts number of sides to integer for later use
								polygon_measure_input = True #begins the solving with actual measures process

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					elif polygon_side_or_angle_input == "4": #Number Of Sides
						current_polygon_path = "the number of sides"
						geometric_polygon_angle_input_screen(background_foreground_color,current_polygon_path)
						try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
							polygon_number_of_sides = float(input("Enter the number of sides: "))
							polygon_central_angle = 360 / polygon_number_of_sides #uses the rules of polygons to solve other values
							polygon_exterior_angle = 360 / polygon_number_of_sides
							polygon_interior_angle = 180 - polygon_exterior_angle

							polygon_interior_angle = round_answer(polygon_interior_angle) #rounds values
							polygon_exterior_angle = round_answer(polygon_exterior_angle)
							polygon_central_angle = round_answer(polygon_central_angle)
							polygon_number_of_sides = round_answer(polygon_number_of_sides)

							if (polygon_number_of_sides).is_integer() == False or polygon_number_of_sides <= 2: #checks to make sure polygon is actually drawabale, not 2d or irregular ect.
								print("Error with entered values; check input and try again.")
							else:
								polygon_number_of_sides = int(polygon_number_of_sides) #converts number of sides to integer for later use
								polygon_measure_input = True #begins the solving with actual measures process

						except SyntaxError: #error handling
							print("syntax error")
						except NameError: #error handling
							print("name error")
						except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
							print("unknown error")

					if polygon_measure_input == True: #Polygon Measure Solver: Apothem, Radius, Area
						geometric_polygon_measure_choice_screen(background_foreground_color) #draws path screen
						polygon_measure_input = input("(Polygon Solver) Choose your path depending on which values you have with the corresponding number: ") #user input on path
						polygon_measure_input = format_input(polygon_measure_input) 

						if polygon_measure_input == "back": #exiting out of mode
							geometric_path = "undefined"
							polygon_solver = False
							break

						if polygon_measure_input == "quit": #exiting out of mode
							geometric_path = "quit"
							path = "undefined"
							polygon_solver = False
							break
							
						if polygon_measure_input == "switch": #switching out of mode
							path = prev_path
							prev_path = "2"
							geometric_path = "quit"
							polygon_solver = False
							break

						#possible path options
						"""
						1 - Apothem (and Side Length, Perimeter or Area )
						2 - Radius
						3 - Area (and Side Length, Perimeter or Apothem)

						"""

						if polygon_measure_input == "1": #Apothem + Side Length, Perimeter, Area
							current_polygon_path = "the apothem" #defines current path
							geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								polygon_apothem_length = float(input("Enter the value of the apothem: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")
							polygon_choice_1 = "Side Length" #defines possible options for path
							polygon_choice_2 = "Perimeter"
							polygon_choice_3 = "Area"
							geometric_polygon_measure_choice_in_choice_screen(background_foreground_color,polygon_choice_1,polygon_choice_2,polygon_choice_3) #lists possible options by drawing on screen
							polygon_apothem_choice = input("Choose your path depending on which values you have with the corresponding number:") #user input for path
							polygon_apothem_choice = format_input(polygon_apothem_choice) #formatting input

							#possible path options
							"""
							1 - Side Length
							2 - Perimeter
							3 - Area

							"""

							if polygon_apothem_choice == "1": #Apothem + Side Length
								current_polygon_path = "the side length" #defines current path
								geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
								try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
									polygon_side_length = float(input("Enter the value of a side length: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
									polygon_perimeter_length = polygon_side_length * polygon_number_of_sides #solves for values of other measures using polygon formulas
									polygon_area_measure = (polygon_perimeter_length * polygon_apothem_length) / 2
									polygon_triangle_area = polygon_area_measure / polygon_number_of_sides
									polygon_radius_length = math.sqrt(((polygon_side_length / 2)**2 + polygon_apothem_length**2))

									polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
									polygon_apothem_length = round_answer(polygon_apothem_length)
									polygon_side_length = round_answer(polygon_side_length)
									polygon_perimeter_length = round_answer(polygon_perimeter_length)
									polygon_area_measure = round_answer(polygon_area_measure)
									polygon_triangle_area = round_answer(polygon_triangle_area)

									geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen

								except SyntaxError: #error handling
									print("syntax error")
								except NameError: #error handling
									print("name error")
								except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
									print("unknown error")

							elif polygon_apothem_choice == "2": #Apothem + Perimeter
								current_polygon_path = "the perimeter" #defines current path
								geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
								try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
									polygon_perimeter_length = float(input("Enter the value of the perimeter: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
									polygon_side_length = polygon_perimeter_length / polygon_number_of_sides #solves for values of other measures using polygon formulas
									polygon_area_measure = (polygon_perimeter_length * polygon_apothem_length) / 2
									polygon_triangle_area = polygon_area_measure / polygon_number_of_sides
									polygon_radius_length = math.sqrt(((polygon_side_length / 2)**2 + polygon_apothem_length**2))

									polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
									polygon_apothem_length = round_answer(polygon_apothem_length)
									polygon_side_length = round_answer(polygon_side_length)
									polygon_perimeter_length = round_answer(polygon_perimeter_length)
									polygon_area_measure = round_answer(polygon_area_measure)
									polygon_triangle_area = round_answer(polygon_triangle_area)

									geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen

								except SyntaxError: #error handling
									print("syntax error")
								except NameError: #error handling
									print("name error")
								except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
									print("unknown error")

							elif polygon_apothem_choice == "3": #Apothem + Area
								current_polygon_path = "the area" #defines current path
								geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
								try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
									polygon_area_measure = float(input("Enter the value of the area: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
									polygon_perimeter_length = (2 * polygon_area_measure) / polygon_apothem_length #solves for values of other measures using polygon formulas
									polygon_side_length = polygon_perimeter_length / polygon_number_of_sides
									polygon_radius_length = math.sqrt(((polygon_side_length / 2)**2 + polygon_apothem_length**2))
									polygon_triangle_area = polygon_area_measure / polygon_number_of_sides

									polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
									polygon_apothem_length = round_answer(polygon_apothem_length)
									polygon_side_length = round_answer(polygon_side_length)
									polygon_perimeter_length = round_answer(polygon_perimeter_length)
									polygon_area_measure = round_answer(polygon_area_measure)
									polygon_triangle_area = round_answer(polygon_triangle_area)

									geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen

								except SyntaxError: #error handling
									print("syntax error")
								except NameError: #error handling
									print("name error")
								except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
									print("unknown error")

							elif polygon_apothem_choice != "1" or polygon_apothem_choice != "2" or polygon_apothem_choice != "3":
								print("bad input")

						elif polygon_measure_input == "2": #Radius of Polygon
							current_polygon_path = "the radius" #defines current path
							geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								polygon_radius_length = float(input("Enter the value of the radius: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
								polygon_side_length = math.sqrt((polygon_radius_length**2 + polygon_radius_length**2 - 2 * polygon_radius_length * polygon_radius_length * math.cos(math.radians(polygon_central_angle)))) #solves for values of other measures using polygon formulas
								polygon_perimeter_length = polygon_side_length * polygon_number_of_sides
								polygon_apothem_length = math.sqrt(polygon_radius_length**2 - (polygon_side_length / 2)**2)
								polygon_area_measure = (polygon_perimeter_length * polygon_apothem_length) / 2
								polygon_triangle_area = polygon_area_measure / polygon_number_of_sides

								polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
								polygon_apothem_length = round_answer(polygon_apothem_length)
								polygon_side_length = round_answer(polygon_side_length)
								polygon_perimeter_length = round_answer(polygon_perimeter_length)
								polygon_area_measure = round_answer(polygon_area_measure)
								polygon_triangle_area = round_answer(polygon_triangle_area)

								geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen

							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")

						elif polygon_measure_input == "3": #Area + Side Length, Perimeter, Apothem
							current_polygon_path = "the area" #defines current path
							geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
							try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
								polygon_area_measure = float(input("Enter the value of the area: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
							except SyntaxError: #error handling
								print("syntax error")
							except NameError: #error handling
								print("name error")
							except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
								print("unknown error")
							polygon_choice_1 = "Side Length"
							polygon_choice_2 = "Perimeter"
							polygon_choice_3 = "Apothem"
							geometric_polygon_measure_choice_in_choice_screen(background_foreground_color,polygon_choice_1,polygon_choice_2,polygon_choice_3) #draws possible choices on screen
							polygon_area_choice = input("Choose your path depending on which values you have with the corresponding number: ")
							polygon_area_choice = format_input(polygon_area_choice)

							"""
							1 - Side Length
							2 - Perimeter
							3 - Apothem

							"""

							if polygon_area_choice == "1": #Area + Side Length
								current_polygon_path = "the side length" #defines current path
								geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
								try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
									polygon_side_length = float(input("Enter the value of the side length: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
									polygon_perimeter_length = polygon_side_length * polygon_number_of_sides #solves for values of other measures using polygon formulas
									polygon_apothem_length = (2 * polygon_area_measure) / polygon_perimeter_length
									polygon_radius_length = math.sqrt(((polygon_side_length / 2)**2 + polygon_apothem_length**2))
									polygon_triangle_area = polygon_area_measure / polygon_number_of_sides

									polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
									polygon_apothem_length = round_answer(polygon_apothem_length)
									polygon_side_length = round_answer(polygon_side_length)
									polygon_perimeter_length = round_answer(polygon_perimeter_length)
									polygon_area_measure = round_answer(polygon_area_measure)
									polygon_triangle_area = round_answer(polygon_triangle_area)

									geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen
								
								except SyntaxError: #error handling
									print("syntax error")
								except NameError: #error handling
									print("name error")
								except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
									print("unknown error")

							elif polygon_area_choice == "2": #Area + Perimeter
								current_polygon_path = "the perimeter" #defines current path
								geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
								try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
									polygon_perimeter_length = float(input("Enter the value of the perimeter: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
									polygon_side_length = polygon_perimeter_length / polygon_number_of_sides #solves for values of other measures using polygon formulas
									polygon_apothem_length = (2 * polygon_area_measure) / polygon_perimeter_length
									polygon_radius_length = math.sqrt(((polygon_side_length / 2)**2 + polygon_apothem_length**2))
									polygon_triangle_area = polygon_area_measure / polygon_number_of_sides

									polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
									polygon_apothem_length = round_answer(polygon_apothem_length)
									polygon_side_length = round_answer(polygon_side_length)
									polygon_perimeter_length = round_answer(polygon_perimeter_length)
									polygon_area_measure = round_answer(polygon_area_measure)
									polygon_triangle_area = round_answer(polygon_triangle_area)

									geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen

								except SyntaxError: #error handling
									print("syntax error")
								except NameError: #error handling
									print("name error")
								except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
									print("unknown error")

							elif polygon_area_choice == "3": #Area + Apothem
								current_polygon_path = "the apothem" #defines current path
								geometric_polygon_angle_input_screen(background_foreground_color, current_polygon_path) #draws input screen
								try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
									polygon_apothem_length = float(input("Enter the value of the apothem: ")) #asks for float value of a value, if another value is entered that isnt a float, errors are handled
									polygon_perimeter_length = (2 * polygon_area_measure) / polygon_apothem_length #solves for values of other measures using polygon formulas
									polygon_side_length = polygon_perimeter_length / polygon_number_of_sides
									polygon_radius_length = math.sqrt(((polygon_side_length / 2)**2 + polygon_apothem_length**2))
									polygon_triangle_area = polygon_area_measure / polygon_number_of_sides

									polygon_radius_length = round_answer(polygon_radius_length) #rounding answers
									polygon_apothem_length = round_answer(polygon_apothem_length)
									polygon_side_length = round_answer(polygon_side_length)
									polygon_perimeter_length = round_answer(polygon_perimeter_length)
									polygon_area_measure = round_answer(polygon_area_measure)
									polygon_triangle_area = round_answer(polygon_triangle_area)

									geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen

								except SyntaxError: #error handling
									print("syntax error")
								except NameError: #error handling
									print("name error")
								except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
									print("unknown error")

							elif polygon_area_choice != "1" or polygon_area_choice != "2" or polygon_area_choice != "3" or polygon_area_choice != "back" or polygon_area_choice != "switch" or polygon_area_choice != "quit": #specifies why the user's input was incorrect
								print("bad input")

						elif polygon_measure_input == "4":
								#print the values of the angles
								polygon_radius_length = "not entered" #defines values as undefined because user chose to skip over them
								polygon_apothem_length = "not entered"
								polygon_side_length = "not entered"
								polygon_perimeter_length = "not entered"
								polygon_area_measure = "not entered"
								polygon_triangle_area = "not entered"

								geometric_polygon_get_measures(background_foreground_color, polygon_number_of_sides,polygon_central_angle) #draws answers on screen


					elif polygon_side_or_angle_input != "1" or polygon_side_or_angle_input != "2" or polygon_side_or_angle_input != "3" or polygon_side_or_angle_input != "4" or polygon_side_or_angle_input != "back" or polygon_side_or_angle_input != "switch" or polygon_side_or_angle_input != "quit" or polygon_side_or_angle_input != True: #specifies why the user's input was incorrect
						print("bad input")
						geometric_path = "undefined"
						polygon_solver = False
						break

	#Graphing Calculator
	if path == "3": #Slope Graphing, Distance Between Points
		graphing_calc = True #begins the graphing process
		graphing_path = "undefined" #maks it so user input is required the first time
		while graphing_calc == True: #loops code with
			if graphing_path == "undefined":
				turtle_title = "Graphing Calculator: Main Menu" #title for screen
				title_for_mode(turtle_title, background_foreground_color) #draws title on screen
				graphing_main_menu(background_foreground_color) #draws paths for graphing mode
				graphing_path = input("(Graphing Calculator) Choose your path with the corresponding number: ") #asks for user input on path
				graphing_path = format_input(graphing_path) #formatting

			if graphing_path == "back" or graphing_path == "quit": #allows user to exit out of mode
				path = "undefined"
				prev_path = "3"
				break
			if graphing_path == "switch": #allows user to exit out of mode
				path = prev_path
				prev_path = "3"
				break

			#possible path options
			"""
			1 - Point Graphing
			2 - Slope Graphing
			3 - Distance Between Points

			"""

			if graphing_path == "1": #Graphing A Point
				graphing_a_point = True #begins graphing a point process
				current_graphing_path = "a point in x,y format" #defines the current path for screen
				graphing_input_screen(background_foreground_color,current_graphing_path) #draws the input screen for current path
				while graphing_a_point == True: #loops code within
					turtle_title = "Graphing Calculator: Graphing A Point" #title for mode
					title_for_mode(turtle_title, background_foreground_color) #draws title for mode
					point_on_graph1 = input("Enter the value of the point in x,y format: ") #asks for input in x,y format

					if point_on_graph1 == "back": #exiting mode
						graphing_path = "undefined"
						graphing_a_point = False
						break

					if point_on_graph1 == "quit": #exiting mode
						graphing_path = "quit"
						path = "undefined"
						graphing_a_point = False
						break
						
					if point_on_graph1 == "switch": #switching mode
						path = prev_path
						prev_path = "2"
						graphing_path = "quit"
						graphing_a_point = False
						break

					try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
						graphing_x_value_1 = point_on_graph1[:point_on_graph1.find(",")] #splits point into x and y coordinates
						graphing_y_value_1 = point_on_graph1[point_on_graph1.find(",")+1:]
						graphing_x_value_1 = float(graphing_x_value_1) #converts x ad y coordinates to float
						graphing_y_value_1 = float(graphing_y_value_1)

						graphing_point_on_graph(background_foreground_color, graphing_x_value_1,graphing_y_value_1) #draws the point on the screen
					except SyntaxError: #error handling
						print("syntax error")
					except NameError: #error handling
						print("name error")
					except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
						print("unknown error")
			
			elif graphing_path == "2": #Slope Graphing
				graphing_a_slope = True #begins the slope graphing process
				current_graphing_path = "a slope in y = mx + b format" #defines current path for drawing
				graphing_input_screen(background_foreground_color,current_graphing_path) #draws input screen
				while graphing_a_slope == True: #loops code within loop
					try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
						turtle_title = "Graphing Calculator: Graphing A Slope" #title for mode
						title_for_mode(turtle_title, background_foreground_color) #draws title on screen
						slope_equation = input("Enter the equation for the line in y = mx + b form: ") #asks user for input of line
						slope_equation = format_input(slope_equation) #formats input

						if slope_equation == "back": #exiting mode
							graphing_path = "undefined"
							graphing_a_slope = False
							break

						if slope_equation == "quit": #exiting mode
							graphing_path = "quit"
							path = "undefined"
							graphing_a_slope = False
							break
							
						if slope_equation == "switch": #switching mode
							path = prev_path
							prev_path = "2"
							graphing_path = "quit"
							graphing_a_slope = False
							break

						slope_value = slope_equation[slope_equation.find("=")+1:slope_equation.find("x")] #finds the slope value by checking all numbers in between the '=' and 'x'
						
						if slope_equation[slope_equation.find("=")+1] == "x": #sets the slope to 1 if x has no coefficient
							slope_value = "1"

						possible_y_intercept = slope_equation[slope_equation.find("x"):] #splits off remaining equation into possible y intercept, if there is one

						if possible_y_intercept.find("+") != -1: #looks for '+' and calculates y intercept with the values following the + 
							y_intercept_value = possible_y_intercept[possible_y_intercept.find("x")+2:]
						elif possible_y_intercept.find("-") != -1: #looks for '-' and calculates y intercept with the values following the -
							y_intercept_value = possible_y_intercept[possible_y_intercept.find("x")+1:]
						else:
							y_intercept_value = "0" #if there is no + or - then the y intercept is set to 0
				
						slope_value = eval(slope_value) #evaluates the slope to convert it to a number 
						y_intercept_value = eval(y_intercept_value) #evaluates the slope to convert it to a number 

						if y_intercept_value == "back": #exiting mode
							graphing_path = "undefined" 
							graphing_a_slope = False
							break

						if y_intercept_value == "quit": #exiting mode
							graphing_path = "quit"
							path = "undefined"
							graphing_a_slope = False
							break
							
						if y_intercept_value == "switch": #switching mode
							path = prev_path
							prev_path = "2"
							graphing_path = "quit"
							graphing_a_slope = False
							break

						graphing_x_value_1 = float("-5") #gets 5 points for the line, however after reworking this process i've realized that only 2 points are needed
						graphing_y_value_1 = (float(slope_value) * -5)
						graphing_x_value_2 = float("-3")
						graphing_y_value_2 = (float(slope_value) * -3)
						graphing_x_value_3 = float("0")
						graphing_y_value_3 = y_intercept_value
						graphing_x_value_4 = float("3")
						graphing_y_value_4 = (float(slope_value) * 3)
						graphing_x_value_5 = float("5")
						graphing_y_value_5 = (float(slope_value) * 5)

						graphing_slope_on_graph(background_foreground_color,slope_equation,y_intercept_value,graphing_x_value_5,graphing_y_value_5,graphing_x_value_1,graphing_y_value_1)

					except SyntaxError: #error handling
						print("syntax error")
					except NameError: #error handling
						print("name error")
					except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
						print("unknown error")

			elif graphing_path == "3": #Distance Between Points
				distance_between_point = True #begins distance between points process
				current_graphing_path = "a point in x,y format" #defines current path
				graphing_input_screen(background_foreground_color,current_graphing_path) #draws input screen
				while distance_between_point == True: #loops code within
					try: #tries following code, when faced with errors, if the error type is specified below, it ignores and resumes program, rather than stopping entirely
						turtle_title = "Graphing Calculator: Distance Between Points" #title of mode
						title_for_mode(turtle_title, background_foreground_color) #draws title of mode
						point_on_graph1 = input("Enter the value of the point in x,y format: ") #asks the user for input in the form of x,y
						point_on_graph1 = format_input(point_on_graph1) #formatting

						if point_on_graph1 == "back": #exiting mode
							graphing_path = "undefined"
							distance_between_point = False
							break

						if point_on_graph1 == "quit": #exiting mode
							graphing_path = "quit"
							path = "undefined"
							distance_between_point = False
							break
							
						if point_on_graph1 == "switch": #switching mode
							path = prev_path
							prev_path = "2"
							graphing_path = "quit"
							distance_between_point = False
							break

						current_graphing_path = "another point in x,y format" #defines graphing path
						graphing_input_screen(background_foreground_color,current_graphing_path) #draws the current graphing path
						point_on_graph2 = input("Enter the value of the point in x,y format: ") #asks for anoher point on the graph
						point_on_graph2 = format_input(point_on_graph2) #formatting

						if point_on_graph2 == "back": #exiting mode
							graphing_path = "undefined"
							break

						if point_on_graph2 == "quit": #exiting mode
							graphing_path = "quit"
							path = "undefined"
							break
							
						if point_on_graph2 == "switch": #exiting mode
							path = prev_path
							prev_path = "2"
							graphing_path = "quit"
							break

						graphing_x_value_1 = point_on_graph1[:point_on_graph1.find(",")] #splits both points into x,y coordinates
						graphing_y_value_1 = point_on_graph1[point_on_graph1.find(",")+1:]
						graphing_x_value_2 = point_on_graph2[:point_on_graph2.find(",")]
						graphing_y_value_2 = point_on_graph2[point_on_graph2.find(",")+1:]

						distance_between_points = math.sqrt(abs(eval(graphing_x_value_1 + "-" + graphing_x_value_2)**2 + eval(graphing_y_value_1 + "-" + graphing_y_value_2)**2)) #using the distance formula it finds the distance between points
						distance_between_points = round_answer(distance_between_points) #rounds the answer

						graphing_x_value_1 = float(point_on_graph1[:point_on_graph1.find(",")]) #converts all points to float values
						graphing_y_value_1 = float(point_on_graph1[point_on_graph1.find(",")+1:])
						graphing_x_value_2 = float(point_on_graph2[:point_on_graph2.find(",")])
						graphing_y_value_2 = float(point_on_graph2[point_on_graph2.find(",")+1:])

						graphing_distance_point_on_graph(background_foreground_color,graphing_x_value_1,graphing_y_value_1,graphing_x_value_2,graphing_y_value_2,distance_between_points) #draws the points on screen

					except SyntaxError: #error handling
						print("syntax error")
					except NameError: #error handling
						print("name error")
					except: #if none of the error types above are the issue, it accepts all other errors and prints 'unknown error'
						print("unknown error")

	#Color Settings
	if path == "4": #Default Color Changing, Light/Dark Mode
		settings = True #begins the settings process
		while settings == True: #loops code within
			turtle_title = "Settings: Color Scheme" #defines title of mode
			title_for_mode(turtle_title, background_foreground_color) #draws the title of the mode
			settings_screen(background_foreground_color) #draws the settings screen
			setting_path = input("Change color settings?: ") #asks user for input on color settings
			setting_path = format_input(setting_path) #formatting
			
			if setting_path == "back" or setting_path == "quit": #exiting mode
				path = "undefined" 
				prev_path = "4"
				break
			if setting_path == "switch": #switching mode
				path = prev_path
				prev_path = "4"
				break

			if setting_path == "1": #depending on the choice of the user, inverts the colors by reversing the order they appear in
				background_foreground_color = ["black", "white"]

			if setting_path == "2": #depending on the choice of the user, inverts the colors by reversing the order they appear in
				background_foreground_color = ["white", "black"]

	#How to navigate program
	if path == "9":
		turtle_title = "How To Navigate Program" #Navigation title
		title_for_mode(turtle_title,background_foreground_color) #draws title
		navigation_mode = True #begins navigation process
		navigation_screen(background_foreground_color) #draws navigation screen
		while navigation_mode == True: #loops code within
			navigation_exit_input = input("Input 'back' to return to the main menu: ") #asks for user input
			if navigation_exit_input == "back" or navigation_exit_input == "quit": #exiting out of mode
				path = "undefined"
				prev_path = "9"
				navigation_mode = False
				break
			if navigation_exit_input == "switch": #switching out of mode
				path = prev_path
				prev_path = "9"
				navigation_mode = False
				break
			
			elif navigation_exit_input != "back" or navigation_exit_input != "quit" or navigation_exit_input != "switch": #checks for bad input
				print("bad input")

	#Quit/End Program
	if path == "quit": #ends program if user enters quit
		sys.exit()

	#Bad Input For Menu Screen
	if path != "1" and  path != "2" and path != "3" and path != "4" and path != "9" and path != "undefined": #makes sure program loops correctly
		print("Enter a correct value")
		path = "undefined"















