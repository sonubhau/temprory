class Car:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mul(self):
        return f"multiplication of ({self.x}) and ({self.y}) is ==>{self.x * self.y}"
    
c = Car(45,20)
print(c.mul())