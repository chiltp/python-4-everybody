import re

fname = input("Enter file:")
if len(fname) < 1:
    fname = "regex_sum_1856255.txt"
handle = open(fname)
numlist = list()

for line in handle:
    # Use 're.findall()' to find all occurrences of one or more digits (0-9) in the current 'line'.
    # The 're.findall()' method returns a list of all matches found in the 'line'.
    numbers = re.findall('[0-9]+', line)
    
    # Check if the length of 'numbers' list is 0 (i.e., no digits were found in the line).
    if len(numbers) == 0 : 
        # If no digits were found, 'continue' with the next iteration of the 'for' loop
        # without executing the following code block.
        continue
    # If digits were found in the line, convert each element in the 'numbers' list from strings to integers
    # using the 'map()' function and 'int' as the mapping function. Create a list called 'num' containing these integers.
    num = list(map(int, numbers))
    for value in num:
        # Append each value to the 'numlist', which will store all the numbers found in the entire file.
        numlist.append(value)
# After processing all lines in the file, print the sum of all numbers stored in 'numlist'.
print(sum(numlist))