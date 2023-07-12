'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
#This line opens the file specified by the fname variable using the open() function and assigns the file object to the variable fh. 
#The file is opened in default read mode.
fh = open(fname)
#These lines initialize two variables: count to keep track of the number of relevant lines, and total to calculate the sum of the confidence values.
count = 0
total = 0.0

#This line starts a loop that iterates over each line in the file specified by fh.
for line in fh:
    #This if statement checks if the current line does not start with the string "X-DSPAM-Confidence:". 
    #If it doesn't, the continue statement skips the remaining code within the loop and proceeds to the next iteration.
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    '''
    These lines are executed for lines starting with "X-DSPAM-Confidence:".
        count is incremented by 1 to keep track of the relevant lines encountered.
        zero_position is assigned the index of the first occurrence of '0' in the line.
        confidence is extracted from the line starting from zero_position to the end and converted to a floating-point number.
        total is updated by adding the extracted confidence value.
    '''
    count = count + 1
    zero_postion = line.find('0')
    confidence = float(line[zero_postion:])
    total = total + confidence

average = total / count
print("Average spam confidence:", average)
