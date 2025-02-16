#def a function with a single condition
'''
def life_in_weeks(age):
    life_left = (90-age)*52
    print(f"You have {life_left} weeks left.\n")

life_in_weeks(int(input("How old are you?\n")))
'''
#def a function with multiple conditions
'''
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name=input("What is your name?\n"), location=input("what is your location?\n"))
'''
#love calculator
'''
def calculate_love_score(name_one,name_two):
    names_combined= name_one+name_two
    names_lower = names_combined.lower()

    t = names_lower.count("t")
    r = names_lower.count("r")
    u = names_lower.count("u")
    e = names_lower.count("e")
    count_one = t+r+u+e

    l = names_lower.count("l")
    o = names_lower.count("o")
    v = names_lower.count("v")
    e = names_lower.count("e")
    count_two = l+o+v+e

    love_score = int(str(count_one)+str(count_two))
    print (love_score)

calculate_love_score(input("First Name?\n"),input("Second?\n"))
'''
nums = [33,44,55,66]
range = [0,1,3]
output = [nums[i]for i in range]
print (output)