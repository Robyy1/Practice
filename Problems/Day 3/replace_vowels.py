# letter = " Hello! I like programing in python!"
# for character in letter:
# vowels= "a", "e" , "i", "o", "u", "y"

# variant 1, Brutal😥
letter = "Cats are curious creatures with a graceful presence."
letter_1 = (letter.replace("a", "x"))
letter_2 = (letter_1.replace("e", "x"))
letter_3 = (letter_2.replace("i", "x"))
letter_4 = (letter_3.replace("o", "x"))
letter_5 = (letter_4.replace("u", "x"))
letter_6 = (letter_5.replace("y", "x"))
letter_7 = (letter_6.replace("w", "x"))
print(letter_7)

# variant 2, Eficcient😎


def replace_vowels(string):
    vowels = ["a", "e", "i", "o", "u", "y", "w"]
    letter = ""
    for char in string:
        if char.lower() in vowels:
            letter += "x"
        else:
            letter += char
    return letter


message = "Cats are curious creatures with a graceful presence."
print(replace_vowels(message))
