alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
original_text = text



'''
def encrypt(original_text,user_shift):
    encrypted_text= ""
    for letter in original_text:
        shift_value = alphabet.index(letter) + user_shift
        shift_value %= len(alphabet)
        encrypted_text += alphabet[shift_value]
    print (f"Your encoded text is: {encrypted_text}")
'''
'''
def decrypt(original_text,user_shift):
    decrypted_text = ""
    for letter in original_text:
        shift_value = alphabet.index(letter) + (user_shift * -1)
        shift_value %= len(alphabet) * -1
        decrypted_text += alphabet[shift_value]
    print (f"Your decoded text is: {decrypted_text}")
'''

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
   
    for letter in original_text:
        shift_amount = shift
        if encode_or_decode == "decode":
            shift_amount = shift_amount * -1
        
        shift_value = alphabet.index(letter) + shift_amount
        shift_value %= len(alphabet)
        output_text += alphabet[shift_value]
    print (f"Your {encode_or_decode}d text is: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    


