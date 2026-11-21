"""
(Encapsulation: Data Hiding) [PDF Q55] Build a Locker class where change_pin(old, new) works only if old is correct.
"""

class Locker:
    old_pass = "Hello123"
    def change_pin(self,old_pass1,new_pass):
        if (self.old_pass == old_pass1):
            self.old_pass = new_pass
            print("Correct pin\nAccess granted!")
        else:
            print("Incorrect pin\nAccess not granted!")

l = Locker()
o_pass = input("Enter the old password: ")
n_pass = input("Enter the new password: ")
l.change_pin(o_pass,n_pass)