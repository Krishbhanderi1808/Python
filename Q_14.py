subject1 = 50
subject2 = 60
subject3 = 70

total = subject1 + subject2 + subject3
average = total / 3

if subject1 <= 39 or subject2 <= 39 or subject3 <= 39:
    result = "Fail"
else:
    result = "Pass"

if 0 <= subject1 <= 39:
    grade1 = "F"
elif 40 <= subject1 <= 44:
    grade1 = "P"
elif 45 <= subject1 <= 49:
    grade1 = "C"
elif 50 <= subject1 <= 54:
    grade1 = "B"
elif 55 <= subject1 <= 59:
    grade1 = "B+"
elif 60 <= subject1 <= 69:
    grade1 = "A"
elif 70 <= subject1 <= 79:
    grade1 = "A+"
elif 80 <= subject1 <= 100:
    grade1 = "O"

if 0 <= subject2 <= 39:
    grade2 = "F"
elif 40 <= subject2 <= 44:
    grade2 = "P"
elif 45 <= subject2 <= 49:
    grade2 = "C"
elif 50 <= subject2 <= 54:
    grade2 = "B"
elif 55 <= subject2 <= 59:
    grade2 = "B+"
elif 60 <= subject2 <= 69:
    grade2 = "A"
elif 70 <= subject2 <= 79:
    grade2 = "A+"
elif 80 <= subject2 <= 100:
    grade2 = "O"

if 0 <= subject3 <= 39:
    grade3 = "F"
elif 40 <= subject3 <= 44:
    grade3 = "P"
elif 45 <= subject3 <= 49:
    grade3 = "C"
elif 50 <= subject3 <= 54:
    grade3 = "B"
elif 55 <= subject3 <= 59:
    grade3 = "B+"
elif 60 <= subject3 <= 69:
    grade3 = "A"
elif 70 <= subject3 <= 79:
    grade3 = "A+"
elif 80 <= subject3 <= 100:
    grade3 = "O"
