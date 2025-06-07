class Number:
    def __init__(self,number)-> None:
        if type(number) == float:
            number : list = str(number).split(".")
            self.value,self.up = Number.nummag(number[0],number[1])
        else:
            self.value,self.up = number,"10^0"

    def nummag(num : str,con : str ,tr : int = 0):
        if num == "":
            return (con,f"10^-{tr}")
        con = num[-1]+con
        return Number.nummag(num[:-1],con,tr+1)
    
    def getUp(self):
        return tuple(map(lambda x: int(x),self.up.split("^")))

    def upEqual(self,other):
        sup = self.getUp()
        oup = other.getUp()
        if sup == oup:
            return 0
        else:
            return sup[1]-oup[1]

    def __str__(self) -> str:
        return f"{self.value} x {self.up}"
    
class Decimal:
    def __init__(self, number) -> None:
        number : list = str(number).split(".")
        self.value,self.up = Number.nummag(number[0],number[1])

    def __str__(self) -> str:
        return f"{self.value} x {self.up}"

n = Number(1.12)
n1 = Number(232)
print(n,n1)
print(n1.upEqual(n))