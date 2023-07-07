'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
'''

#This line defines a function named computepay that takes two parameters: h for hours worked and r for the hourly rate.
def computepay(h, r):
    #This line checks if the number of hours worked (h) is less than or equal to 40. If so, it calculates the pay by multiplying the hours (h) by the hourly rate (r).
    if h <= 40:
        p = h*r
    #If the number of hours worked is greater than 40, this line calculates the pay by considering overtime. It calculates the overtime hours by subtracting 40 from the total hours worked (h - 40), multiplies it by the overtime rate (1.5 times the hourly rate r), and adds it to the regular pay for 40 hours (40 * r).    
    else:
        p = (h-40)*(r*1.5) + 40*r
    #This line returns the calculated pay (p) as the output of the function.   
    return p

#These lines prompt the user to enter the number of hours and the hourly rate. The input() function takes user input as a string, and the float() function converts the input to a floating-point number.
h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))

#This line invokes the computepay function, passing the entered hours (h) and rate (r) as arguments. The return value of the function is assigned to the variable p.
p = computepay(h, r)
#This line displays the calculated pay (p) to the user, along with the label "Pay:".
print("Pay", p)