#If the bill was $150.00, Split between 5 people, with 12% tip/

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
percentTip = int(input("What percentage tip would you like to give? 10,12, or 15?? "))
splitBill = int(input("How many People to split the bill? "))

tip_as_percent = percentTip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / splitBill

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")