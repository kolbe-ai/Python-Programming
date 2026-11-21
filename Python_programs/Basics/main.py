line = int(input("Enter the number of lines: "))
for i in range(0,line):
    print(" "*(line-i-1),end="")
    for j in range(0,i+1):
        print(chr(65+j),end = " " )
    print()
