alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypt_text = ""
    for i in text:
        index = alphabet.index(i)
        letter = index+shift
        if letter > 26:
            letter -= 26
        encrypt_text += alphabet[letter]
    print(encrypt_text)
   

def decrypt(text, shift):
    encrypt_text = ""
    for i in text:
        index = alphabet.index(i)
        letter = index-shift
        if letter < 0 :
            letter += 26
        encrypt_text += alphabet[letter]
    print(encrypt_text)
 


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)