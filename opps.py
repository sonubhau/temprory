class Car:
    y = 10; # class variable
    z = 5; # class variable
    def __init__(self,x,y):
        self.x = x #Instance variable
        self.y = y #Instance variable
    def mul(self): # instance method
        return f"multiplication of ({self.x}) and ({self.y}) is ==>{self.x * self.y}"
    @classmethod
    def sub(cls):
        return (cls.y-cls.z)
c = Car(45,20)
print(c.mul())
print(c.sub())