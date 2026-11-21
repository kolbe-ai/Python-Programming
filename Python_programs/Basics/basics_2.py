"""
Take a word and print its length, its first and last character, and whether it contains a vowel from "aeiou"
"""
word = input("Enter a word: ")
print("Length: ", len(word))
print("First letter: ", word[0])
print("Last letter: ", word[-1])
flag = False
for i in word.lower():
    if i in 'aeiou':
        flag = True
print("Contains vowels: ", flag)
