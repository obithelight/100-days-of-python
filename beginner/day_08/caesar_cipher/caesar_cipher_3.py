'''
TODO-3:
Can you figure out a way to restart the cipher program?

e.g.

Type 'yes' if you want to go again. Otherwise, type 'no'.

If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.
'''

alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
# print(alphabets)

should_continue = True

while should_continue:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
        if direction in ('encode', 'decode'):
            break
        print("Invalid. Please enter 'encode' or 'decode'")

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

    go_again = input("Do you want to play again? Type 'yes' to continue or any key to quit\n").lower()

    if go_again != "yes":
        print("Goodbye")
        should_continue = False
