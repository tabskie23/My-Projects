print("Welcome to the Love Calculator")

name1 = input("Enter your name \n")
name2 = input("Enter their name \n")

combined_name = str(name1.upper()) +" "+ str(name2.upper())

t = combined_name.count("T")
r = combined_name.count("R")
u = combined_name.count("U")
e = combined_name.count("E")
l = combined_name.count("L")
o = combined_name.count("O")
v = combined_name.count("V")
e = combined_name.count("E")

true = t+r+u+e
love = l+o+v+e

truelove = int(str(true) + str(love))

if truelove <= 10 or truelove >= 90:
    print(f"Your love score is: {truelove}, you go together like coke and mentos.")

elif truelove >= 40 and truelove <= 50:
    print(f"Your love score is: {truelove}, you are alright together.")
else:
    print(f"Your score is: {truelove}.")