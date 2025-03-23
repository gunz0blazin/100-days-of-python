import art

go_again = "yes"

while go_again == "yes":
    print (art.logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    original_text = text
    
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        
        if encode_or_decode == "decode":
            shift_amount = shift_amount * -1
    
        for letter in original_text: 
                if letter not in alphabet:
                     output_text += letter
                else:
                    shift_value = alphabet.index(letter) + shift_amount
                    shift_value %= len(alphabet)
                    output_text += alphabet[shift_value]
        
        print (f"Your {encode_or_decode}d text is: {output_text}")
         
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    go_again = input ("Do you want to go again? Yes or No?\n").lower()
    


