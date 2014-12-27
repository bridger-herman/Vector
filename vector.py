import math
from draw import *

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
                
        def plot(self, axis):
                axis.t.up()
                # Go to x coordinate
                axis.t.left(45)
                axis.t.backward(axis.scale[0] * self.get_x())
                # Go to y coordinate
                axis.t.right(45)
                axis.t.forward(axis.scale[1] * self.get_y())
                # Go to z coordinate
                axis.t.left(90)
                axis.t.forward(axis.scale[2] * self.get_z())
                # Draw arrow
                axis.t.down()
                pos = axis.t.position()
                heading = math.degrees(math.atan(pos[1] / pos[0]))
                axis.t.setheading(heading + 45)
                axis.t.forward(6)
                axis.t.goto(*pos)
                axis.t.setheading(heading - 45)
                axis.t.forward(6)
                axis.t.goto(*pos)
                axis.t.goto(0, 0)
                
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


i = Vector3(5,2,3)
j = Vector3(4,5,6)
a = Axis(200)
i.plot(a)
input()























