"""
34. Take two sets of numbers and perform union, intersection, difference and symmetric difference.
Do it both ways: with operators and with set methods.
"""

setA= {1,2,3,4,5}
setB = {3,4,5,6,7}

#using operators
print("Union of both set is: ",setA|setB)
print("Intersection of both set is: ",setA&setB)
print("setA - setB: ",setA-setB)
print("Symetric difference: ",setA^setB)

#using set methods
print("\n\n")
print("Union of both set is: ",setA.union(setB))
print("Intersection of both set is: ",setA.intersection(setB))
print("setA - setB: ",setA.difference(setB))
print("Symetric difference: ",setA.symmetric_difference(setB))