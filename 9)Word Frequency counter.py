import string

text = input("Enter a text or paragraph: ").lower()
for p in string.punctuation:
    text = text.replace(p, "")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequencies:", word_count)