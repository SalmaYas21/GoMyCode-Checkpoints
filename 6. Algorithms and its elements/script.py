sentence = input("Enter a sentence: ")
length = 0
words = 1
vowels = 0

for char in sentence:
    length += 1
    if char == ' ':
        words += 1
    elif char in 'aeiouAEIOU':
        vowels += 1
    elif char == '.':
        break

print("Length of sentence:", length)
print("Number of words:", words)
print("Number of vowels:", vowels)