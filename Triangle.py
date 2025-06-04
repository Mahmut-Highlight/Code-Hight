from Basic import Angle,Edge
from GeomExep import *
class Triangle(Angle,Edge):

    edgenum : list = [3,0]
    anglenum : list = [180,0]

    def __init__(self, angles : list ,edges : list):
        if len(angles)<3 or len(edges)<3:
            raise MissingValue((angles,edges),Triangle.edgenum[0],Triangle)
        elif Angle.AllAddList(angles)>180 or Angle.AllAddList(angles)<0:
            raise SpecifRange(angles,Triangle.anglenum,Triangle)

    
Triangle([45,90,45],[1,2,3])