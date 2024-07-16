import random
import string

text=["BALL","JESUS", "TRUMP", "BOOB"]
def get_word(set_lenght):
    filtered_words=[_ for _ in text if len(_)==set_lenght]
    return random.choice(filtered_words)
def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
def encrypt_1(text, key): #i have no idea how this works but it just does
    ciphertext = ''
    for p, k in zip(text, key):
        encrypted_char = chr(((ord(p) - 65 + ord(k) - 65) % 26) + 65)
        ciphertext += encrypted_char
    return ciphertext
def encrypt_2(text, key):
    #just write that shift encryption code here, 
    print("asdas")
def decrypt_1(cipher, key):
    plaintext = ''
    for c, k in zip(cipher, key):
        decrypted_char = chr(((ord(c) - 65 - (ord(k) - 65)) % 26) + 65)
        plaintext += decrypted_char
    return plaintext
def decyrpt_2(cipher, key):
    #just write decrytion of that shift encryption
    print("asd")
