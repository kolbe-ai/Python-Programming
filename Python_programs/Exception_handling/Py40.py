"""
Create a custom exception. InvalidMarkError is raised when a
student’s mark is less than 0 or greater than 100. (use else and finally
blocks too.)
"""
class InvalidMarkError(Exception):
    pass

try:
    name = input("Enter the student name : ")
    mark = float(input("Enter the student name: "))
    if mark<0 or mark>100:
        raise InvalidMarkError
except InvalidMarkError:
    print("The mark should be between 0 and 100")
except ValueError:
    print("Type a valid mark")
else:
    print("\nStudent name : ",name,"\nMark : ",mark)
finally:
    print("\nProcess completed")