height=float(input("Enter your height in centimeters: "))
weight=float(input("Enter your weight in kilograms: "))
height=height/100
bmi=weight/(height*height)
print("Your BMI is:",bmi)
if bmi<=18.5:
    print("You are Underweight")
elif (bmi==18.5 and bmi <= 24.9):
    print("Your BMI is normal")
elif (bmi>=25 and bmi <= 29.9):
    print("You are overweight")
else:
    print("Obesity")