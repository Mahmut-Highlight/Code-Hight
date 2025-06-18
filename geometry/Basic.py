from GeomExep import * 
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

    def __int__(self):
        return int(self.angle)

    def __float__(self):
        return float(self.angle)

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
    def sum(*sel,total : int= 0):
        for i in sel:
            total += i.angle
        return total

    def r90(self):
        return 80-self.angle

    def r180(self):
        return 180-self.angle

    def r360(self):
        return 360-self.angle

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
    
    def __int__(self):
        return int(self.long)

    def __float__(self):
        return float(self.long)

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
        if type(other)==int:
            return self.long > other
        return self.long > other.long

    def __lt__(self,other):
        if type(other)==int:
            return self.long < other
        return self.long < other.long

    def __eq__(self,other):
        if type(other)==int:
            return self.long == other
        return self.long == other.long

    def __ne__(self,other):
        if type(other)==int:
            return self.long != other
        return self.long != other.long

    #Class method

    def pis(self,other):
        return (self.long**2+other.long**2)**0.5

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
    
    def __list__(self):
        return self.angles
    
    def __getitem__(self,item):
        return self.angles[item]

    def __iter__(self):
        return iter(self.angles)
    
    def __next__(self):
        return next(self.angles)

##Operator
    def __add__(self,other):
        return list(map(lambda x: x.angle + other,self.angles))

    def __sub__(self,other):
        return list(map(lambda x: x.angle - other,self.angles))

    def __mul__(self,other):
        return list(map(lambda x: x.angle * other,self.angles))
    
    def __truediv__(self, other):
        return list(map(lambda x: x.angle / other,self.angles))
    
    def __floordiv__(self, other):
        return list(map(lambda x: x.angle // other,self.angles))
    
    def __mod__(self, other):
        return list(map(lambda x: x.angle % other,self.angles))
    
    def __pow__(self,other):
        return list(map(lambda x: x.angle ** other,self.angles))
    
    def __iadd__(self,other):
        return list(map(lambda x: x.angle + other,self.angles))

    def __isub__(self,other):
        return list(map(lambda x: x.angle - other,self.angles))

    def __imul__(self,other):
        return list(map(lambda x: x.angle * other,self.angles))
    
    def __itruediv__(self, other):
        return list(map(lambda x: x.angle / other,self.angles))
    
    def __ifloordiv__(self, other):
        return list(map(lambda x: x.angle // other,self.angles))
    
    def __imod__(self, other):
        return list(map(lambda x: x.angle % other,self.angles))

##Method

    def sum(self,total : int = 0):
        for angl in self:
            total += angl.angle
        return total

    def append(self,*other):
        for element in other:
            self.angles.append(Angle(element))
        return self

    def insert(self, index,other):
        self.angles.insert(index, Angle(other))
        return self

class EdgeList:
    """
    Edge List use for a many edge.
    """
    def __init__(self, longs : list):
        self.longs = []
        for i in longs:
            self.longs.append(Edge(i))
        self.num = len(longs)

    def __repr__(self):
        return f"{self.longs}"
    
    def __str__(self):
        return f"EdgeList({self.longs})"
    
    def __list__(self):
        return self.angles
    
    def __getitem__(self,item):
        return self.longs[item]

    def __iter__(self):
        return iter(self.longs)

    def __next__(self):
        return next(self.longs)

##Operator
    def __add__(self,other):
        return list(map(lambda x: x.long + other,self.longs))

    def __sub__(self,other):
        return list(map(lambda x: x.long - other,self.longs))

    def __mul__(self,other):
        return list(map(lambda x: x.long * other,self.longs))
    
    def __truediv__(self, other):
        return list(map(lambda x: x.long / other,self.longs))
    
    def __floordiv__(self, other):
        return list(map(lambda x: x.long // other,self.longs))
    
    def __mod__(self, other):
        return list(map(lambda x: x.long % other,self.longs))
    
    def __pow__(self,other):
        return list(map(lambda x: x.long ** other,self.longs))
    
    def __iadd__(self,other):
        return list(map(lambda x: x.long + other,self.longs))

    def __isub__(self,other):
        return list(map(lambda x: x.long - other,self.longs))

    def __imul__(self,other):
        return list(map(lambda x: x.long * other,self.longs))
    
    def __itruediv__(self, other):
        return list(map(lambda x: x.long / other,self.longs))
    
    def __ifloordiv__(self, other):
        return list(map(lambda x: x.long // other,self.longs))
    
    def __imod__(self, other):
        return list(map(lambda x: x.long % other,self.longs))

#Method
    def append(self,*other):
        for element in other:
            self.longs.append(Edge(element))
        return self
    
    def insert(self, index,other):
        self.longs.insert(index, Edge(other))
        return self

    def pis(self):
        return self[0].pis(self[1])

    def sum(self,total : int = 0):
        for angl in self:
            total += angl.long
        return total

    def sin(self,st=0):
        return self[st]/self[-1]

#List convert angle object
any = 0
quar = 45
rht = 90
strht = 180
comp  = 360
if __name__ == "__main__":
    Edl : EdgeList = EdgeList([3,4,5])
    Anl : AngleList = AngleList([45,45,90])
    for i in Edl:
        print(i)
    for i in Anl:
        print(i)