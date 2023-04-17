## **Password Generator**

Write a Python program to generate a strong and secure password. The program should allow the user to specify the length of the password and the types of characters that should be included, such as uppercase and lowercase letters, digits, and symbols. The program should then generate a random password that meets the specified criteria.


**Input:**
```python
length = 10
include_uppercase = True
include_lowercase = True
include_digits = True
include_symbols = True
generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
```


**Output:**
```
sT#1mF7xKz
```


**Constraints:**
- The length of the password will be an integer between 6 and 32.
- The input for including each type of character will be a boolean value.
- Your program should generate a random password that meets the specified criteria.
- The password should contain at least one character from each type of character specified by the user.
- Your program should return the generated password as a string.

**Concepts Practised:**
- Random number generation: using Python's built-in random number generator to generate random numbers for selecting characters.
- Lists: creating and manipulating lists to store characters that will be used in password generation.
- String manipulation: creating and manipulating strings using Python's string methods.
- Loops: using loops to iterate over strings, lists, or other data structures.
- Conditional statements: using if/else statements to check conditions and perform different actions based on those conditions.
- Functions: writing functions to encapsulate blocks of code that can be reused in the program.

**Resources:**

- [Python Random Module](https://www.w3schools.com/python/module_random.asp)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [Python Loops](https://www.w3schools.com/python/python_for_loops.asp)

