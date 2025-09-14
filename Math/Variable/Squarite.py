from math import sqrt

class SqRt:
    def __init__(self,root):
        self.image = "√"+str(root)
        self.value = sqrt(root)

    def __str__(self):
        return f"SquareRoot({self.image})"
    
    def startwith(lis):
        return startwith(lis[0])

class PrimeNum:
    def __init__(self ,root , prli : list = []): ##Prime factors
        pri : int = 2
        while root > pri:
            if root % pri == 0:
                prli.append(pri)
            pri += 1
        self.prime = prli

    def __str__(self):
        return f"Primes({str(self.prime)})"
    
    def __repr__(self):
        return str(self.prime)

    def inprime(self):
        if len(self.prime) == 0:
            return False
        return PrimeNum(self.prime[-1],[])
    
"""   Problem
    def findup(self):
        prl = []
        while self.prime:
            prl.append(self.prime[0])
            self.prime = self.findup()
        return prl
"""

startwith = SqRt.startwith
p1 : PrimeNum = PrimeNum(32)
print(p1.inprime())