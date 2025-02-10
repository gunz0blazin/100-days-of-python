#day7notes
#TASK 1 randomly choose a word from the word_list and assign it a variable called chosen_word, then print it
#TASK 2 ask the user to guess a letter, make the answer a variable called guess. Make it lower case
#TASK 3 check if guess is in chosen word, print RIGHT if it is and WRONG if its not
#TASK 4 create a "placeholder" with the same number of "_" as characters in the chosen word
#TASK 5 create a "display" that puts the guess letters in right position in the "placeholder"
#TASK 6 use a while loop to let the use guess gain
#TASK 7 change the for loop to keep the previous correct along with the new one
#TASK 8 create a variable called lives to keep track how many lives the user has left set to 6
#TASK 9 when user makes a wrong guess, reduce number of lives by one, if lives hit zero print you loose
#TASK 10 print ASCII art to show number of lives user has left

import random

#all the stages of hang man in a list to index later
stages = ['''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        |
        |
=============
''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        |
        |
=============                             
''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        |
        |
=============
''','''
    +---+
    |   |
    0   |
   /|   |
    |   |
        |
        |
        |
=============
''','''
    +---+
    |   |
    0   |
    |   |
    |   |
        |
        |
        |
=============
''','''
    +---+
    |   |
    0   |
        |
        |       
        |
        |
=============
''','''
    +---+
    |   |
        |
        |
        |
        |
        |
        |
=============
''',]
#word list to pick from
word_list = ["aardvark", "baboon", "camel"]

#pick a word from the list
chosen_word = random.choice(word_list)

#generate blank display based on chosen word length
guess_count = len(chosen_word)
placeholder = "_" * guess_count
display = ""

#make display and chosen word a list we can index to check against
chosen_word_list = list(chosen_word)
display_list = list(placeholder)

#set lives to 6
lives = 6 
print ("WELCOME TO HANGMAN")
print (placeholder)

#check if guess is in chosen word list if not remove a life
while lives > 0:
    guess = input("Guess a letter!\n").lower()
    if guess not in chosen_word_list:
        lives -= 1
#check if guess is in chosen word & update display list per list index    
    for x in range(len(chosen_word_list)):
        if guess == chosen_word[x]:
            display_list[x] = guess

#display screen based on lives with game over at 0                         
    display ="".join(display_list)
    if display == chosen_word:
        print (chosen_word)
        print ("YOU WIN!")
        exit()
    elif lives == 6:
        print (stages[-1])
    elif lives == 5:
        print (stages[-2])
    elif lives == 4:
        print (stages[-3])
    elif lives == 3:
        print (stages[-4])
    elif lives == 2:
        print (stages[-5])
    elif lives == 1:
        print (stages[-6])
    elif display == chosen_word:
        print ("YOU WIN!")
    else:
        print(stages[-7])
        print("GAME OVER")
    print (display)
    print (f"you have {lives} lives left")
    
    
    
    







    

