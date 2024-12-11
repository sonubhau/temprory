# create a class name as car with two parameter brand and model with one 
# mathod name as fullname then create elecctercar class which inherit car class
# with battery capacity attribute
# Polymorphysm==> single method behave multiple way
#              Add fuel type method in both parent and child and that 
# return their respective fuel type

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} - {self.model}"
    def fuel_Type(self):
        return "disel And Petrol"
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
    def fuel_Type(self):
        return "electric charge"
    
e1 = ElectricCar("10Kwh" , "Mahindra" , "BE9")
print(e1.full_name())
print(e1.ele_full_name())
print(e1.fuel_Type())
c1 = Car("suziki","Grand Vitara")
print(c1.full_name())
print(c1.fuel_Type())