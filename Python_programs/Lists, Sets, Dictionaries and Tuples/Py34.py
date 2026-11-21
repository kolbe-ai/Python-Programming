"""
Write a program that takes two sets of numbers as input and
performs the union, intersection, difference, and symmetric difference
operations, then displays the results. (Do it in both way using operators
and functions for the set operations.)
"""

set_a = set(map(int,input("Enter the numbers in set a: ").split()))
print(set_a)
set_b = set()
num = input("Enter the number in set b: ")
for i in num.split():
    set_b.add(int(i))
print(set_b)
print("\n\n|--- Using set operation ---|")
print(f"A UNION B : {set_a.union(set_b)}")
print("A INTERSECTION B : ",set_a.intersection(set_b))
print("A - B : ",set_a.difference(set_b))
print("A symmetric B",set_a.symmetric_difference(set_b))


print("\n\n|--- Using operators ---|")
print(f"A UNION B : {set_a|set_b}")
print("A INTERSECTION B : ",set_a & set_b)
print("A - B : ",set_a - set_b)
print("A symmetric B",set_a ^ set_b)
