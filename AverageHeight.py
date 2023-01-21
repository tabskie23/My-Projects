#Don't change the code below

student_heights = input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
#Don't change the code above

total_height = 0
for height in student_heights:
    total_height += height

print(total_height)
total_student = 0
for student in student_heights:
   total_student += 1

print(total_student) 
average_height = round(total_height / total_student)

print(average_height)
