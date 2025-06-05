from GeomExep import * 

##Angle class
class Angle:

#Init method
    def __init__(self,angle : int):

        if angle>360:
            raise SpecifRangeError(angle,Angle.spRange,Angle)
        elif angle<0:
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


    ##Class method
    def AllAdd(*selfs,total : int= 0):
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

    #Class method

#List convert angle object
class AngleList(Angle):

#Init
    def __init__(self, angles : list):
        if any(set(filter(lambda x : type(x)!=Angle,angles))):
            self.angles = []
            for i in angles:
                self.angles.append(Angle(i))
            self.num = len(angles)
        else:
            self.angles = angles
            self.num = len(angles)
#
    def __repr__(self):
        return f"{self.angles}"
    
    def __str__(self):
        return f"AngleList({self.angles})"
    
    def __getitem__(self,item):
        return self.angles[item]
    
    def AllAdd(li : list,total : int= 0):
        for i in li:
            total += i.angle
        return total

class EdgeList(Edge):
    
    def __init__(self, longs : list):
        if any(set(filter(lambda x : type(x)!=Edge,longs))):
            self.longs = []
            for i in longs:
                self.longs.append(Edge(i))
            self.num = len(longs)
        else:
            self.longs = longs
            self.num = len(longs)

    def __repr__(self):
        return f"{self.longs}"
    
    def __str__(self):
        return f"EdgeList({self.longs})"
    
    def __getitem__(self,item):
        return self.longs[item]

    def Pis(self):
        return ((self[0].long)**2+(self[1].long)**2)

#List convert angle object
Angle.quar = Angle(45)
Angle.rht = Angle(90)
Angle.strht = Angle(180)
Angle.comp  = Angle(360)