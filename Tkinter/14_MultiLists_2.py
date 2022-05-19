
#Creating list of students & printing current state of students list before appending
students = ["Connor", "Tariq", "Leo", "Meical", "Shawn", "Austin"]
print(students)

#Students to append to the list named students
students_append = ["Paul", "Wei Xiang"]


for x in range(len(students_append)):
    students.append(students_append[x])
    print(students)

