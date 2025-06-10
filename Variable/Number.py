class Decimal:
    def __init__(self, number, up : int = 0) -> None:
        number : list = str(number).split(".")
        self.value,self.up = Decimal.nummag(number[0],number[1])

    def __str__(self) -> str:
        return f"{self.value} x {self.up}"
    
    def getup(self):
        return list(map(lambda x: int(x),self.up.split("^")))

    def nummag(num : str,con : str ,tr : int = 0):
        if num == "":
            return (con,f"10^{len(con)-tr}")
        con = num[-1]+con
        return Decimal.nummag(num[:-1],con,tr+1)

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
            return Decimal(int(self.value)+int(other.value)*self.getup())


upEqual = Decimal.upEqual
n = Decimal(11.12)
n1 = Decimal(23.2)
print(n.allin())