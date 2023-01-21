Age = input("What is your current age? ")

#Write your code below this line

#365 days
#52 weeks
#12 months

age_as_int = int(Age)
years_remaining = 90 - age_as_int

x = years_remaining * 365
y = years_remaining * 52
z = years_remaining * 12

print(f"You have {x} days, {y} weeks, and {z} months left.")
