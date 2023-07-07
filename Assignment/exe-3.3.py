'''
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''

score = float(input("Enter Score: "))
if score < 0.0 or score > 1.0:
    print("Value is out of range!")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")

#Using elif allows the code to evaluate multiple conditions in order, and only execute the block of code associated with the first condition that is true. 
#It provides a way to handle different cases based on the value of score and choose the appropriate grade to display.