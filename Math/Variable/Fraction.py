class Fraction:
    def __init__(self,nume,deno : int = 1) -> None:
        self.nume = nume ##pay
        self.deno = deno ##payda
    
    def __repr__(self) -> str:
        return f"{self.nume}/{self.deno}"
    
    def __str__(self) -> str:
        return f" {self.nume}\n===\n {self.deno}"
    
    def __int__(self) -> int:
        return self.nume//self.deno
    
    def __float__(self) -> float:
        return self.nume/self.deno

##Operator

    def __add__(self,other):
        if type(other)== int or self.deno == other.deno:
            return Fraction(self.nume+other,self.deno)
        return self.sum(other)

    def __sub__(self,other):
        if type(other) == int or self.deno == other.deno:
            return Fraction(self.nume-other,self.deno)
        return self.sub(other)
    
    def __mul__(self,other):
        if type(other)== int:
            return Fraction(self.nume*other,self.deno)
        return Fraction(self.nume*other.nume,self.deno*other.deno)
        

    """def __truediv__(self, other):
        return Fraction(self.nume/other,self.deno*other)
    
    def __floordiv__(self, other):
        return Fraction(self.nume//other,self.deno*other)
    
    def __mod__(self, other):
        return Fraction(self.nume%other,self.deno*other)"""
    
    def __pow__(self,other):
        return Fraction(self.nume**other,self.deno**other)

##Class method
    def sum(self,other):
        return Fraction(self.nume*other.deno+self.deno*other.nume,self.deno*other.deno)
    
    def sub(self,other):
        return Fraction(self.nume*other.deno-self.deno*other.nume,self.deno*other.deno)

    def equal(self,other) -> bool | int:
        if self.deno == other.deno:
            return 1
        return 0

if __name__ == "__main__":
    print(int(Fraction(4,2))) ## Error