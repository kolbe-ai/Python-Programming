#23. Write a function that collects n numbers when it is called and prints those that are not multiples of 7.

def mul(num):
    for i in range(num):
        n = int(input("Enter the number: "))
        if(n%7 != 0):
            print("Number is: ",n)


num = int(input("Enter the number of iteration: "))
mul(num)
