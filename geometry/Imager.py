from turtle import Turtle
from Triangle import Rectangle, EdgeList,AngleList,Triangle
class ImagerShape:
    def __init__(self , shape : object , turtle : Turtle = Turtle(), color : str = "black", size : int = 1):
        self.shape = shape
        self.color = color
        self.size = size
        self.turtle = turtle

    def color(self, color : str):
        self.color = color
    
    def size(self, size : int):
        self.size = size
    
    def draw(self):
        self.turtle.color(self.color)
        self.turtle.pensize(self.size)
        for e,a in zip(self.shape["edge"], self.shape["angle"]):
            self.turtle.forward(e.long)
            self.turtle.left(a.r180())
        self.turtle.stamp()

if __name__ == "__main__":
    re : Triangle = Triangle(EdgeList([100, 100,100]), AngleList([60, 60, 60]))
    turt = Turtle(visible=False)
    ImagerShape(re, turt, "black", 4).draw()