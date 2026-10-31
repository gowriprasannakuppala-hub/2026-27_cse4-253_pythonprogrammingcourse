#To analyze student performance across multiple examinations
print("STUDENT PERFORMANCE TREND ANALYSIS")

n = int(input("Enter number of students: "))

subjects = ["Python", "Mathematics", "English"]

for i in range(n):

    print("\nStudent", i + 1)
    name = input("Enter student name: ")

    marks = []

    for subject in subjects:
        print("\nEnter marks for", subject)

        exam1 = float(input("Exam 1: "))
        exam2 = float(input("Exam 2: "))
        exam3 = float(input("Exam 3: "))

        if not all(0 <= m <= 100 for m in [exam1, exam2, exam3]):
            print("Invalid marks! Enter marks between 0 and 100.")
            break

        marks.append([exam1, exam2, exam3])

    if len(marks) != 3:
        print("Student record skipped.")
        continue

    total = 0
    weak_subjects = []

    print("\n----- PERFORMANCE REPORT -----")
    print("Student Name:", name)

    for j in range(3):

        avg = sum(marks[j]) / 3
        improvement = marks[j][2] - marks[j][0]

        total += avg

        print("\nSubject:", subjects[j])
        print("Average:", round(avg, 2))

        if improvement > 0:
            print("Trend: Improved by", improvement)
        elif improvement < 0:
            print("Trend: Declined by", abs(improvement))
        else:
            print("Trend: No change")

        if all(m < 40 for m in marks[j]):
            weak_subjects.append(subjects[j])

    overall_average = total / 3

    print("\nOverall Average:", round(overall_average, 2))

    if overall_average >= 75:
        category = "Excellent"
    elif overall_average >= 60:
        category = "Good"
    elif overall_average >= 40:
        category = "Average"
    else:
        category = "Needs Improvement"

    print("Student Classification:", category)

    if weak_subjects:
        print("Consistently Weak Subjects:", weak_subjects)
    else:
        print("No Consistently Weak Subjects")

print("\nAnalysis Completed!")

