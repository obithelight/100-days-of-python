'''
TODO-1:
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

TODO-3:
Combine the encrypt() and decrypt() functions into a single function called caesar().
Use the value of the user chosen direction variable to determine which functionality to use.
call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.
'''
alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
# print(alphabets)

while True:
    text = input("Type your message:\n").strip()

    if text:
        break
    print("Invalid. Please enter a word or message.")

while True:
    try:
        shift = int(input("Type the shift number:\n"))
        
        if shift > 0:
            break
        print("Invalid Input. Enter a positive integer.")
    
    except ValueError:
        print("Invalid Input. Enter a valid integer.")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    if direction in ('encode', 'decode'):
        break
    print("Invalid. Please enter 'encode' or 'decode'")

def cipher(original_text: str, shift_amount: int, encode_or_decode: str) -> None:
    output_text = ''

    for letter in original_text:
        if letter in alphabets:
            
            if encode_or_decode == 'encode':
                shift_position = alphabets.index(letter) + shift_amount
            else:
                shift_position = alphabets.index(letter) - shift_amount

            shift_position %= len(alphabets)
            output_text += alphabets[shift_position]

        else:
            output_text += letter

    print(f"Your {encode_or_decode}d text is: {output_text}")

cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)
