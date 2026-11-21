"""
(Generator + File Handling) [PDF Q63] Write a generator that reads a file lazily and yields only the non-empty lines.
"""

def generator():
  with open("example.txt","r") as f:
    for i in f:
      line = i.strip()
      if (line):
          print("Reached")
          yield line

with open("example.txt","w") as f:
  f.write("Hello hwo are you?\n")
  f.write("Good to see you\n")
  f.write("Hello from earth\n")

line = generator()
for i in line:
    print(i)