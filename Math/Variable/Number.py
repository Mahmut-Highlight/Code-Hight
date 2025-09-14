class strint:
    def __init__(self, value : str | int):
        self.value = str(value)
    
    def __repr__(self):
        return self.value
    
    def __str__(self):
        return f"{self.value}"

    def __int__(self) -> int:
        return int(self.value)

    def __add__(self,other):
        return strint((int(self) + int(other)))

    def __sub__(self,other):
        return strint((int(self) - int(other)))
    
    def __mul__(self,other):
        return strint((int(self) * int(other)))
    
    def __truediv__(self,other):
        return strint((int(self) / int(other)))
    
    def __floordiv__(self,other):
        return strint((int(self) // int(other)))
    
    def __mod__(self,other):
        return strint((int(self) % int(other)))

    def __pow__(self,other):
        return strint((int(self) ** int(other)))

    def __eq__(self,other):
        return self.value == other.value

class decimal:
    def __init__(self, number, up : int = 0) -> None:
        number : list = str(number).split(".")
        self.value,self.up = decimal.nummag(number[0],number[1])

    def __str__(self) -> str:
        return f"{self.value} x {self.up}"
    
    def getup(self):
        return list(map(lambda x: int(x),self.up.split("^")))

    def nummag(num : str,con : str ,tr : int = 0):
        if num == "":
            return (con,f"10^{len(con)-tr}")
        con = num[-1]+con
        return decimal.nummag(num[:-1],con,tr+1)

    def left(self,amount : int = 1):
        ups = self.getup()
        self.value = float(self.value) / (10**(amount))
        ups[1] -= amount
        self.up = "^".join(list(map(lambda x: str(x),ups)))
        del ups
        return self

    def right(self,amount : int = 1):
        ups = self.getup()
        self.value = float(self.value) * (10**(amount))
        ups[1] += amount
        self.up = "^".join(list(map(lambda x: str(x),ups)))
        del ups
        return self

    def upEqual(self,other): ##Up is equal
        sup = self.getup()[1]
        oup = other.getup()[1]
        if sup == oup:
            return 0
        else:
            return sup-oup

    def allin(self):
        return self.getup()[0]**-self.getup()[1]

    def __add__(self,other):
        if not upEqual(self,other):
            return decimal(int(self.value)+int(other.value)*self.getup())


upEqual = decimal.upEqual
if __name__ == "__main__":
    #n = decimal(11.12)
    #n1 = decimal(23.2)
    si = strint("5")
    si1 = strint("25")
    print(si)
    print(si**si) ##!!error
    #print(n.allin())