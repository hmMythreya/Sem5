#ceasar cipher code
from tokenize import PlainToken


plaintext = input("(PES2UG20CS130) Enter the text you want decipher: ")
plaintext = plaintext.lower()
key = int(input("(PES2UG20CS130) Enter key:"))

decipher=""
for i in plaintext:
    decipher += (chr(((ord(i)-ord("a")-key))%26+ord("a")))

print("(PES2UG20CS130) Plaintext=", decipher.upper())