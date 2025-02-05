#Even or Odd check
"""
num_to_check = int(input("what number are you checking? \n"))

if num_to_check % 2 == 0:
    print ("Even")
    exit()
else: 
    print ("Odd")
"""

#rollercoaster check

print ("Welcome to the rollercoaster!")

bill = 0
height = int(input("What is your hight in cm? \n"))

if height >= 120:
    print ("You can ride!")
    age = int(input("How old are you? \n"))
    if age < 12:
        print ("Kids are $5")
        bill = 5
    elif age > 18:
        print ("Adults are $12")
        bill = 12
    else:
        print("Teens are $7")
        bill = 7
    wants_photo = input("do you want a photo? \n")

    if wants_photo == "y":
        bill += 3

    print (f"Your bill is ${bill}")
    
    
else:
    print ("You're too short!")
#BMI calculator

'''
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇


if bmi < 18.8:
    print("Underweight")
    
elif bmi >= 25:
    print ("Overweight")
    
else:
    print ("Normal")
'''