import random

letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("ingrese la longuitud: "))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(letras)

print(contraseña)