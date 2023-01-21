
Year = int(input("Which year do you want to check? "))

Year1 = Year % 4
year2 = Year % 100
year3 = Year % 400

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("This is a Leap Year")       
        else:
            print("This is not a Leap Year")
    else:
        print("This a Leap Year")
else:
    print("This is not a Leap Year")

