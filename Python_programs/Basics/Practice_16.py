#16. Print the star pyramid shown below (*, ***, ***** ... up to 11 stars). Take the number of lines from the user.

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()