#4. Read a string and display its length, its uppercase version, and whether it contains the letter ‘a’.

sent = input("Enter the string: ")
print("Length of string is: ",len(sent))
print("Upper is: ",sent.upper())
if 'a' in sent:
    print("a is in string")
else:
    print("a not in string")