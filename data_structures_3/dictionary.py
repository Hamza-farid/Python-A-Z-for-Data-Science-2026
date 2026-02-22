# here we use keys

dict={"x":1,"y":2,"z":3}
print(dict["x"])  # access value by key

# dict also mutable

dict["x"]=10  # update value by key
print(dict)


my_dict={"x":1,"y":2,"z":3,
         "demo":{"aa":10,"bb":20}}
print(my_dict["demo"])  # access nested dictionary by key
print(my_dict["demo"]["aa"])  # access nested dictionary value by key