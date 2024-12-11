class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car +=1
    def full_name(self):
        return f"{self.brand} - {self.model}"
c1 = Car("Tata","Nexon")
print(c1.full_name())
print(c1.brand)
c2 = Car("Toyata","Figo")
print(c2.full_name())
print(c1.total_car) #Both the way we can access total_car object but the best
print(Car.total_car) # way using class name.var