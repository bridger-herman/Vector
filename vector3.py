import math
import turtle

# 3 Dimensional Point Class
# Digital representation of points in space
# Available operations:
# + Distance Between Points `p.distance(q)`
class Point3D():
        # Initializer
        # Takes:
        # + self; Point3D object
        # TODO define more in depth
        # + p; tuple; coordinates of point
        def __init__(self, *p):
                if not p:
                        p = (1, 1, 1)
                self.__x = p[0]
                self.__y = p[1]
                self.__z = p[2]
                self.__values = p
        
        # Distance
        # Determines the distance between two points
        # Takes: self, other; both Point3D objects
        # Returns: a scalar value
        def distance(self, other):
                dx = other.get_x() - self.get_x()
                dy = other.get_y() - self.get_y()
                dz = other.get_z() - self.get_z()
                dis = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5
                return dis
        
        def get_values(self):
                return self.__values
        def get_x(self):
                return self.__x
        def get_y(self):
                return self.__y
        def get_z(self):
                return self.__z

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
#TODO add description to all initializers
class Vec3D():
        # Initializer
        # Takes:
        # + self; Vec3D object
        # TODO define more in depth
        # + p; tuple; coordinates of vector
        # + mode; boolean; if vector is displayed in angle brackets [True] or ijk notation [False]
        def __init__(self, *p, mode = True):
                print("p",p)
                if not p:
                       p = (1, 1, 1)
                self.__x = p[0]
                self.__y = p[1]
                self.__z = p[2]
                self.__values = p
                self.__mode = mode
        
        # Cross Product
        # Performs the cross product self x other
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def cross(self, other):
                new_x = self.get_y() * other.get_z() - self.get_z() * other.get_y()
                new_y = self.get_z() * other.get_x() - self.get_x() * other.get_z()
                new_z = self.get_x() * other.get_y() - self.get_y() * other.get_x()
                return Vec3D(new_x, new_y, new_z, mode = self.get_mode())
        
        # Dot Product
        # Performs the dot product self . other
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def dot(self, other):
                new_values = []
                i = 0
                while i < len(self.get_values()):
                        new_values.append(self.get_values()[i] * other.get_values()[i])
                        i += 1
                return sum(new_values)
        
        # Vector Addition
        # Adds self and other
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def __add__(self, other):
                nx = self.get_x() + other.get_x()
                ny = self.get_y() + other.get_y()
                nz = self.get_z() + other.get_z()
                return Vec3D((nx, ny, nz))

        # Vector Subtraction
        # Subtracts other from self
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def __sub__(self, other):
                nx = self.get_x() - other.get_x()
                ny = self.get_y() - other.get_y()
                nz = self.get_z() - other.get_z()
                return Vec3D(nx, ny, nz)
        
        # Scalar Multiplication
        # Performs scalar multiplication of self * scalar
        # Takes: 
        # + self; Vec3D object
        # + scalar; float/int; a scalar value to divide the vector by
        # Returns: Vec3D object
        def __mul__(self, scalar):
                new_values = []
                for value in self.get_values():
                        new_values.append(value * scalar)
                return Vec3D(new_values, mode = self.get_mode())
                
        # Scalar True Division
        # Performs scalar true division of self / scalar
        # Takes: 
        # + self; Vec3D object
        # + scalar; integer; a scalar value to divide the vector by
        # Returns: Vec3D object
        def __truediv__(self, scalar):
                return self * (1 / scalar)
                
        # Magnitude
        # Gets the magnitude of a vector
        # Takes: 
        # + self; Vec3D object
        # + fmt; integer; format parameter (whether or not to format the output nicely)
        # Returns: float/int
        def mag(self, fmt = False):
                mag_squared = self.get_x() ** 2 + self.get_y() ** 2 + self.get_z() ** 2
                mag = mag_squared ** 0.5
                if fmt:
                        return "sqrt(" + str(mag_squared) + ") ~= " + str(mag)
                else:
                        return mag
        
        # Projection
        # Gets the value proj _other_ (self)
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def proj(self, other):
                dot = self.dot(other)
                mag_2 = other.mag() ** 2
                vec = other * (dot / mag_2)
                return Vec3D(vec.get_values())
                
        # Unit Vector
        # Gets the unit vector of self
        # Takes: Vec3D object
        # Returns: Vec3D object
        def unit(self):
                return self / self.mag()
                
        # Angle
        # Gets the angle between self and other
        # Takes:
        # + self, other; Vec3D objects
        # + radians; boolean
        # Returns: float/int
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
        # Takes: self, other; Vec3D objects
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
        # Takes: self, other; Vec3D objects
        # Returns: boolean
        def orthogonal(self, other):
                dot = self.dot(other)
                if dot == 0:
                        return True
                else:
                        return False
        
        # Distinct
        # Determines if self and other are distinct vectors
        # Takes: self, other; Vec3D objects
        # Returns: boolean
        def distinct(self, other):
                if self.get_x() == other.get_x() and self.get_y() == other.get_y() and self.get_z() == other.get_z():
                        return False
                else:
                        return True
        
        # Reproduce
        # Takes: self; Vec3D object
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

