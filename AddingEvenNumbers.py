# You are going to write a program that calculates the sum of all
# Even numbers from 1 to 100, including 1 and 100
# e.g 2+4+5.. 96+98+100
# Important, there should only be 1 print statement in your console
# output, it should just print the final total and not every step of the calculation
# hint: use for loop

total = 0
for number in range(2, 101, 2):
     total += number
print(total)