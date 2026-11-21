"""
Write a program that performs the following operations using tuples:
a. Create a tuple named cities that contains the names of five
different cities.
b. Print the entire tuple of cities.
c. Access and display:
d. The second city in the tuple.
e. The last city in the tuple using negative indexing.
f. Unpack the tuple into individual variables and print each city.
g. Ask the user to input a city name, and check whether that city is
present in the tuple using the in operator. Display an appropriate
message.
"""
cities = ("Thrissur","Eranakulam","Kollam","Kozhikodu","Alapuzha")
print(f"All cities is: {cities}")
print(f"Second city is: {cities[1]}")
print(f"Last city is: {cities[-1]}")

city1,city2,city3,city4,city5 = cities
print(f"The cities using unpack is: {city1},{city2},{city3},{city4},{city5}")

search = input("Enter the city name to search: ")
if search in cities:
    print(f"The city {search} is found in cities")
else:
    print(f"The city {search} not found in cities")