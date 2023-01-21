#Password Generator Project
# Instruction
# The program will ask:
# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1,nr_letters +1):
    password_list.append(random.choice(letters))

for char in range(1,nr_numbers +1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbols +1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password1 = ""
for char in password_list:
    password1 += char

print(f"You final password is: {password1}")
#or
#random1 = [random.choice(letters) for i in range(nr_letters)]
#random2 = [random.choice(numbers) for i in range(nr_numbers)]
#random3 = [random.choice(symbols) for i in range(nr_symbols)]

#random4 = random1+random2+random3

#print(random4)