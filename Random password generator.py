import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&"
length = int(input("Enter the length of password: "))
password = ""

for i in range(length):
    random.choice(chars)
    password += random.choice(chars)
print(password)
