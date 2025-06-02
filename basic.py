##Angle
class Angle:
    Symbol : dict = {
        "angle" : "°",
        "right" : "⟂",
        "angleI" : "⦟"
    }
    angleType : dict = {
        "acute" : [0,"less90"],
        "right" : [1,"90"],
        "Obtuse" : [2,"less180"],
        "straight" : [3,"180"]
    }
    rht : int = 90
    strht : int = 180
    comp : int = 360

    def __init__(self,angle : int):
        if not(angle<0) and not(angle>360):
            self.angle = angle
        else:
            raise Exception("an angle is can not less zero")

    def rema90(self):
        return 80-self.angle

    def rema180(self):
        return 180-self.angle

    def rema360(self):
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
        else:
            raise Exception("Not find angle")

class Side:
    pass
