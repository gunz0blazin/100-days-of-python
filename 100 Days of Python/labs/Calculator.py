def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div, 
}

def calculate():
    n1= float(input("First Number?\n"))
    user_opp = input ("select +,-,*,/\n")
    n2= float(input("Second Number?\n"))
    return (operations[user_opp](n1,n2))

def calculate_again():
    user_opp = input ("select +,-,*,/\n")
    n2_2= float(input("Second Number?\n"))
    return (operations[user_opp](n1_2,n2_2))

output = calculate()
print (output)



    

    


