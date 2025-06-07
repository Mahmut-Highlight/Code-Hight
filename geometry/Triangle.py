from Basic import *
from GeomExep import *
class Triangle:
    edgenum : int = 3
    anglenum : list = [180,0]

    def __init__(self, angles : AngleList ,edges : EdgeList,enum : int = 3, inAngle : int = 180) -> None:
        if angles.num!=enum or edges.num!=enum:
            raise MissingValueError((angles,edges),Triangle.edgenum,Triangle)
        elif angles.sum()<inAngle:
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
    hipo : Angle = Angle(90)

    def __init__(self, angles : AngleList, edges : EdgeList):
        super().__init__(angles.append(90),edges.append(edges.Pis()),2,90)

    def __repr__(self):
        return f"{self.angles},{self.edges}"

    def __str__(self):
        return f"Rectangle({self.angles},{self.edges})"


anl : AngleList = AngleList([45,45])
edl : EdgeList = EdgeList([4,3])
tr : Rectangle = Rectangle(anl,edl)
print(tr)
#Triangle([45,90,45],[1,2,3])