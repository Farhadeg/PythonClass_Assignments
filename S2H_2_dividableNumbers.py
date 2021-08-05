#A simple Code to check if first number is dividable by second number
Number1 = int(input("Please enter your first Number:\n"))
Number2 = int(input("Please enter your second Number:\n"))

if (Number1%Number2 == 0):
    print("Your first number is dividable by the second number\n\
And the quotient is",int(Number1/Number2))
else:
    print("Your first number is not dividable by the second number\n\
And the remainder is",Number1%Number2)
