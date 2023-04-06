letter = "the quick brown fox jumps over the lazy dog"

word_count = {}

words = letter.split()   #this function splits the string so you can ocunt the words

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(word, count)