"""
Write a Python program that performs various operations on a given
string. The program should:
a. Accept a string input from the user.
b. Print the first 3 characters of the string.
c. Print the last 3 characters of the string.
d. Print the string excluding the first and last characters.
e. Print the reverse of the string using slicing.
f. Find and display the length of the string.
g. Check whether a given substring is present in the main string.
"""
sent = input("Enter a sentence: ")
sub_sent = input("Enter a sentence: ")
print("First 3 characters of the string is: ",sent[:3])
print("Last 3 characters of the string is: ",sent[-3:])
print("Excluding first and last character of the string is: ",sent[1:-1])
print("Reversed string is: ",sent[::-1])
print("The length of the string is: ",len(sent))
if sub_sent in sent:
    print("The given substring is present in the main string")
else:
    print("The given substring is not present in the main string")

