from Basic import *
class Triangle:
    edgenum : int = 3
    anglenum : list = [180,0]

    def __init__(self,edges : EdgeList, angles : AngleList ,enum : int = 3, inAngle : int = 180) -> None:
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
            raise Exception(f"I am not found \"{keys}\"")

    def primeter(self):
        return self.edges.sum()

class Rectangle(Triangle):
    hipo : Angle = Angle(90)

    def __init__(self , edges : EdgeList, angles : AngleList = AngleList([])):
        super().__init__(edges.append(edges.pis()),angles.append(90),2,90)

    def __repr__(self):
        return f"{self.angles},{self.edges}"

    def __str__(self):
        return f"Rectangle({self.angles},{self.edges})"

    def area(self):
        return self.edges[2]*self.edges[0]/2   

if __name__ == "__main__":
    anl : AngleList = AngleList([45,45])
    edl : EdgeList = EdgeList([4,3])
    tr : Rectangle = Rectangle(edl,anl)
    print(tr)
    #Triangle([45,90,45],[1,2,3])