#40. Create a custom exception InvalidMarkError, raised when a mark is below 0 or above 100. Also use else and finally blocks.

class InvalidMarkError (Exception):
    pass

try:
    mark = int(input("Enter you age (0-100): "))
    if(mark >100 or mark < 0):
        raise InvalidMarkError
    else:
        print("You mark is",mark)
except InvalidMarkError:
    print("Error: Invalid mark")



