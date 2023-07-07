'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
'''

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h > 0 and h <= 40:
    total_pay = h * r
else:
    regular_pay = 40 * r
    overtime = h - 40
    overtime_rate = 1.5 * r
    overtime_pay = overtime * overtime_rate
    total_pay = regular_pay + overtime_pay
print(total_pay)