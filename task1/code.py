# University Scholarship Allocation
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000
def check_eligibility(student):
    reasons = []

    if student["aggregate"] < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if any(mark < MIN_SUBJECT_MARK for mark in student["subjects"]):
        reasons.append("A subject mark is below 60%")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if student["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 2,50,000")

    return reasons


students = []
eligible_students = []
ineligible_students = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nApplicant {i + 1}")

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate percentage: "))

    subject_count = int(input("Enter number of subjects: "))
    subjects = []

    for j in range(subject_count):
        mark = float(input(f"Enter marks for subject {j + 1}: "))
        subjects.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = {
        "name": name,
        "aggregate": aggregate,
        "subjects": subjects,
        "attendance": attendance,
        "income": income
    }

    reasons = check_eligibility(student)

    if not reasons:
        eligible_students.append(student)
    else:
        ineligible_students.append((student, reasons))

# Ranking: aggregate descending, attendance descending,
# income ascending, then name alphabetically.
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

print("\n===== SCHOLARSHIP RANK LIST =====")

if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"Rank {rank}: {student['name']} | "
            f"Aggregate: {student['aggregate']}% | "
            f"Attendance: {student['attendance']}% | "
            f"Income: Rs. {student['income']:.0f}"
        )
else:
    print("No eligible students found.")

print("\n===== INELIGIBLE STUDENTS =====")

if ineligible_students:
    for student, reasons in ineligible_students:
        print(f"{student['name']}: {'; '.join(reasons)}")
else:
    print("All applicants are eligible.")
