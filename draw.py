import turtle
from vector import *
class Axis():
        def __init__(self, size = 100, max_x = 5, max_y = 5, max_z = 5):
                self.__size = size
                self.t = turtle.Turtle()
                self.t.ht()
                self.t.speed(0)
                self.maxm = (5, 5, 5)
                # Number of pixels per unit
                self.scale = (20, 20, 20)
                self.setscale(max_x, max_y, max_z)
                self.drawaxis()
                
        def drawaxis(self):
                # Draw the y axis
                self.t.color("#00aa00")
                self.t.forward(self.__size)
                self.t.up()
                self.t.forward(self.__size // 10)
                self.t.down()
                self.t.write(str(self.maxm[1]) + "  +y")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.backward(self.__size)
                self.t.up()
                self.t.goto(0, 0)
                # Draw the z axis
                self.t.down()
                self.t.color("#0000aa")
                self.t.left(90)
                self.t.forward(self.__size)
                self.t.up()
                self.t.forward(self.__size // 10)
                self.t.down()
                self.t.write(str(self.maxm[2]) + "  +z")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.backward(self.__size)
                self.t.up()
                self.t.goto(0, 0)
                # Draw the x axis
                self.t.down()
                self.t.color("#aa0000")
                self.t.right(45)
                self.t.forward(self.__size)
                self.t.goto(0, 0)
                self.t.backward(self.__size)
                self.t.up()
                self.t.backward(self.__size // 10)
                self.t.down()
                self.t.write(str(self.maxm[0]) + "  +x")
                self.resetpos()
        
        def setscale(self, max_x = 5, max_y = 5, max_z = 5):
                xs = self.__size // max_x
                ys = self.__size // max_y
                zs = self.__size // max_z
                self.maxm = (max_x, max_y, max_z)
                self.scale = (xs, ys, zs)
        
        def plotpoint(self, point = (0,0,0)):
                self.t.up()
                # Go to x coordinate
                self.t.left(45)
                self.t.backward(self.scale[0] * point[0])
                # Go to y coordinate
                self.t.right(45)
                self.t.forward(self.scale[1] * point[1])
                # Go to z coordinate
                self.t.left(90)
                self.t.forward(self.scale[2] * point[2])
                # Draw point
                self.t.setheading(0)
                self.t.forward(2)
                self.t.setheading(90)
                self.t.down()
                self.t.begin_fill()
                self.t.circle(2)
                self.t.end_fill()
        
        def resetpos(self):
                # Reset so turtle is at (0, 0), facing positive y axis, and black-colored
                self.t.color("#000000")
                self.t.up()
                self.t.goto(0, 0)
                self.t.setheading(0)
                self.t.down()
        
        #def plotvector(self, vector = Vector3(0, 0, 0)):
        #        self.plotpoint(vector.get_values())
        #        self.t.goto(0, 0)
        #        self.resetpos()
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#a = Axis(200)
#u = Vector3(2,2,2)
#p = (1,1,0)
#q = (3,4,5)
##a.plotpoint(p)
#a.plotvector(u)
#input()
