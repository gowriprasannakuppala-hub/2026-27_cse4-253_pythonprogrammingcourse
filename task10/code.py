# UNIVERSITY ADMISSION DECISION ENGINE
print("UNIVERSITY ADMISSION DECISION ENGINE")

n = int(input("Enter number of applicants: "))

courses = {
    1: ("Computer Science", 75),
    2: ("Mechanical Engineering", 65),
    3: ("Civil Engineering", 60)
}

eligible = []
rejected = []

for i in range(n):

    print("\nApplicant", i + 1)

    app_id = input("Enter application ID: ")
    name = input("Enter applicant name: ")

    math = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))

    print("\nAvailable Courses")
    for key, value in courses.items():
        print(key, ".", value[0])

    choice = int(input("Select course: "))

    if not all(0 <= m <= 100 for m in [math, physics, chemistry]):
        print("Invalid marks!")
        rejected.append((app_id, name, "Invalid marks"))
        continue

    if choice not in courses:
        print("Invalid course selection!")
        rejected.append((app_id, name, "Invalid course"))
        continue

    course_name, cutoff = courses[choice]

    aggregate = (math + physics + chemistry) / 3

    subject_eligible = (
        math >= 40 and
        physics >= 40 and
        chemistry >= 40
    )

    if subject_eligible and aggregate >= cutoff:

        eligible.append({
            "id": app_id,
            "name": name,
            "course": course_name,
            "aggregate": aggregate,
            "math": math,
            "physics": physics,
            "chemistry": chemistry
        })

    else:
        if not subject_eligible:
            reason = "Subject eligibility not satisfied"
        else:
            reason = "Aggregate below course cutoff"

        rejected.append((app_id, name, reason))

# Ranking and tie-breaking
eligible.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["math"],
        -x["physics"],
        -x["chemistry"]
    )
)

print("\n========== ADMISSION MERIT LIST ==========")

if eligible:

    for rank, student in enumerate(eligible, start=1):

        print("\nRank:", rank)
        print("Application ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Aggregate:", round(student["aggregate"], 2), "%")
        print("Mathematics:", student["math"])
        print("Physics:", student["physics"])
        print("Chemistry:", student["chemistry"])

else:
    print("No eligible candidates found.")

print("\n========== REJECTED APPLICANTS ==========")

for app_id, name, reason in rejected:
    print(app_id, "-", name, "-", reason)

print("\nAdmission Analysis Completed!")

