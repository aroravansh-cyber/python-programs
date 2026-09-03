text = input("Enter a sentence: ")

words = text.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
