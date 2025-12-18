# Student Marks & Grade Calculator (Enhanced Version)

name = "Kavya"
subjects = 3
marks_list = [78, 82, 69]

total = 0
valid = True

for marks in marks_list:
    if marks < 0 or marks > 100:
        valid = False
        break
    total += marks

if valid:
    average = total / subjects
    percentage = (total / (subjects * 100)) * 100

    if average >= 75:
        grade = "A"
        result = "Pass"
    elif average >= 60:
        grade = "B"
        result = "Pass"
    elif average >= 40:
        grade = "C"
        result = "Pass"
    else:
        grade = "Fail"
        result = "Fail"

    print("----- Student Result -----")
    print("Name       :", name)
    print("Subjects   :", subjects)
    print("Marks      :", marks_list)
    print("Total      :", total)
    print("Average    :", round(average, 2))
    print("Percentage :", round(percentage, 2), "%")
    print("Grade      :", grade)
    print("Result     :", result)

else:
    print("Invalid marks entered! Marks should be between 0 and 100.")