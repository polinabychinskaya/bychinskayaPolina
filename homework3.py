print("Sup! Enter three numbers you like!")


#Exercise 1
num_1_task_1 = int(input("Enter the first num: "))
num_2_task_1 = int(input("Enter the second num: "))
num_3_task_1 = int(input("Enter the third num: "))
result_task_1 = num_1_task_1 and num_2_task_1 and num_3_task_1 and "No zero values!"
print(result_task_1)
print("--------------------------------------------------------")


#Exercise 2
num_1_task_2 = int(input("Enter the first num: "))
num_2_task_2 = int(input("Enter the second num: "))
num_3_task_2 = int(input("Enter the third num: "))
result_task_2 = num_1_task_2 or num_2_task_2 or num_3_task_2 or "All input numbers contain zeros!"
print(result_task_2)
print("--------------------------------------------------------")


#Exercise 3
num_1_task_3 = int(input("Enter the first num: "))
num_2_task_3 = int(input("Enter the second num: "))
num_3_task_3 = int(input("Enter the third num: "))
sum = num_2_task_3 + num_3_task_3
if num_1_task_3 > sum:
    result_task_3 = num_1_task_3 - sum
    print(result_task_3)
print("--------------------------------------------------------")


#Exercise 4
num_1_task_4 = int(input("Enter the first num: "))
num_2_task_4 = int(input("Enter the second num: "))
num_3_task_4 = int(input("Enter the third num: "))
sum = num_2_task_4 + num_3_task_4
if num_1_task_4 < sum:
    result_task_4 = sum - num_1_task_4
    print(result_task_4)
print("--------------------------------------------------------")


#Exercise 5
num_1_task_5 = int(input("Enter the first num: "))
num_2_task_5 = int(input("Enter the second num: "))
num_3_task_5 = int(input("Enter the third num: "))
if num_1_task_5 > 50 and (num_2_task_5 > num_1_task_5 or num_3_task_5 > num_1_task_5):
    print("Vasya")
print("--------------------------------------------------------")


#Exercise 6
num_1_task_6 = int(input("Enter the first num: "))
num_2_task_6 = int(input("Enter the second num: "))
num_3_task_6 = int(input("Enter the third num: "))
if num_1_task_6 > 5 or (num_2_task_6 == 7 and num_3_task_6 == 7):
    print("Petya")
print("--------------------------------------------------------")


#AUGMENTED BMI


#Calculating a standard BMI
print("Hello! Let's calculate your BMI!")
height = float(input("Enter your height (cm): "))/100
weight = float(input("Enter your weight (kg): "))
sex = input("Enter your sex (male/female): ")
age = int(input("Enter your age: "))
bmi = weight/(pow(height, 2))
print("Your Body Mass Index is " + str(bmi))


#Adding parameters for "male" results
if bmi < 19 and sex == "male":
    print("Too thin for your age!")
elif 19 <= bmi <= 27 and sex == "male":
    print("Standard for your age!")
elif bmi > 27 and sex == "male":
    print("Too obese for your age!")


#Adding parameters for "female" results
if bmi < 17 and sex == "female":
    print("Too thin for your age!")
elif 17 <= bmi <= 25 and sex == "female":
    print("Standard for your age!")
elif bmi > 25 and sex == "female":
    print("Too obese for your age!")


#Adding recommendations for males + their age (underweight)
if bmi < 19 and sex == "male" and 0 <= age <= 30:
    print("Go and have a medical checkup. Make up a special diet with high-calorie foods. Introduce some exercises.")
elif bmi < 19 and sex == "male" and 30 <= age <= 60:
    print("Go and have a medical checkup. Make up a special diet with high-calorie foods. Give up bad habits.")
elif bmi < 19 and sex == "male" and age > 60:
    print("Pay attention to your health! Try to lead an active lifestyle and obtain a comprehensive diet.")


#Adding recommendations for females + their age (underweight)
if bmi < 17 and sex == "female" and 0 <= age <= 30:
    print("Go and have a medical checkup. Make up a special diet with high-calorie foods. Do some stetching.")
elif bmi < 17 and sex == "female" and 30 <= age <= 60:
    print("Go and have a medical checkup. Make up a special diet with high-calorie foods. Give up bad habits.")
elif bmi < 17 and sex == "female" and age > 60:
    print("Pay attention to your health! Try to lead an active lifestyle and obtain a comprehensive diet.")


#Adding recommendations for males + their age (standard)
if 19 <= bmi <= 27 and sex == "male" and 0 <= age <= 30:
    print("Keep up your perfect welfare!")
elif 19 <= bmi <= 27 and sex == "male" and 30 <= age <= 60:
    print("Keep up your perfect welfare!")
elif 19 <= bmi <= 27 and sex == "male" and age > 60:
    print("Keep up your perfect welfare!")


#Adding recommendations for females + their age (standard)
if 17 <= bmi <= 25 and sex == "female" and 0 <= age <= 30:
    print("Keep up your perfect welfare!")
elif 17 <= bmi <= 25 and sex == "female" and 30 <= age <= 60:
    print("Keep up your perfect welfare!")
elif 17 <= bmi <= 25 and sex == "female" and age > 60:
    print("Keep up your perfect welfare!")


#Adding recommendations for males + their age (obese)
if bmi > 27 and sex == "male" and 0 <= age <= 30:
    print("Sign up for a gym membership (muscle exercises). Go and have a medical check up. Reduce the amount of calories you consume.")
elif bmi > 27 and sex == "male" and 30 <= age <= 60:
    print("Go and have a medical checkup. Make up a special diet with low-calorie foods. Give up bad habits.")
elif bmi > 27 and sex == "male" and age > 60:
    print("Pay attention to your health! Try to lead an active lifestyle and obtain a comprehensive diet.")


#Adding recommendations for females + their age (obese)
if bmi > 25 and sex == "female" and 0 <= age <= 30:
    print("Sign up for a gym membership (stretching). Go and have a medical check up. Reduce the amount of calories you consume.")
elif bmi > 25 and sex == "female" and 30 <= age <= 60:
    print("Go and have a medical checkup. Make up a special diet with low-calorie foods. Give up bad habits and junk food.")
elif bmi > 25 and sex == "female" and age > 60:
    print("Pay attention to your health! Try to lead an active lifestyle and obtain a comprehensive diet.")


#Adding a horizontal indicator
dash_num_left = abs(16 - round(bmi))
dash_num_right = 40 - round(bmi)
print("16" + "="*dash_num_left + "|" + "="*dash_num_right + "40")





print("Hello! Let's calculate your BMI!")
height = float(input("Enter your height (cm): "))/100
weight = float(input("Enter your weight (kg): "))
bmi = weight/(pow(height, 2))
print("Your Body Mass Index is " + str(bmi))
dash_num_left = abs(16 - round(bmi))
dash_num_right = 40 - round(bmi)
print("16" + "="*dash_num_left + "|" + "="*dash_num_right + "40")