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
        # + p; tuple; coordinates of point
        def __init__(self, *p):
                if not p:
                        p = (1, 1, 1)
                self.__x = p[0]
                self.__y = p[1]
                self.__z = p[2]
                self.__position = p
        
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
        
        # Reproduce
        # Takes: self; Point3D object
        # Returns: string
        def __repr__(self):
                return "(" + self.get_x() + ", " + self.get_y() + ", " + self.get_z() + ")"
        
        def get_position(self):
                return self.__position
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
class Vec3D():
        # Initializer
        # Takes:
        # + self; Vec3D object
        # + p; tuple; coordinates of vector
        def __init__(self, *p):
                if not p:
                       p = (1, 1, 1)
                self.__x = p[0]
                self.__y = p[1]
                self.__z = p[2]
                self.__position = p
        
        # Cross Product
        # Performs the cross product self x other
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def cross(self, other):
                new_x = self.get_y() * other.get_z() - self.get_z() * other.get_y()
                new_y = self.get_z() * other.get_x() - self.get_x() * other.get_z()
                new_z = self.get_x() * other.get_y() - self.get_y() * other.get_x()
                return Vec3D(new_x, new_y, new_z)
        
        # Dot Product
        # Performs the dot product self . other
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def dot(self, other):
                new_position = []
                i = 0
                while i < len(self.get_position()):
                        new_position.append(self.get_position()[i] * other.get_position()[i])
                        i += 1
                return sum(new_position)
        
        # Vector Addition
        # Adds self and other
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def __add__(self, other):
                new_x = self.get_x() + other.get_x()
                new_y = self.get_y() + other.get_y()
                new_z = self.get_z() + other.get_z()
                return Vec3D(new_x, new_y, new_z)

        # Vector Subtraction
        # Subtracts other from self
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def __sub__(self, other):
                new_x = self.get_x() - other.get_x()
                new_y = self.get_y() - other.get_y()
                new_z = self.get_z() - other.get_z()
                return Vec3D(new_x, new_y, new_z)
        
        # Scalar Multiplication
        # Performs scalar multiplication of self * scalar
        # Takes: 
        # + self; Vec3D object
        # + scalar; float/int; a scalar value to divide the vector by
        # Returns: Vec3D object
        def __mul__(self, scalar):
                new_position = []
                for value in self.get_position():
                        new_position.append(value * scalar)
                return Vec3D(*new_position)
                
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
        # Returns: float/int
        def mag(self):
                mag_squared = self.get_x() ** 2 + self.get_y() ** 2 + self.get_z() ** 2
                mag = mag_squared ** 0.5
                return mag
        
        # Projection
        # Gets the value proj _other_ (self)
        # Takes: self, other; Vec3D objects
        # Returns: Vec3D object
        def proj(self, other):
                dot = self.dot(other)
                mag_2 = other.mag() ** 2
                vec = other * (dot / mag_2)
                return Vec3D(*vec.get_position())
                
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
        # Returns: string
        def __repr__(self):
                final_str = ""
                final_str = "<" + str(self.get_x()) + ", " + str(self.get_y()) + ", " + str(self.get_z()) + ">"
                return final_str
                
        def get_position(self):
                return self.__position
        def get_x(self):
                return self.__x
        def get_y(self):
                return self.__y
        def get_z(self):
                return self.__z

