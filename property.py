#  @ prorerty  decorator is use to make varriable read only once we declare 
# at level of constructor then we are not able change again
# Step 1 ==> make variable private using (__)
# Step 2 ==> write method to access that decorator with @property decorator

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model
        Car.total_car +=1
    def full_name(self):
        return f"{self.brand} - {self.__model}"
    @property
    def readmodel(self):
        return self.__model
c1 = Car("Tata","Nexon")
print(c1.full_name())
# print(c1.__model)  ..........This variable not accessable with class object
print(c1.readmodel)
c2 = Car("Toyata","Figo")
c3 = Car("Jagwar","lamborgini")
print(c2.full_name())
print(c1.total_car) #Both the way we can access total_car object but the best
print(Car.total_car) # way using class name.classvariable