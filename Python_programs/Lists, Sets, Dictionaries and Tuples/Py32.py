"""
Train Passenger Tracker
Write a program to manage a list of train passengers:
● Add passengers to the list.
● Cancel a ticket (remove a name).
● Display the current list sorted alphabetically.
● Check if a specific passenger has booked.
Concepts: List operations, append(), remove(), sort(), in .
"""

n = int(input("Enter the number of passengers: "))
passenger = []
for i in range (n):
    pass1 = input("Enter the passenger name: ")
    passenger.append(pass1)
print("Current list of sorted passenger is : ",sorted(passenger))
dlt = input("Enter the passenger name to cancel there ticket: ")
passenger.remove(dlt)

print("New list of sorted passenger is : ",sorted(passenger))
