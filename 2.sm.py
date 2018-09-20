
import math
import turtle
#радиус описоной окружности равеного правельного многукгольника
#turtle.speed (10)

#turtle.circle (50,360)

'''def mam (n,R):
    
  red=360/n
  turtle.right(red)
  turtle.setpos(0,0)
  for i  in range (1,n+1,1):
    turtle.forward(R)
    turtle.setheading(red*i)
'''

'''for i in range (0,360,1):
   rad=i*3.14/180
   y=100*math.sin(rad)
   y=int(y)
   x=100*math.cos(rad)
   x=int(x)
   turtle.setpos(x,y)'''

'''R=50
n=7
red=360/n
turtle.setpos(0,0)
for i  in range (1,n+1,1):
   turtle.forward(R)
   turtle.seteading(red*i)  '''

def mnog (R,A,n):
    turtle.pu()
    turtle.setpos(0,-R)
    
    turtle.pd()

    ug=360/n
    turtle.right(ug/2)
    
    for i in range (n):
      turtle.left(ug)
      turtle.forward(A)
    turtle.left(ug/2)
    turtle.pu() 
    turtle.setpos(0,0)
    
def krug (R):
    
     turtle.pu() 
     turtle.setpos(0,-R)
     turtle.pd()
     
     
     
     turtle.circle (R,360)
    
     turtle.pu()
     turtle.setpos(0,0)
     turtle.pd()



r=50
n=7

i=1
k=3
for i in range (n-2):
 rad=(360/(2*k))*3.14/180
 A=r*(2*math.sin(rad))

 krug (r)
 mnog(r,A,k)

 r=r*1.5

 k=k+1

