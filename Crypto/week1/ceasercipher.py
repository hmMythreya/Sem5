#ceasar cipher code
from tokenize import PlainToken


plaintext = input("(PES2UG20CS130) Enter the text you want cipher: ")
plaintext = plaintext.lower()
key = int(input("(PES2UG20CS130) Enter key:"))

cipher=""
for i in plaintext:
    cipher += (chr(((ord(i)-ord("a")+key))%26+ord("a")))

print("(PES2UG20CS130) Ciphertext=", cipher.upper())