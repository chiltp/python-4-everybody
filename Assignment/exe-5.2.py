'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
'''

#This line initializes the variable largest/smallest to None. 
#This variable will be used to keep track of the largest/smallest number entered by the user.
largest = None
smallest = None

#This line starts an infinite loop. 
#The code inside this loop will continue to execute until the loop is explicitly broken.
while True:
    num = input("Enter a number: ")
    #This line checks if the user entered "done" as the input. 
    #If the condition is true, meaning the user wants to stop entering numbers, the break statement is encountered, which breaks the loop and moves to the next lines of code outside the loop.
    if num == "done":
        break
    #This line tries to convert the user's input from a string to an integer using the int() function. 
    #The converted integer is then stored in the variable number. 
    #If the input cannot be converted to an integer (raises a ValueError), the code will jump to the except block.
    try:
        number = int(num)

        #This line checks if the largest variable is None (i.e., no largest number has been found yet) or if the number is greater than the current largest value. 
        #If either condition is true, the largest variable is updated with the new number.
        if largest is None or number > largest:
            largest = number
        #This line checks if the smallest variable is None (i.e., no smallest number has been found yet) or if the number is smaller than the current smallest value. 
        #If either condition is true, the smallest variable is updated with the new number.
        if smallest is None or number < smallest:
            smallest = number
    #If the input cannot be converted to an integer (raises a ValueError), it means the input is not a valid number. 
    #In that case, this block of code is executed, which prints "Invalid input" and then continues to the next iteration of the loop.
    except ValueError:
        print('Invalid input')
        
#After the loop is broken, these lines of code print the largest and smallest numbers entered by the user using the values stored in the largest and smallest variables.    
print("Maximum is", largest)
print("Minimum is", smallest)