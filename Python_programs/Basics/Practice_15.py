#15. Write a program to check whether a given number is a palindrome.

num = int(input("Enter a number: "))
palin = 0
dup = num
count = len(str(num))

while(dup>0):
    last = dup%10
    palin = palin*10 + last
    dup = dup//10
if (num == palin):
    print("The number is palindrome")
else:
    print("The number is not palindrome")