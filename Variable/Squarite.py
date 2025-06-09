from math import sqrt

class SqRt:
    def __init__(self,root):
        self.image = ""+str(root)
        self.value = sqrt(root)

    def __str__(self):
        return f"SquareRoot({self.image})"
    
    def prifac(root , prli : list = [], pri : int = 2): ##Prime factors
        while root > pri:
            if root % pri == 0:
                prli.append(pri)
            pri += 1
        if len(prli) == 0 or root == 2:
            return prli
        return prifac(prli[-1],[prli])

    def startwith(lis):
        return startwith(lis[0])

startwith = SqRt.startwith
prifac = SqRt.prifac
r1 : SqRt = SqRt(32)
print(prifac(32)[0][::-1])