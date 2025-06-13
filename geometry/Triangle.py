from Basic import *
class Triangle:
    edgenum : int = 3
    anglenum : list = [180,0]

##Apperance
    def __init__(self,edges : EdgeList, angles : AngleList ,enum : int = 3, inAngle : int = 180) -> None:
        self.angles = angles
        self.edges = edges

    def __repr__(self):
        return f"{self.angles},{self.edges}"
    
    def __str__(self):
        return f"Triangle({self.angles},{self.edges})"

    def __list__(self):
        return[self.edges,self.angles,]

    def __getitem__(self,keys):
        if keys == "angle" or keys == 0:
            return self.angles
        elif keys == "edge" or keys == 1:
            return self.edges
    
    def __iter__(self):
        for elm in list(zip(self.edges,self.angles)):
            return elm

##Class method
    def primeter(self):
        return self.edges.sum()

    def area(self,h):
        return h*self.edges[0]/2  
class Rectangle(Triangle):
    hipo : Angle = Angle(90)

##Apperance
    def __init__(self , edges : EdgeList, angles : AngleList = AngleList([])):
        super().__init__(edges.append(edges.pis()),angles.append(90),2,90)

    def __repr__(self):
        return f"{self.angles},{self.edges}"

    def __str__(self):
        return f"Rectangle({self.angles},{self.edges})"

##Class method
    def area(self):
        return super().area(self.edges[2])

if __name__ == "__main__":
    anl : AngleList = AngleList([45,45])
    edl : EdgeList = EdgeList([4,3])
    tr : Rectangle = Rectangle(edl,anl)
    for i in tr:
        print(i)
    #Triangle([45,90,45],[1,2,3])