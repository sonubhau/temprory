num_list = "0123456789"
print(num_list[:]) #0123456789
print(num_list[:6])#0123456789
print(num_list[-1])#0123456789
print(num_list[3:])#3456789
print(num_list[0:7:2])#0246
print(num_list[0:7:3])#036
print(num_list[-2:])#012345678
print(num_list[::2])#0123456789

# Conversion of String to list on <,> Seperatrd value [.split()]
student_name = "sonu, monu, ram, mithesh"
print(student_name.split()) #['sonu,', 'monu,', 'ram,', 'mithesh']
print(student_name.split(", ")) #['sonu', 'monu', 'ram', 'mithesh']
# ********************************************************************
# *********************************************************************
name = 'Mithesh'
chai_type = "Masala"
quantity = 2
order = " {} ordered {} cup of {} tea"
var = order.format(name,quantity,chai_type)
print(var)
# *********************************************
#  Conversion of list to string
# ********************************************************
list_chai_type = ["Masala","Ginger","Lemon","Black"]
str_chai_type = ", ".join(list_chai_type)
print(str_chai_type)
# ****************************************************************************
#  Unicode Escaping <\> And row String <r>
# *******************************************************************
chai = "He said, \"Masala tea is awsome\"!" #He said, "Masala tea is awsome"!
print(chai)
chai_1 = r"c:\mithesh\sonu" # c:mithesh\sonu
print(chai_1)