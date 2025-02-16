alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
original_text = text

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
#comment test


def encrypt(original_text, shift):
    #define empty lists to add our data to
    text_list = []
    original_index = []
    new_index = []
    new_text_list = [alphabet[y] for y in range]
    #convert original text to a list
    for x in original_text:
        if x==x:
            text_list.append(x)
    #find the index of each letter in our text list
    for index in text_list:
        if index in alphabet:
            original_index.append(alphabet.index(index))
    #shift the index of each letter by the users shift amount 
    for change in original_index:
        new_index.append(change + shift)
    #print statements for debug 
    print(original_index)
    print(new_index)
    print (new_text_list)

#call encrypt function 
encrypt(original_text,shift)


