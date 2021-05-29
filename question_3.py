import turtle 
import math


num =  int(input())

# trangle components = "/ \ _".split()
cos60 = math.cos(math.pi/3)
sin60 = math.sin(math.pi/3)
window = turtle.Screen()
window.title("CUT Pyramid")
turtle.tracer(False)
x,y = window.screensize()
length = y/num*2
turtle.penup()
turtle.setposition(-length/2,y - 50)
turtle.pendown()
    
def UP_RIGHT(num,mouse) :
    x,y = mouse.position()
    mouse.setposition(x+num*length/2 , y+num*length*sin60)
def DOWN_RIGHT(num,mouse) :
    x,y = mouse.position()
    mouse.setposition(x+num*length/2 , y-num*length*sin60)
def RIGHT(num,mouse) :
    x,y = mouse.position()
    mouse.setposition(x+num*length, y)

def type1(mouse):
    RIGHT(1,mouse)
    DOWN_RIGHT(1,mouse)
    RIGHT(-2,mouse)
    UP_RIGHT(1,mouse)

def type2(mouse):
    RIGHT(2,mouse)
    UP_RIGHT(-1,mouse)
    RIGHT(-1,mouse)
    DOWN_RIGHT(-1,mouse)

def type3(mouse):
    DOWN_RIGHT(1,mouse)
    UP_RIGHT(-1,mouse)
    RIGHT(-1,mouse)
    UP_RIGHT(2,mouse)

def type4(mouse):
    DOWN_RIGHT(2,mouse)
    RIGHT(-1,mouse)
    DOWN_RIGHT(-1,mouse)
    UP_RIGHT(1,mouse)

def showPyramid(num) :

    for i in range(2,num+1):
        howCome = ((i+1)//3) 
        if i%3 ==2 :
            turtle.pencolor('red')
            how = ((i+1)//3)*2-1
            for j in range(how):
                if j%2==0 :
                    type1(turtle)
                    RIGHT(1,turtle)
                else :
                    type2(turtle)
                    RIGHT(2,turtle)
            RIGHT(-(howCome + (howCome-1)*2),turtle )

        elif i%3== 0 :
            turtle.pencolor('green')
            type3(turtle)
            how = ((i+1)//3)*2-1
            for j in range(how):
                if j%2==1 :
                    type1(turtle)
                    RIGHT(1,turtle)
                else :
                    type2(turtle)
                    RIGHT(2,turtle)
            type4(turtle)
            RIGHT(-(howCome*3-1) ,turtle)
          
        else :
            turtle.pencolor('blue')
            turtle.penup()
            RIGHT(1,turtle)
            turtle.pendown()
            for j in range(how):
                if j%2==0 :
                    type1(turtle)
                    RIGHT(1,turtle)
                else :
                    type2(turtle)
                    RIGHT(2,turtle)
            turtle.penup()
            RIGHT(-(howCome*3-1),turtle )
            turtle.pendown()
        turtle.penup()
        UP_RIGHT(-1,turtle)
        turtle.pendown()
    turtle.getscreen()._root.mainloop() 
if num%3==0 :
    print("Can not generate this case !")
else :
    showPyramid(num)
