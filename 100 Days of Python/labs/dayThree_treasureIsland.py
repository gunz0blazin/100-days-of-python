###PIRATE TREASURE ISLAND###


#intro
print (" WELCOME TO TREASURE ISLAND!")
print ('''
         __________          
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       ''')


#part one
path_one = input ("A path has split in two, what direction do you go? l or r?:\n")

if path_one == "r":
    print ("Quick Sand! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()
if path_one == "l":
    print ("You venture on!")
else:
    print ("You are struck by lightning! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()


#part two

path_two = input ("You come across a river, what do you do? wait or swim?:\n")

if path_two == "swim":
    print ("You cant swim! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()
if path_two == "wait":
    print ("A boat comes along and gives you a ride!")
else:
    print ("You are struck by lightning! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()


#path three

path_three = input ("Three doors are on the other side, what do you open? left, middle, or right:\n")

if path_three == "left":
    print ("You explode when it opens! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()

elif path_three == "right":
    print ("Angry dogs! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()
elif path_three == "middle":
    print ("You found the treasure!")

else:
    print ("You are struck by lightning! YOU DIED")
    print ('''          
         .\  _---_  /.
         . \/     \/.
            |() ()|
             \ + /
           ./ HHH  \.
          ./  \_/   \.
                  ''')
    exit()