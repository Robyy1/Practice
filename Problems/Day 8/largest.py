# Problem: Find the Second Largest Number

# Write a Python function `second_largest_number(lst)` that takes in a list of integers and returns the second largest number in the list.

# # Example Input/Output:
# ```
# Input:
# [5, 9, 3, 7, 6]
# Output:
# 7
# ```

list = [5, 9, 3, 7, 6]
largest_number = list[0]
second_largest_number = None

for number in list[1:]:
    if number > largest_number:
        second_largest_number = largest_number
        largest_number = number
    elif second_largest_number == None or number > second_largest_number:
        second_largest_number = number
        

print(second_largest_number)
   
