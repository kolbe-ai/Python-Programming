#13. Write a program to check whether a given year is a leap year.

year = int(input("Enter a year: "))
if( year % 400 == 0):
    print("The year is leap year!")
elif(year %100 == 0):
    print("The year is not leap year!")
elif(year%4 == 0):
    print("The year is leap year! ")
else:
    print("The year is not leap year!")