# 3 Dimensional Parametric Vector Class
# 
# TODO add more description
class ParVec3D(Vec3D):
        def __init__(self, *pd):
                if not pd:
                        pd = (1, 1, 1, 1, 1, 1)
                print(pd)
                super().__init__(pd[:3], True)
                self.__xt = pd[3]
                self.__yt = pd[4]
                self.__zt = pd[5]
                self.__position = pd[3:]
        
        #TODO add rest of methods
        
        def get_xt(self):
                return self.__xt
        def get_yt(self):
                return self.__yt
        def get_zt(self):
                return self.__zt
        def get_position(self):
                return self.__position
        def get_tmin(self):
                return self.__tmin
        def get_tmax(self):
                return self.__tmax
        def get_res(self):
                return self.__res
        
# 3 Dimensional axis class
# Axis for plotting points and vectors in 3 dimensions
# Handles:
# + Drawing the axis itself
# + Scaling the axis to maximum values
# + Plotting of points
# + Plotting of vectors
class Axis3D():
        def __init__(self, xm = (-5, 5), ym = (-5, 5), zm = (-5, 5), guides = True):
                self.t = turtle.Turtle()
                self.s = turtle.Screen()
                self.s.screensize(1920, 1040)
                self.s.title("Vector3D")
                self.guides = guides
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
        # Takes: Axis3D object
        # Returns: None
        def drawaxis(self):
                self.t.pensize(1)
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
        # Redraws the axis, with all the current Vec3Ds and Point3Ds
        # Takes: Vec3D or Point3D object
        # Returns: None
        def redraw(self):
                self.t.clear()
                self.drawaxis()
                for obj in self.objects:
                        self.plot(obj)
        
        # Set Scale
        # Sets the scale of the 3D axis (number of pixels per unit)
        # Takes: xm, ym, zm; ints; the (minimum, maximum) of each axis
        # Returns: None
        def setscale(self, xm = (-5, 5), ym = (-5, 5), zm = (-5, 5)):
                self.maxm = (xm, ym, zm)
        
        # Plot
        # Plots a Vec3D or a Point3D on the 3D axis
        # Takes: 
        # + self; Axis3D object
        # + obj; Vec3D or Point3D object
        # Returns: None
        def plot(self, obj = None):
                if obj not in self.objects:
                        self.objects.append(obj)
                nmax = []
                nmin = []
                vals = obj.get_values()
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
                if self.guides:
                        self.t.color("#bbbbbb")
                        self.t.pensize(1)
                else:
                        self.t.up()
                # Go to x coordinate
                self.t.left(45)
                self.t.backward(self.scale * obj.get_x())
                # Go to y coordinate
                self.t.right(45)
                self.t.forward(self.scale * obj.get_y())
                # Go to z coordinate
                self.t.left(90)
                self.t.forward(self.scale * obj.get_z())
                if self.guides:
                        self.t.color("#000000")
                        self.t.pensize(2)
                else:
                        self.t.down()
                # Draw arrow if Vec3D
                if type(obj) == type(Vec3D()):
                        pos = self.t.position()
                        heading = math.degrees(math.atan(pos[1] / pos[0]))
                        # Fixes arrow head direction on positive x (2D) values
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
                # Draw circle if Point3D
                elif type(obj) == type(Point3D()):
                        self.t.setheading(0)
                        self.t.forward(2)
                        self.t.setheading(90)
                        self.t.down()
                        self.t.begin_fill()
                        self.t.circle(2)
                        self.t.end_fill()
                self.resetpos()
        
        # Parametric Plot
        # Plots a parametric vector in 3D
        # Takes: 
        # + self; Axis3D object
        # + obj; ParVec3D object
        # Returns: None
        def paramplot(self, obj = None, tmin = 0, tmax = 5, res = 0.5):
                sincos45 = 1.41421356
                # Goto initial position
                self.t.up()
                iy = self.scale * (obj.get_z() - obj.get_x() / sincos45)
                ix = self.scale * (obj.get_y() - obj.get_x() / sincos45)
                self.t.goto(int(ix), int(iy))
                self.t.down()
                # Plot the rest of the curve
                t = tmin
                while t < tmax:
                        x = ix + self.scale * ((obj.get_zt() * t) - (obj.get_xt() * t) / sincos45)
                        y = iy + self.scale * ((obj.get_yt() * t) - (obj.get_xt() * t) / sincos45)
                        self.t.goto(int(x), int(y))
                        t += res
        # Reset Position
        # Reset so turtle is at (0, 0), facing positive y axis, black-colored, and of size 2px
        # Takes: a Turtle object
        # Returns: None
        def resetpos(self):
                self.t.pensize(2)
                self.t.color("#000000")
                self.t.up()
                self.t.goto(0, 0)
                self.t.setheading(0)
                self.t.down()
        
#i = Vec3D(1,1,1)
#j = Vec3D(1,2,3)
#k = i.cross(j)
p = ParVec3D(1,1,1,2,2,3)
#a = Axis3D()
#a.plot(i)
#a.plot(j)
#a.plot(k)
#a.paramplot(p)
input()
