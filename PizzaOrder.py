#Don't change the code below

print("Welcome to Python Pizza Deliveries! ")

size = str(input("What size pizza do you want? S, M, or L \n"))
add_pepperoni = str(input("Do you want pepperoni? Y or No \n"))
extra_cheese = str(input("Do you want extra chesse? Y or N \n"))
#Don't change the code above

# small = $15
# medium = $20
# large = $25
# pepperoni for small pizza: +$2
# pepperoni for medium or large pizza: +$3
# extra cheese for any size pizza: +$1

bill = 0

if size == 's':
    bill += +15
    print(f"Your Pizza size is Small")
elif size == 'm':
        bill = +20
        print(f"Your pizza size is Medium")
else:
    bill = +25
    print("Your pizza size is Large")   

if add_pepperoni == 'y':
        if size == 's':
            bill += +2
        else:
            bill += +3
else:
    bill += 0

if extra_cheese == "y":
    bill += +1
else:
    bill += 0

print(f"Your final bill is: ${bill}")

