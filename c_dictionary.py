tea_types = {
    "Masala":"Spicy","Ginger":"Hot","Black":"Bitter","Lemon":"Sweet","Coffie":"Strong"
}
# *******Two way to Access Value********************
print(tea_types["Ginger"]) # we will get error if key not present
print(tea_types.get("Black"))# we will get None if key not present

keys= ["Masala","Ginger","Black"]
values = ["Good","Better","Best"]
new_dict = {}
for key in keys:
    print("round "+key )
    for val in values:
        new_dict[key] = val
        print(new_dict)
        values.remove(val)
        print(values)
        break

print(new_dict)

        
    
        

   