# 3 Dimensional Parametric Vector Class
# Parametric vectors (vectors including a 't')
class ParVec3D(Vec3D):
        # Initializer
        # Takes:
        # + self; ParVec3D object
        # + pdt; tuple; coorinates of vector (including position and direction); (x, y, z, xt, yt, zt, (tmin, tmax, resolution))
        def __init__(self, *pdt):
                if not pdt:
                        pdt = (1, 1, 1, 1, 1, 1, (0, 1, 0.5))
                # TODO add a support class for building each of these classes or modify
                # TODO includes merging ParVec3D and Vec3D (very eventually)
                self.__x = pdt[0]
                self.__y = pdt[1]
                self.__z = pdt[2]
                self.__position = pdt[:3]
                self.__xt = pdt[3]
                self.__yt = pdt[4]
                self.__zt = pdt[5]
                self.__direction = pdt[3:6]
                self.__tmin = pdt[6][0]
                self.__tmax = pdt[6][1]
                self.__res = pdt[6][2]
                self.__props = pdt[6]
                
        # Splits the ParVec3D into two Vec3Ds, one for position, one for direction
        # Takes: self; ParVec3D object
        # Returns: tuple containing:
        # + Position Vec3D object
        # + Direction Vec3D object
        def split(self):
                return(Vec3D(*self.get_position()), Vec3D(*self.get_direction()))
                
        # Performs the cross product self x other
        # Takes:
        # + self; ParVec3D object
        # + other; ParVec3D object
        # Returns:
        # + ParVec3D object
        def cross(self, other):
                self_vectors = self.split()
                other_vectors = other.split()
                self_p = self_vectors[0]
                self_d = self_vectors[1]
                other_p = other_vectors[0]
                other_d = other_vectors[1]
                new_p = self_p.cross(other_p)
                new_d = self_d.cross(other_d)
                p_tuple = new_p.get_position()
                d_tuple = new_d.get_position()
                pd_list = list(p_tuple + d_tuple)
                pd_list.append(self.get_props())
                return ParVec3D(*pd_list)
        
        # Performs the dot product self . other
        # Takes:
        # + self; ParVec3D object
        # + other: ParVec3D object
        # Returns:
        # + float/int; scalar dot product
        #TODO verify correctness of method, pretty sure this is not right
        def dot(self, other):
                self_vectors = self.split()
                other_vectors = other.split()
                self_p = self_vectors[0].get_position()
                self_d = self_vectors[1].get_position()
                other_p = other_vectors[0].get_position()
                other_d = other_vectors[1].get_position()
                p_total = 0
                d_total = 0
                i = 0
                while i < len(self_p):
                        p_total += self_p[i] * other_p[i]
                        d_total += self_d[i] * other_d[i]
                        i += 1
                return p_total + d_total
        
        # Vector Addition
        # Adds self and other
        # Takes: self, other; ParVec3D objects
        # Returns: ParVec3D object
        def __add__(self, other):
                new_x = self.get_x() + other.get_x()
                new_y = self.get_y() + other.get_y()
                new_z = self.get_z() + other.get_z()
                new_xt = self.get_xt() + other.get_xt()
                new_yt = self.get_yt() + other.get_yt()
                new_zt = self.get_zt() + other.get_zt()
                return ParVec3D(new_x, new_y, new_z, new_xt, new_yt, new_zt, self.get_props())
                
        # Vector Subtraction
        # Subtracts other from self
        # Takes: self, other; ParVec3D objects
        # Returns: ParVec3D object
        def __sub__(self, other):
                new_x = self.get_x() - other.get_x()
                new_y = self.get_y() - other.get_y()
                new_z = self.get_z() - other.get_z()
                new_xt = self.get_xt() - other.get_xt()
                new_yt = self.get_yt() - other.get_yt()
                new_zt = self.get_zt() - other.get_zt()
                return ParVec3D(new_x, new_y, new_z, new_xt, new_yt, new_zt, self.get_props())
        
        # Vector Projection
        # Takes: 
        # + self; ParVec3D object
        # + other; ParVec3D object
        # Returns: ParVec3D object
        # TODO figure out parametric vector projection
        def proj(self, other):
                return self
        
        # Unit Vector
        # Finds the unit direction vector of the given parametric vector
        # Takes:
        # + self; ParVec3D object
        # Returns:
        # + Vec3D object
        def unit(self):
                return Vec3D(*self.get_direction()).unit()
                
        # Angle
        # Finds the angle between the direction vector of two parametric vectors
        # Takes:
        # + self; ParVec3D object
        # + other; ParVec3D object
        # Returns: float/int
        def angle(self, other):
                self_d = Vec3D(*self.get_direction())
                other_d = Vec3D(*other.get_direction())
                return self_d.angle(other_d, False)
                
        # Reproduce
        # Takes: self; ParVec3D object
        # Returns: string
        def __repr__(self):
                final_str = super().__repr__()
                final_str += " + <" + str(self.get_xt()) + "t, " + str(self.get_yt()) + "t, " + str(self.get_zt()) + "t>"
                return final_str
        
        def get_x(self):
                return self.__x
        def get_y(self):
                return self.__y
        def get_z(self):
                return self.__z
        def get_position(self):
                return self.__position
        def get_xt(self):
                return self.__xt
        def get_yt(self):
                return self.__yt
        def get_zt(self):
                return self.__zt
        def get_direction(self):
               return self.__direction
        def get_props(self):
                return self.__props
       
