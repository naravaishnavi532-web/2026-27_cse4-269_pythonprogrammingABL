
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks (%): "))
    subjects = int(input("Enter number of subjects: "))

    marks = []
    for j in range(subjects):
        mark = float(input("Enter marks for subject " + str(j + 1) + ": "))
        marks.append(mark)

    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income (Rs.): "))

    if (aggregate >= 75 and all(m >= 60 for m in marks)
            and attendance >= 75 and income <= 250000):
        students.append([name, aggregate, attendance, income])

students.sort(key=lambda s: (-s[1], -s[2], s[3], s[0].lower()))

if students:
    print("\nEligible Students - Scholarship Ranking")
    for rank, s in enumerate(students, start=1):
        print(rank, s[0], "| Aggregate:", s[1],
              "| Attendance:", s[2], "| Income:", s[3])
else:
    print("\nNo students are eligible for the scholarship.")

