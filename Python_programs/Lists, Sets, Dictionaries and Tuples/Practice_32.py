"""
32. (Train Passenger Tracker) Manage a passenger list:
add passengers, cancel a ticket (remove a name), display the list sorted alphabetically, and check whether a particular passenger has booked.
"""

train = []
name = input("Enter the passenger: ")               #inputing
train.append(name)
name = input("Enter the passenger: ")
train.append(name)
name = input("Enter the passenger: ")
train.append(name)
name = input("Enter the name of the passenger to DELETE: ")
if name in train:               #removing
    train.remove(name)
else:
    print("Name NOT FOUND!")
print("Passengers are: ",sorted(train))         #sorting
name = input("Enter the passenger name to search: ")
if name in train:                   #searching
    print("Passenger FOUND!")
else:
    print("Passenger NOT FOUND!")