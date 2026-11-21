"""
Sentence Word Counter
Accept a sentence from the user and:
● Convert it into a list of words.
● Count total number of words.
● Print unique words in the sentence.
Concepts: .split(), list length, set conversion
"""

sent = input("Enter a sentence: ")
words = sent.split()
count = len(words)
unique = set(words)
print(f"The number of words: {count}")
print(f"The unique words: {unique}")