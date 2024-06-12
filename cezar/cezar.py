import art
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cezar(direction,text,shift):
    encrypt_text = "" 
    for i in text:
        if i  in alphabet:
            index = alphabet.index(i)
            if direction == "encode":
                letter = index+shift
                if letter > 26:
                        letter -= 26
                encrypt_text += alphabet[letter]
            elif direction == "decode":
                letter = index-shift
                if letter < 0:
                    letter += 26
                encrypt_text += alphabet[letter]
            elif i not in alphabet:
                encrypt_text += i
    print(encrypt_text)

stop = False

print(logo)
while(stop == False):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cezar(direction,text,shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no' ")
    if again == "no":
        stop = True
        print("Goodbye")
