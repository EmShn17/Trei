import random
ifadeler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk=int(input("Şifrenizin uzunluğunu giriniz."))
şifre=""
for i in range(uzunluk):
    şifre += random.choice(ifadeler)

print(şifre)