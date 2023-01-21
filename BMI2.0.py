#Don't change the code below

from telnetlib import BM


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
#Don't change the code above

BMI = (weight/(height*height))
bmi_as_int = int(BMI)
underweight = ("You are underweight. ")
normalKg = ("You have a normal weight. ")
slghtlyOver = ("You are slightly overweight. ")
obese = ("You are obese. ")
cliObese = ("Clinically obese")


if bmi_as_int <= 18.5:
    print(f"Your BMI is {bmi_as_int}, {underweight}")
elif bmi_as_int <= 25:
        print(f"Your BMI is {bmi_as_int}, {normalKg}")
elif bmi_as_int <= 30:
        print(f"Your BMI is {bmi_as_int}, {slghtlyOver}")  
elif bmi_as_int <= 35:
        print(f"Your BMI is {bmi_as_int}, {obese}")    
else:
    print(f"Your BMI is {bmi_as_int}, {cliObese}")