# 3 Dimensional axis class
# Axis for plotting points and vectors in 3 dimensions
# Handles:
# + Drawing the axis itself
# + Scaling the axis to maximum values
# + Plotting of points
# + Plotting of vectors
# + Plotting of parametric vectors
class Axis3D():
        # Initializer
        # Takes:
        # + self; Axis3D object
        # + xm; tuple; (xmin, xmax)
        # + ym; tuple; (ymin, ymax)
        # + zm; tuple; (zmin, zmax)
        # + guides; bool; whether or not to display tracing guides on each axis
        def __init__(self, xm = (-5, 5), ym = (-5, 5), zm = (-5, 5), guides = True):
                self.t = turtle.Turtle()
                self.s = turtle.Screen()
                self.s.screensize(3840, 2560)
                self.s.title("Vector3D")
                self.guides = guides
                self.t.ht()
                self.t.speed(0)
                self.objects = []
                # (Minimum, Maximum) for each axis
                self.maxmin = ((-5, 5), (-5, 5), (-5, 5))
                # Number of pixels per unit
                self.scale = 40
                self.setscale(*self.maxmin)
                self.drawaxis()
        
        # Draw Axis
        # Draws the 3 dimensional axis, with labels for xyz and their maxima
        # Takes: Axis3D object
        # Returns: None
        def drawaxis(self):
                self.t.pensize(4)
                # Draw the y axis
                self.t.color("#00aa00")
                self.t.forward(int(self.scale * self.maxmin[1][1]))  # y axis maximum
                self.t.up()
                self.t.forward(self.scale)
                self.t.down()
                self.t.write(str(self.maxmin[1][1]) + "  [y axis]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.forward(int(self.scale * self.maxmin[1][0]))  # y axis minimum
                self.t.up()
                self.t.backward(self.scale)
                self.t.down()
                self.t.write(str(self.maxmin[1][0]))
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                # Draw the z axis
                self.t.color("#0000aa")
                self.t.left(90)
                self.t.forward(int(self.scale * self.maxmin[2][1]))  # z axis maximum
                self.t.up()
                self.t.forward(self.scale)
                self.t.down()
                self.t.write(str(self.maxmin[2][1]) + "  [z axis]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.forward(int(self.scale * self.maxmin[2][0]))  # z axis minimum
                self.t.up()
                self.t.backward(self.scale)
                self.t.down()
                self.t.write(str(self.maxmin[2][0]))
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                # Draw the x axis
                self.t.color("#aa0000")
                self.t.right(225)
                self.t.forward(int(self.scale * self.maxmin[0][1]))  # x axis maximum
                self.t.up()
                self.t.forward(self.scale)
                self.t.down()
                self.t.write(str(self.maxmin[0][1]) + "  [x axis]")
                self.t.up()
                self.t.goto(0, 0)
                self.t.down()
                self.t.forward(int(self.scale * self.maxmin[0][0]))  # x axis minimum
                self.t.up()
                self.t.backward(self.scale)
                self.t.down()
                self.t.write(str(self.maxmin[0][0]))
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
                self.maxmin = (xm, ym, zm)
        
        # Plot
        # Plots a Vec3D or a Point3D on the 3D axis
        # Takes: 
        # + self; Axis3D object
        # + obj; Vec3D or Point3D object
        # + t_param; tuple; (minimum, maximum, resolution)
        # Returns: None
        # TODO Figure out error in rescaling of axes of negative numbers on the Y axis
        def plot(self, obj = None):
                if obj not in self.objects:
                        self.objects.append(obj)
                new_max = []
                new_min = []
                # TODO Figure out a way to do this without creating new objects every time
                if type(obj) != type(ParVec3D()):
                        position = obj.get_position()
                        i = 0
                        while i < len(position):
                                if position[i] > self.maxmin[i][1]:
                                        new_max.append(position[i])
                                else:
                                        new_max.append(self.maxmin[i][1])
                                if position[i] < self.maxmin[i][0]:
                                        new_min.append(position[i])
                                else:
                                        new_min.append(self.maxmin[i][0])
                                i += 1
                else:
                        tmin = obj.get_props()[0]
                        tmax = obj.get_props()[1]
                        res = obj.get_props()[2]
                        direction = obj.get_direction()
                        [new_max.append(n * tmax) for n in direction]
                        [new_min.append(n * tmin) for n in direction]
                new_maxs = []
                new_maxs.append((new_min[0], new_max[0]))
                new_maxs.append((new_min[1], new_max[1]))
                new_maxs.append((new_min[2], new_max[2]))
                if tuple(new_maxs) != self.maxmin:
                        self.setscale(*new_maxs)
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
                # Draw rest of curve if ParVec3D
                elif type(obj) == type(ParVec3D()):
                        SINCOS45 = 1.41421356
                        xcor = self.scale * (obj.get_z() - (obj.get_x() / SINCOS45))
                        ycor = self.scale * (obj.get_y() - (obj.get_x() / SINCOS45))
                        self.t.goto(xcor, ycor)
                        t_n = tmin
                        while t_n < tmax:
                                x = xcor + self.scale * ((obj.get_zt() * t_n) - (obj.get_xt() * t_n) / SINCOS45)
                                y = ycor + self.scale * ((obj.get_yt() * t_n) - (obj.get_xt() * t_n) / SINCOS45)
                                print(x, y)
                                self.t.goto(int(x), int(y))
                                t_n += res
                        if self.guides:
                                self.t.color("#bbbbbb")
                                self.t.pensize(1)
                                xy_end = self.scale * ((obj.get_xt() * t_n) / SINCOS45)
                                self.t.goto(int(x), int(-xy_end))
                                self.t.goto(int(-xy_end), int(-xy_end))
                                self.t.goto(0, 0)
                                self.t.color("#000000")
                                self.t.pensize(2)
                self.resetpos()
        
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

#param = (0,2,.5)
#p = ParVec3D(1,1,1,2,2,2,param)
#q = ParVec3D(1,1,1,2,3,4,param)
#r = p.cross(q)
#s = ParVec3D(0,0,0,2,-2,2,param)
u = Vec3D(1,2,3)
v = Vec3D(1,1,10)
x = u.cross(v)
p = Point3D(-1,-1,-1)
a = Axis3D()
a.plot(u)
a.plot(v)
a.plot(x)
input()
