alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs

def encrypt(text,shift):
    encode_text = ""
    for letter in text:
        if not letter in alphabet:
            encode_text += letter
        else:
            index = alphabet.index(letter) + shift
            if index > 25:
                index = index - 26
            encode_text += alphabet[index]
    print(f"The encoded text is {encode_text}")

#Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.

def decrypt(text,shift):
    decode_text = ""
    for letter in text:
        if not letter in alphabet:
            decode_text += letter
        else:
            index = alphabet.index(letter) - shift
            if index < 0:
                index = index + 26
            decode_text += alphabet[index]
    print(f"The decoded text is {decode_text}")
    
#Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(start_text,shift_amount,direction_program):
    final_text = ""
    if direction_program == "encode":
        for letter in start_text:
            if not letter in alphabet:
                final_text += letter
        else:
            index = alphabet.index(letter) + shift_amount
            if index > 25:
                index = index - 26
            final_text += alphabet[index]
        print(f"The encoded text is {final_text}")
    else:
        for letter in start_text:
            if not letter in alphabet:
                final_text += letter
        else:
            index = alphabet.index(letter) - shift_amount
            if index < 0:
                index = index + 26
            final_text += alphabet[index]
        print(f"The decoded text is {final_text}")



programa = True
while programa:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction in ['encode','decode']:
        programa = False
        print('Ingrese una direccion valida')

if(direction=="encode"):
    encrypt(text=text,shift=shift)
else:
    decrypt(text=text,shift=shift)

