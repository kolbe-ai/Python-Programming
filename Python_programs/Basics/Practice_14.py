#14. Write a program to check whether a given number is an Armstrong number.

num = int(input("Enter the number: "))

dup = num
arm = 0
length = len(str(num))
while(dup > 0):
    last = dup%10
    arm +=pow(last,length)
    dup = dup//10
if(arm == num):
    print("The number is an armstrong number: ",num)
else:
    print("The number is not an armstrong number: ",num)