#Project made by Atakan Özden#
import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_lenght = int(input("Please enter your password lenght:"))
password = ""
for i in range(password_lenght):

    selected = random.choice(characters)
    password += selected


print("Your password is ready!", password)


