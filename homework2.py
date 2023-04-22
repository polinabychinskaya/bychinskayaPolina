print("Hello! Let's calculate your BMI!")
height = float(input("Enter your height (cm): "))/100
weight = float(input("Enter your weight (kg): "))
bmi = weight/(pow(height, 2))
print("Your Body Mass Index is " + str(bmi))
dash_num_left = abs(16 - round(bmi))
dash_num_right = 40 - round(bmi)
print("16" + "="*dash_num_left + "|" + "="*dash_num_right + "40")