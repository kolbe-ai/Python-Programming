"""
Take a list index from the user and handle IndexError. What’s the difference between except: and except Exception:?
"""

try:
    numbers = input("Enter the numbers with space: ")
    num = list(map(int,numbers.split()))
    print(num)
    index = int(input("Enter the possition to access: "))
    print(num[index])
except IndexError:           #catch IndexError
    print("Error: Invalid Index")
except Exception:              #catch every other error
    print("Error: Error occured!")
else:
    print("Ran sucessfully")
finally:
    print("Process Completed!")