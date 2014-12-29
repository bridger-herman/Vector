import math
import turtle

# 3 Dimensional Vector Class
# Digital representation of mathematical vectors
# Available operations:
# + Cross Product `u.cross(v)`
# + Dot Product `u.dot(v)`
# + Scalar Multiplication `u * k`
# + Scalar Division `u / k`
# + Projection `u.proj(v)`
# + Unit Vectors `u.unit()`
# + Angle Between Vectors `u.angle(v)`
class Vector3():
        def __init__(self, x = 0, y = 0, z = 0, mode = True):
                self.__x = x
                self.__y = y
                self.__z = z
                self.__values = (self.__x, self.__y, self.__z)
                # If vector is displayed in angle brackets or ijk notation
                # True: angle brackets
                # False: ijk notation
                self.__mode = mode
        
        # Cross Product
        # Performs the cross product self x other
        # Takes: a vector object, another vector object
        # Returns: a vector object
        def cross(self, other):
                new_x = self.get_y() * other.get_z() - self.get_z() * other.get_y()
                new_y = self.get_z() * other.get_x() - self.get_x() * other.get_z()
                new_z = self.get_x() * other.get_y() - self.get_y() * other.get_x()
                return Vector3(new_x, new_y, new_z, mode = self.get_mode())
        
        # Dot Product
        # Performs the dot product self . other
        # Takes: a vector object, another vector object
        # Returns: a scalar value
        def dot(self, other):
                new_values = []
                i = 0
                while i < len(self.get_values()):
                        new_values.append(self.get_values()[i] * other.get_values()[i])
                        i += 1
                return sum(new_values)
        
        # Vector Addition
        # Adds self and other
        # Takes: self and other, both vector objects
        # Returns: vector object
        def __add__(self, other):
                nx = self.get_x() + other.get_x()
                ny = self.get_y() + other.get_y()
                nz = self.get_z() + other.get_z()
                return Vector3(nx, ny, nz)

        # Vector Subtraction
        # Subtracts other from self
        # Takes: self and other, both vector objects
        # Returns: vector object
        def __sub__(self, other):
                nx = self.get_x() - other.get_x()
                ny = self.get_y() - other.get_y()
                nz = self.get_z() - other.get_z()
                return Vector3(nx, ny, nz)
        
        # Scalar Multiplication
        # Performs scalar multiplication of self * scalar
        # Takes: a vector object, a scalar to multiply the vector by
        # Returns: a vector object
        def __mul__(self, scalar):
                new_values = []
                for value in self.get_values():
                        new_values.append(value * scalar)
                return Vector3(*new_values, mode = self.get_mode())
                
        # Scalar True Division
        # Performs scalar true division of self / scalar
        # Takes: a vector object, a scalar value to divide the vector by
        # Returns: a vector object
        def __truediv__(self, scalar):
                return self * (1 / scalar)
                
        # Magnitude
        # Gets the magnitude of a vector
        # Takes: a vector object, format parameter (whether or not to format the output nicely)
        # Returns: a scalar value
        def mag(self, fmt = False):
                mag_squared = self.get_x() ** 2 + self.get_y() ** 2 + self.get_z() ** 2
                mag = mag_squared ** 0.5
                if fmt:
                        return "sqrt(" + str(mag_squared) + ") ~= " + str(mag)
                else:
                        return mag
        
        # Projection
        # Gets the value proj _other_ (self)
        # Takes: a vector object, another vector object
        # Returns: a vector object
        def proj(self, other):
                dot = self.dot(other)
                mag_2 = other.mag() ** 2
                vec = other * (dot / mag_2)
                return Vector3(*vec.get_values())
                
        # Unit Vector
        # Gets the unit vector of self
        # Takes: a vector object
        # Returns: a vector object
        def unit(self):
                return self / self.mag()
                
        # Angle
        # Gets the angle between self and other
        # Takes: a vector object, another vector object, boolean of degrees/radians
        # Returns: a scalar value
        def angle(self, other, radians = True):
                dot = self.dot(other)
                mag_s = self.mag()
                mag_o = other.mag()
                val = dot / (mag_s * mag_o)
                ang = math.acos(val)
                if radians:
                        return ang
                else:
                        return math.degrees(ang)
                        
        # Parallel
        # Determines if self and other are parallel
        # Returns: boolean
        def parallel(self, other):
                x = self.get_x() / other.get_x()
                y = self.get_y() / other.get_y()
                z = self.get_z() / other.get_z()
                if x == y and x == z:
                        return True
                else:
                        return False
                        
        # Orthogonal
        # Determines if self and other are orthogonal
        # Returns: boolean
        def orthogonal(self, other):
                dot = self.dot(other)
                if dot == 0:
                        return True
                else:
                        return False
        
        # Distinct
        # Determines if self and other are distinct vectors
        # Returns: boolean
        def distinct(self, other):
                if self.get_x() == other.get_x() and self.get_y() == other.get_y() and self.get_z() == other.get_z():
                        return False
                else:
                        return True
        
        # Reproduce
        # Takes: a vector object
        # Returns: a string dependant upon the user's choice of angle brackets or ijk notation
        def __repr__(self):
                final_str = ""
                if self.get_mode():
                        final_str = "<" + str(self.get_x()) + ", " + str(self.get_y()) + ", " + str(self.get_z()) + ">"
                else:
                        final_str += str(self.get_x()) + "i "
                        if self.get_y() < 0:
                                final_str += "- " + str(self.get_y())[1:]
                        else:
                                final_str += "+ " + str(self.get_y())
                        final_str +=  "j "
                        if self.get_z() < 0:
                                final_str += "- " + str(self.get_z())[1:]
                        else:
                                final_str += "+ " + str(self.get_z())
                        final_str += "k"
                return final_str
                
        def get_values(self):
                return self.__values
        def get_mode(self):
                return self.__mode
        def get_x(self):
                return self.__x
        def get_y(self):
                return self.__y
        def get_z(self):
                return self.__z

