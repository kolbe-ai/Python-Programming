"""
37. Tuple operations:
(a) create a tuple cities with five cities,
(b) print it,
(c) display the second city,
(d) display the last city using negative indexing,
(e) unpack it into separate variables and print each,
(f) ask the user for a city name and use in to check whether it is in the tuple, showing a suitable message.
"""
#a
cities = ("Delhi","Mumbai","Kerala","Assam","Karnataka")
#b
print(cities)
#c
print("Second city is: ",cities[1])
#d
print("Last city is: ",cities[-1])
#e
a,b,c,d,e = cities
print("Unpacked cities: ",end=" ")
print(a,end=", ")
print(b,end=", ")
print(c,end=", ")
print(d,end=", ")
print(e)

#print("Cities are: ",*cities)
#f
check = input("Enter the city to search: ")
if check in cities:
    print("The city is found!")
else:
    print("The city is not found!")