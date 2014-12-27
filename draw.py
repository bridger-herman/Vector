import turtle
class Draw():
        def __init__(self, size = 100):
                self.__size = size
                self.__t = turtle.Turtle()
                self.__s = turtle.Screen()
                self.__t.ht()
                self.__t.speed(0)
                # Number of pixels per unit
                self.__scale = (20, 20, 20)
                self.__max = (5, 5, 5)
                
        def drawaxes(self):
                # Draw the y axis
                self.__t.color("#00aa00")
                self.__t.forward(self.__size)
                self.__t.up()
                self.__t.forward(self.__size // 10)
                self.__t.down()
                self.__t.write(str(self.__max[1]) + "  +y")
                self.__t.goto(0, 0)
                self.__t.backward(self.__size)
                self.__t.goto(0, 0)
                
                # Draw the z axis
                self.__t.color("#0000aa")
                self.__t.left(90)
                self.__t.forward(self.__size)
                self.__t.up()
                self.__t.forward(self.__size // 10)
                self.__t.down()
                self.__t.write(str(self.__max[2]) + "  +z")
                self.__t.goto(0, 0)
                self.__t.backward(self.__size)
                self.__t.goto(0, 0)
                
                # Draw the x axis
                self.__t.color("#aa0000")
                self.__t.right(45)
                self.__t.forward(self.__size)
                self.__t.goto(0, 0)
                self.__t.backward(self.__size)
                self.__t.up()
                self.__t.backward(self.__size // 10)
                self.__t.down()
                self.__t.write(str(self.__max[0]) + "  +x")
                
                # Reset so turtle is at (0, 0), facing positive y axis, and black-colored
                self.__t.color("#000000")
                self.__t.goto(0, 0)
                self.__t.left(45)
        
        def setscale(self, max_x = 5, max_y = 5, max_z = 5):
                xs = self.__size // max_x
                ys = self.__size // max_y
                zs = self.__size // max_z
                self.__scale = (xs, yx, zs)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

a = Draw()
a.drawaxes()
input()
