######fuctions' area#####
#Body Mass Index is a simple calculation using a person's height and weight
def BMI(height: int, weight: int):
    h_meter = round(height/100, 2)
    BMI = round(weight/(h_meter**2), 2)
    return BMI
def Normal_weight(height: int):
    h_meter = round(height/100, 2)
    least_w = round(18.5*(h_meter**2), 0)
    max_w = round(24.9*(h_meter**2), 0)
    return least_w, max_w
######fuctions' area######

######Code area######
print('To calculate your BMI please answer following questions:\n')
h = int(input("What is your height?\n"))
w = int(input("What is your weight?\n"))
bmi = BMI(h, w)
print("your BMI is ",bmi)
if bmi < 18.50:
    print('You are Underweight')
    print('Normal range for you weight based on your height is {}'.format(Normal_weight(h)))
elif bmi<=24.90 and bmi>=18.50:
    print('You have Healthy Weight')
elif bmi>25.00 and bmi<=29.9:
    print('You are Overweight')
    print('Normal range for you weight based on your height is {}'.format(Normal_weight(h)))
else:
    print('You are Obese')
    print('Normal range for you weight based on your height is {}'.format(Normal_weight(h)))
######Code area######
