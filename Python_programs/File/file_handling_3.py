"""
Append 3 lines to a file, then read it back and print the number of lines and words.
"""

with open("example.txt","a") as f:
    f.write("Hello 1\n")
    f.write("Hello 2\n")
    f.write("Hello 3\n")

lines = []
with open("example.txt","r") as f:
    lines = f.readlines()

count = 0
word = 0
for i in lines:
    count = len(lines)
    word += len(i.split())
print("Number of lines: ",count)
print("Number of words: ",word)