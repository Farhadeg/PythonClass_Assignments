######fuctions' area#####
#Body Mass Index is a simple calculation using a person's height and weight
def BMI(height: int, weight: int):
    h_meter = round(height/100, 2)
    BMI = round(weight/(h_meter**2), 2)
    return BMI
######fuctions' area######

######Code area######
print('To calculate your BMI please answer following questions:\n')
bmi = BMI(int(input("What is your height?\n")),int(input("What is your weight?\n")))
print("your BMI is ",bmi, 'and')
if bmi < 18.50:
    print('You are Underweight')
elif bmi<=24.90 and bmi>=18.50:
    print('You have Healthy Weight')
elif bmi>25.00:
    print('You are Overweight')
else:
    print('You are Obese')
######Code area######
