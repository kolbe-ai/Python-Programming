"""
Design a class PasswordManager that stores a password.
The class should provide a method to update the password, but the update must happen only if the old password is correctly entered.
Also, ensure that the password cannot be accessed directly from outside the class.
"""

class PasswordManager:
    def __init__(self,password):
        self.__password = password
    def update(self,new_pass):
        check = input("Enter the current password: ")
        if (check == self.__password):
            self.__password = new_pass
            print("Password changed successfully")
        else:
            print("Incorrect password!")

#setting the password
password = PasswordManager("123456789")
#trying to change the password
password.update("1234567890")
