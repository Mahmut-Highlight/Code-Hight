from GeomExep import * 
##Angle class
class Angle:
#Init method
    def __init__(self,angle : int):

        if angle<0:
            raise NegativeValueError(angle,Angle)
        else:
            self.angle = angle

#Important value
    spRange : list = [360,0]

    def __repr__(self):
        return f"{self.angle}"

    def __str__(self):
        return f"Angle({self.angle})"
    
    ##Operator method

    def __add__(self,other):
        return self.angle + other.angle

    def __sub__(self,other):
        return self.angle - other.angle

    def __mul__(self,other):
        return self.angle * other.angle
    
    def __truediv__(self, other):
        return self.angle / other.angle
    
    def __floordiv__(self, other):
        return self.angle // other.angle
    
    def __mod__(self, other):
        return self.angle % other.angle
    
    def __iadd__(self,other):
        return self.angle + other.angle

    def __isub__(self,other):
        return self.angle - other.angle

    def __imul__(self,other):
        return self.angle * other.angle
    
    def __itruediv__(self, other):
        return self.angle / other.angle
    
    def __ifloordiv__(self, other):
        return self.angle // other.angle
    
    def __imod__(self, other):
        return self.angle % other.angle

##Comparison magic methods

    def __gt__(self,other):
        if type(other)==int:
            return self.angle > other
        return self.angle > other.angle

    def __lt__(self,other):
        if type(other)==int:
            return self.angle < other
        return self.angle < other.angle

    def __eq__(self,other):
        if type(other)==int:
            return self.angle == other
        return self.angle == other.angle

    def __ne__(self,other):
        if type(other)==int:
            return self.angle != other
        return self.angle != other.angle

    ##Class method
    def sum(*selfs,total : int= 0):
        for i in selfs:
            total += i.angle
        return total

    def r90(self):
        return 80-self.angle

    def r180(self):
        return 180-self.angle

    def r360(self):
        return 360-self.angle

    def whicbig(self,other):
        if self.angle >= other.angle:
            return True
        else:
            return False

    def howa(self):
        if self.angle==360:
            return 3
        elif self.angle>180:
            return 2
        elif self.angle>90:
            return 1
        elif self.angle>0:
            return 0

class Edge:
    #Init method
    def __init__(self,long):
        if long<0:
            raise NegativeValueError(long,Edge)
        else:
            self.long = long

    def __str__(self):
        return f"Edge({self.long})"
    
    def __repr__(self):
        return f"{self.long}"
    
    ##Operator method

    def __add__(self,other):
        return self.long + other.long

    def __sub__(self,other):
        return self.long - other.long

    def __mul__(self,other):
        return self.long * other.long
    
    def __truediv__(self, other):
        return self.long / other.long
    
    def __floordiv__(self, other):
        return self.long // other.long
    
    def __mod__(self, other):
        return self.long % other.long
    
    def __iadd__(self,other):
        return self.long + other.long

    def __isub__(self,other):
        return self.long - other.long

    def __imul__(self,other):
        return self.long * other.long
    
    def __itruediv__(self, other):
        return self.long / other.long
    
    def __ifloordiv__(self, other):
        return self.long // other.long
    
    def __imod__(self, other):
        return self.long % other.long
##Comparison magic methods

    def __gt__(self,other):
        return self.long > other.long

    def __lt__(self,other):
        return self.long < other.long

    def __eq__(self,other):
        return self.long == other.long

    def __ne__(self,other):
        return self.long != other.long

    #Class method

#List convert angle object
class AngleList:

#Init
    def __init__(self, angles : list):
        self.angles = []
        for i in angles:
            self.angles.append(Angle(i))
        self.num = len(angles)
#
    def __repr__(self):
        return f"{self.angles}"
    
    def __str__(self):
        return f"AngleList({self.angles})"
    
    def __getitem__(self,item):
        return self.angles[item]

##Operator
    def __iadd__(self,other):
        if type(other) == list:
            return self.angles + other
        if type(other) == Angle:
            return self.angles + other
        return self.angles + other.angles

##Method

    def sum(self,total : Angle = 0):
        for angl in self:
            total += angl.angle
        return total

    def append(self,*other):
        for element in other:
            self.angles.append(Angle(element))
        return self

class EdgeList(Edge):
    
    def __init__(self, longs : list):
        self.longs = []
        for i in longs:
            self.longs.append(Edge(i))
        self.num = len(longs)

    def __repr__(self):
        return f"{self.longs}"
    
    def __str__(self):
        return f"EdgeList({self.longs})"
    
    def __getitem__(self,item):
        return self.longs[item]

#Method
    def append(self,*other):
        for element in other:
            self.longs.append(Angle(element))
        return self

    def Pis(self):
        return int(((self[0].long)**2+(self[1].long)**2)**0.5)

#List convert angle object
any = 0
quar = 45
rht = 90
strht = 180
comp  = 360
#Anl = AngleList([quar,quar])
#nl.append(90)
#rint(Anl.sum())