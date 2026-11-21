"""
55. Design a PasswordManager class that stores a password and lets it be updated only if the old password is entered correctly.
The password must not be directly accessible from outside the class.
"""

class PasswordManager:
    def set_pass(self,password):
        self.__password = password
    def change_pass(self,oldpass):
        if (self.__password == oldpass):
            self.__password = input("Enter your new password: ")
        else:
            print("Wrong password!")


password = input("Enter your password: ")
p = PasswordManager()
p.set_pass(password)
new = int(input("Enter 1 to change password \nEnter 0 to not change password\n\nEnter you choice: "))
if (new == 1):
    pass_ = input("Enter your password: ")
    p.change_pass(pass_)
