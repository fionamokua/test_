import turtle
body_turtle=turtle.Turtle()
#big triangle
def a(x,y):

    body_turtle.left( x )
    body_turtle.forward( y)  
a( 90 , 50 )
a(120,100)
a(150,87)
a(270,50)
a(240,100)
a(210,87)
body_turtle.forward(50)
#smaller triange
a(135,71) 
body_turtle.penup()
a(135,50)
a(90,50)
body_turtle.pendown()
a(225,71)
#repositioning to centre of triangle
body_turtle.penup()
a(225,50)
#firstcircle
body_turtle.pendown()

body_turtle.circle(20)
#secondcircle
body_turtle.penup()

a(225,35)
a(90,0)
body_turtle.pendown()

body_turtle.circle(20)
#repositioning turtle
body_turtle.penup()
a(90,35)
a(270,35)
a(90,0)
#third circle
body_turtle.pendown()
body_turtle.circle(20)
#repositioning turtle
body_turtle.penup()
a(90,35)
a(45,0)
a(0,35)
a(135,0)
#fourth circle
body_turtle.pendown()
body_turtle.circle(45)
#repositioning turtle
body_turtle.penup()
a(45,35)
a(270,50)
a(270,0)
a(180,0)
#fifth circle
body_turtle.pendown()
body_turtle.circle(40)
#repositioning turtle
body_turtle.penup()
a(45,35)
a(270,50)
a(270,0)
a(180,0)