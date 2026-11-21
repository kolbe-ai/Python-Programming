"""
36. Read a string and perform these operations:
(a) Accept a string input from the user.
(b) print the first 3 characters,
(c) print the last 3,
(d) print the string without its first and last characters,
(e) print the reverse using slicing,
(f) display its length,
(g) check whether a given substring is present.
"""
#a
sent = input("Enter your sentence: ")
#b
print("First 3 character is: ",sent[:3])
#c
print("Last 3 character is: ",sent[-3:])
#d
print("Without first and last character is: ",sent[1:-1])
#e
print("Reversed string is: ",sent[::-1])
#f
print("Length of the string is: ",len(sent))
#g
check_string = input("Enter the string to check: ")
if check_string in sent:
    print("Check String found in the main String")
else:
    print("Check String not found in the main String")