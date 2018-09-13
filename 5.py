import turtle
turtle.shape("turtle")
turtle.left(0)



turtle.pd()
a=20
for j in range (10):
   
   for i in range(4):
       turtle.forward(a)
       turtle.right(90)

   turtle.pu()    
   a+=10
   turtle.left(90)
   turtle.forward(5)
   turtle.left(90)
   turtle.forward(5)
   turtle.left(180)
   turtle.pd()   

turtle.pu()
