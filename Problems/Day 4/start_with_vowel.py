# Write a Python program that takes in a list of words and prints the number of words in the list that start with a vowel.
def count_vowel_words(word_list):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for word in word_list:
        if word[0].lower() in vowels:
            count += 1
    print(f"The number of words that start with a vowel is{count}")
        

words_list = ["pineapple", "orange", "mango", "apple", "banana", "pear", "watermellon" "lemon"] 
count_vowel_words(words_list)