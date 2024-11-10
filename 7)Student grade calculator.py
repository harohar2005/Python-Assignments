

name = input("Enter student's name: ")
subjects = int(input("Enter number of subjects: "))
scores = [int(input("Enter score: ")) for _ in range(subjects)]
average = sum(scores) / len(scores)

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 60 <= average < 70:
    grade = 'D'
else:
    grade = 'F'


print(f"{name}'s average score: {average}")
print(f"Grade: {grade}")