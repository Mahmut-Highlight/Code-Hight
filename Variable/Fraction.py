class Fraction:
    def __init__(self,nume,deno : int = 1):
        self.nume = nume ##pay
        self.deno = deno ##payda
    
    def __repr__(self):
        return f"{self.nume}/{self.deno}"
    
    def __str__(self):
        return f"{self.nume}\n=\n{self.deno}"
    
    def equal(self,other):
        if self.deno == other.deno:
            return 1
        
    def __add__(self,other):
        if self.equal(other):
            return self.nume+other.nume,self.deno

if __name__ == "__main__":
    print(Fraction(1)+Fraction(3))