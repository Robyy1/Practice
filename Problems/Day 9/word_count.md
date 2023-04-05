# Problem: Word Count

Write a Python function called word_count that takes a string as input and returns a dictionary that contains the count of each word in the string.

### **Example Input/Output:**

**Input:**
```
string = "the quick brown fox jumps over the lazy dog"
word_count(string)
```

**Output:**
```
{
    'the': 2,
    'quick': 1,
    'brown': 1,
    'fox': 1,
    'jumps': 1,
    'over': 1,
    'lazy': 1,
    'dog': 1
}
```

**Constraints:**
- The input string will only contain alphabetic characters and spaces.
- Your function should return a dictionary where each key is a unique word in the input string and the corresponding value is the count of that word in the string. The keys should be sorted in alphabetical order.
- The words in the input string should be treated as case-insensitive, i.e., "the" and "The" should be treated as the same word