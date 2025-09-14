from Basic import *

class Square:
    edgenum: int = 4
    anglenum: list = [90, 90, 90, 90]

    ## Appearance
    def __init__(self, edge):
        self.edges = EdgeList([edge] * self.edgenum)
        self.angles = AngleList(Square.anglenum)

    def __repr__(self):
        return f"{self.angles}, {self.edges}"

    def __str__(self):
        return f"Square({self.angles}, {self.edges})"

    ## Class method
    def area(self):
        return self.edges[0].long ** 2

    def primeter(self):
        return self.edges.sum()
    
    def __getitem__(self, keys):
        if keys == "angle" or keys == 0:
            return self.angles
        elif keys == "edge" or keys == 1:
            return self.edges
    
    def __iter__(self):
        for i in range(self.edgenum):
            yield self.edges[i], self.angles[i]
    
    def __len__(self):
        return self.edgenum
    
if __name__ == "__main__":
    square = Square(5)
    print(square)
    print("Area:", square.area())
    print("Perimeter:", square.primeter())
    
    for e, a in square:
        print(f"Edge: {e}, Angle: {a}")