from Basic import *
from GeomExep import *
class Triangle:
    edgenum : int = 3
    anglenum : list = [180,0]

    def __init__(self, angles : AngleList ,edges : EdgeList):
        if angles.num!=3 or edges.num!=3:
            raise MissingValueError((angles,edges),Triangle.edgenum,Triangle)
        elif angles.AllAdd()<180:
            raise SpecifRangeError(angles,Triangle.anglenum,Triangle)
        else:
            self.angles = angles
            self.edges = edges

    def __repr__(self):
        return f"{self.angles},{self.edges}"
    
    def __str__(self):
        return f"Triangle({self.angles},{self.edges})"

    def __getitem__(self,keys):
        if keys == "angle":
            return self.angles
        elif keys == "edge":
            return self.edges
        else:
            raise FileNotFoundError(f"I am not found \"{keys}\"")

class Rectangle(Triangle):
    def __init__(self, angles : AngleList, edges : EdgeList):
        if not any(filter(lambda x : x.angle==90,angles)):
            raise NotSuitableObjectError(angles,Rectangle)
        #elif edges:
        #    raise
        else:
            super().__init__(angles,edges)

    def __repr__(self):
        return f"{self.angles},{self.edges}"

    def __str__(self):
        return f"Rectangle({self.angles},{self.edges})"

anl : AngleList = AngleList([45,90,45])
edl : EdgeList = EdgeList([4,3,5])
tr : Rectangle = Rectangle(anl,edl)
print(tr["edge"].Pis()**1/2)
#Triangle([45,90,45],[1,2,3])