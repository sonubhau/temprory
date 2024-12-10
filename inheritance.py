# create a class name as car with two parameter brand and model with one 
# mathod name as fullname then create elecctercar class which inherit car class
# with battery capacity attribute

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} - {self.model}"
c1 = Car("Tata","Nexon")
print(c1.full_name())
print(c1.brand)
print(c1.model)

class ElectricCar(Car):
    def __init__(self,battery_capacity,brand,model):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
    def ele_full_name(self):
        return f"{self.brand} - {self.model} ==>  {self.battery_capacity}"
    
e1 = ElectricCar("10Kwh" , "Mahindra" , "BE9")
print(e1.full_name())
print(e1.ele_full_name())