# 3 Dimensional axis class
# Axis for plotting points and vectors in 3 dimensions
# Handles:
# + Drawing the axis itself
# + Scaling the axis to maximum values
# + Plotting of points
# + Plotting of vectors
class Axis3():
        def __init__(self, xm = (-5, 5), ym = (-5, 5), zm = (-5, 5)):
                self.t = turtle.Turtle()
                self.s = turtle.Screen()
                self.s.screensize(1920,1040)
                self.s.title("Vector3D")
                self.t.ht()
                self.t.speed(0)
                self.objects = []
                # (Minimum, Maximum) for each axis
                self.maxm = ((-5, 5), (-5, 5), (-5, 5))
                # Number of pixels per unit
                self.scale = 40
                self.setscale(*self.maxm)
                self.drawaxis()
        
        # Draw Axis
        # Draws the 3 dimensional axis, with labels for xyz and their maxima
        # Takes: an axis object
        # Returns: None
        def drawaxis(self):
                # Draw the y axis
                self.t.color("#00aa00")
                self.t.forward(int(self.scale * self.maxm[1][1]))  # y axis maximum
                self.t.up()
                self.t.forward(self.scale)
                self.t.down()
                self.t.write(str(self.maxm[1][1]) + "  [+y]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.forward(int(self.scale * self.maxm[1][0]))  # y axis minimum
                self.t.up()
                self.t.backward(self.scale)
                self.t.down()
                self.t.write(str(self.maxm[1][0]) + "  [-y]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                # Draw the z axis
                self.t.color("#0000aa")
                self.t.left(90)
                self.t.forward(int(self.scale * self.maxm[2][1]))  # z axis maximum
                self.t.up()
                self.t.forward(self.scale)
                self.t.down()
                self.t.write(str(self.maxm[2][1]) + "  [+z]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.forward(int(self.scale * self.maxm[2][0]))  # z axis minimum
                self.t.up()
                self.t.backward(self.scale)
                self.t.down()
                self.t.write(str(self.maxm[2][0]) + "  [-z]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                # Draw the x axis
                self.t.color("#aa0000")
                self.t.right(225)
                self.t.forward(int(self.scale * self.maxm[0][1]))  # x axis maximum
                self.t.up()
                self.t.forward(self.scale)
                self.t.down()
                self.t.write(str(self.maxm[0][1]) + "  [+x]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.forward(int(self.scale * self.maxm[0][0]))  # x axis minimum
                self.t.up()
                self.t.backward(self.scale)
                self.t.down()
                self.t.write(str(self.maxm[0][0]) + "  [-x]")
                self.resetpos()
                
        # Redraw
        # Redraws the axis, with all the current vectors and points
        # Takes: None
        # Returns: None
        def redraw(self):
                self.t.clear()
                self.drawaxis()
                #TODO after plot() is condensed, make this general
                for vec in self.objects:
                        self.plotvector(vec)
        
        # Set Scale
        # Sets the scale of the 3D axis (number of pixels per unit)
        # Takes: xm, ym, zm the (minimum, maximum) of each axis
        # Returns: None
        def setscale(self, xm = (-5, 5), ym = (-5, 5), zm = (-5, 5)):
                self.maxm = (xm, ym, zm)
        
        #TODO add comment
        #TODO condense plotpoint and plotvector into one method, plot
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
        
        # Plot
        # Plots a vector on the 3D axis
        # Takes: a vector object
        # Returns: None
        #TODO guides on/off (gray color or nothing)
        def plotvector(self, vector = Vector3(1,1,1)):
                if vector not in self.objects:
                        self.objects.append(vector)
                nmax = []
                nmin = []
                vals = vector.get_values()
                i = 0
                while i < len(vals):
                        if vals[i] > self.maxm[i][1]:
                                nmax.append(vals[i])
                        else:
                                nmax.append(self.maxm[i][1])
                        if vals[i] < self.maxm[i][0]:
                                nmin.append(vals[i])
                        else:
                                nmin.append(self.maxm[i][0])
                        i += 1
                nmaxm = []
                nmaxm.append((nmin[0], nmax[0]))
                nmaxm.append((nmin[1], nmax[1]))
                nmaxm.append((nmin[2], nmax[2]))
                if tuple(nmaxm) != self.maxm:
                        self.setscale(*nmaxm)
                        self.redraw()
                self.t.color("#bbbbbb")
                # Go to x coordinate
                self.t.left(45)
                self.t.backward(self.scale * vector.get_x())
                # Go to y coordinate
                self.t.right(45)
                self.t.forward(self.scale * vector.get_y())
                # Go to z coordinate
                self.t.left(90)
                self.t.forward(self.scale * vector.get_z())
                # Draw arrow
                self.t.color("#000000")
                pos = self.t.position()
                heading = math.degrees(math.atan(pos[1] / pos[0]))
                # Fixes arrow head direction on positive x values
                if pos[0] <= 0:
                        arrow = 45
                elif pos[0] == 0 and pos[1] <= 0:
                        arrow = 135
                else:
                        arrow = 135
                self.t.setheading(heading + arrow)
                self.t.forward(6)
                self.t.goto(*pos)
                self.t.setheading(heading - arrow)
                self.t.forward(6)
                self.t.goto(*pos)
                self.t.goto(0, 0)
                self.resetpos()
        
        def resetpos(self):
                # Reset so turtle is at (0, 0), facing positive y axis, and black-colored
                self.t.color("#000000")
                self.t.up()
                self.t.goto(0, 0)
                self.t.setheading(0)
                self.t.down()
        


i = Vector3(5,3,1)
j = Vector3(1,2,3)
k = i.cross(j)
a = Axis3()
a.plotvector(i)
a.plotvector(j)
a.plotvector(k)
input()
