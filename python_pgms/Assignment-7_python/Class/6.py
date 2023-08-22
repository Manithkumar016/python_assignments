
# 6) Write a Python class to implement pow(x, n) 

class Power:
    def __init__(self,x,n) -> None:
        self.x=x
        self.n=n 
    def power(self):
        y=1
        for i in range(self.n):
            y=y*self.x
        print(f"{self.x} to the power of {self.n} is:{y}")

p =Power(4,2)
p.power()