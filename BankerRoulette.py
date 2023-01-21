import random

name_string = input("Give me everybody's name, seperated it by a comma. \n")
names = name_string.split(",")

tigihap = len(names)
random_choice = random.randint(0,tigihap - 1)

personwhowill_pay = names[random_choice]

print(f"{personwhowill_pay} is going to buy the meal")


#or use this instead

#person_who_will_pay = random.choice(names)
#print(person_who_will_pay + " is going to buy the meal today!")