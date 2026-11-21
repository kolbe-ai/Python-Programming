"""
42. Demonstrate the file modes r, w, x and a.
Perform a suitable operation for each, show the result or
error message using exception handling, and keep the same file name throughout.
"""

try:
 with open("example.txt","r") as f:
  pass
 with open("example.txt","w") as f:
  pass
 with open("example.txt","x") as f:
  pass
 with open("example.txt","a") as f:
  pass
except FileNotFoundError as e:
 print("File not found!")
except FileExistsError as e:
 print("File already exist!")
except Exception as e:
 print("Error occured!")

