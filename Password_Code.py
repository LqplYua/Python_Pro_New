import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

panjang_karakter = int(input('Masukan Panjang Password :'))

password = ""

for i in range(panjang_karakter): 
    karakter_acak = random.choice(karakter)
    password += karakter_acak

print(password)
