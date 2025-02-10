#FizzBuzz
import time

for number in range (1, 1000 * 1000):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz ")
        time.sleep(.1)
    elif number % 5 == 0:
        print ("Buzz ")
        time.sleep(.1)
    elif number % 3 == 0: 
        print ("Fizz")
        time.sleep(.1)
    else:
        print (number)
        time.sleep(.1)
    
    