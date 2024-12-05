list_1 = ["Black","Ginger","Lemon","Green","Milk"]
len=(len(list_1))
print(len)
print(list_1[len-1])
print(list_1[-1])  
list_1[2] ="Herbal"
# list_1[1:2] = "Herbal"   DOnt do like your optput will be not Expected
# ['Black', 'H', 'e', 'r', 'b', 'a', 'l', 'Herbal', 'Green', 'Milk']
# we need to pass like 
list_1[1:2] = ["Masala"]  #Array
print(list_1)
#  Replace two value At A time
# list_1[0:2] = ["Green","Green"]
# print(list_1)
list_1[2:2] = ["test","test"]
print(list_1) #['Black', 'Masala', 'test', 'test', 'Herbal', 'Green', 'Milk']
# Deleting 2 & 3 positinal element
list_1[2:4] = [] #empty array
print(list_1)
