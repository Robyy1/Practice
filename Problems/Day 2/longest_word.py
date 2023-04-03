def longest_word(words):
    longest = "" 
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


word_list = ["apple", "blueberry", "blackberry", "orange", "banana", "almonds"]
print(longest_word(word_list))
