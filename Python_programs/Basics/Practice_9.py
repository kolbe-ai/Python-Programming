"""
9. Read a name (string), age (integer) and GPA (float), and display them in the sample format “Hello John, you are 20 years old,
and your GPA is 3.75” using four methods:
(a) string concatenation,
(b) str.format(),
(c) f-strings,
(d) % formatting.
"""

name = input("Enter the name: ")
gpa = float(input("Enter the GPA: "))
age = int(input("Enter the age: "))

#a
print("\n\nName: "+name+"\nAge: "+str(age)+"\nGPA: "+str(gpa))

#b
print("\n\nName: {}\nAge: {}\nGPA: {}".format(name,age,gpa))

#c
print(f"\n\nName: {name}\nAge: {age}\nGPA: {gpa}")

#d
print("\n\nName: %s \nAge: %d \nGPA: %f "%(name,age,gpa))