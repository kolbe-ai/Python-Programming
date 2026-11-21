#33. (Sentence Word Counter) Read a sentence, convert it into a list of words, count the total words, and print the unique words.

sent = input("Enter the sentence: ")
words = sent.split()
print("Length is: ",len(words))
unique_words = set(words)
print("Unique words is: ",unique_words)