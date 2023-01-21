# Don't change the code below
height = input ("Enter your height in m: ")
weight = input ("Enter your weight in kg: ")
# Don't change the code above

#Write your code below this line

height1 = float(height)
weight1 = float(weight)

BMI = (weight1/(height1*height1))
bmi_as_int = int(BMI)
print(bmi_as_int)