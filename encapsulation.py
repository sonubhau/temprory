# Encapsulation ==>restrict the access of variable or method within 
# a class & for outside class its not accesseble 
# (i.e = for class object || Instance) 
# Exa => private brand variable || Attribute and write getter mehod to access

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand + "!"
    def full_name(self):
        return f"{self.__brand} - {self.model}"
c1 = Car("Tata","Nexon")
print(c1.full_name())
# print(c1.__brand) Its not accesseble as a varible at instance
print(c1.get_brand())
print(c1.model)

