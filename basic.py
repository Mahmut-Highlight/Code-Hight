##Angle class
from GeomExep import * 

class Angle:
#Important value
    spRange : list = [360,0]
    quar : int = 45
    rht : int = 90
    strht : int = 180
    comp : int = 360

#Init method
    def __init__(self,angle : int):

        if angle>360:
            raise SpecifRange(angle,Angle.spRange,Angle)
        elif angle<0:
            raise NegativeValue(angle,Angle)
        else:
            self.angle = angle

    def __repr__(self):
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

    def rema90(self):
        return 80-self.angle

    def rema180(self):
        return 180-self.angle

    def rema360(self):
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
    #Import value
    lo : str = "a"
    lo1 : str = "2a"
    lo3 : str = "a√2"
    lo4 : str = "a√3"

    #Init method
    def __init__(self,long: int,thick : int = 1):
        if long<0:
            raise NegativeValue(long,Edge)
        elif  thick<0:
            raise NegativeValue(thick,Edge)
        else:
            self.long = long
            self.thick = thick

    def __repr__(self):
        return f"Edge({self.long},{self.thick})"
    
    ##Operator method

    def __add__(self,other):
        return [self.long + other.long,[self.thick,other.thick]]

    def __sub__(self,other):
        return [self.long - other.long,[self.thick,other.thick]]

    def __mul__(self,other):
        return [self.long * other.long,[self.thick,other.thick]]
    
    def __truediv__(self, other):
        return [self.long / other.long,[self.thick,other.thick]]
    
    def __floordiv__(self, other):
        return [self.long // other.long,[self.thick,other.thick]]
    
    def __mod__(self, other):
        return [self.long % other.long,[self.thick,other.thick]]
    
    def __iadd__(self,other):
        return [self.long + other.long,[self.thick,other.thick]]

    def __isub__(self,other):
        return [self.long - other.long,[self.thick,other.thick]]

    def __imul__(self,other):
        return [self.long * other.long,[self.thick,other.thick]]
    
    def __itruediv__(self, other):
        return [self.long / other.long,[self.thick,other.thick]]
    
    def __ifloordiv__(self, other):
        return [self.long // other.long,[self.thick,other.thick]]
    
    def __imod__(self, other):
        return [self.long % other.long,[self.thick,other.thick]]

    #Class method


if __name__ == "__main__":
    #an : Angle = Angle(90)
    #an2 : Angle = Angle(45)
    s1 = Edge(10)
    s2 = Edge(20,12)
    print(s1+s2)