with open ("example.txt","w") as f:
    f.write("Hello how are you?\n")
    f.write("Good to see you!")

with open ("example.txt","r") as f:
    data = f.read()
print("Data is: ",data)

with open("example.txt","a") as f:
    f.write("Hi hi hi....!")
with open("example.txt","r") as f:
    data = f.read()
print("Data is: ",data)

f = open("example.txt","w")
f.write("Hello")
f.close()

f = open("example.txt","r")
print("Data is: ",f.read())
f.close()