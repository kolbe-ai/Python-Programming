#17. Print the letter pattern (A, A B, A B C ... up to A B C D E F G). Take the number of lines from the user.

n = int(input("Enter the number of lines: "))


for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range (i*2-1):
        print(chr(65+k),end="")
    print()