# Case Study 1: University Scholarship Allocation

## 1. Problem Statement

Develop a Python program to allocate university scholarships based on students’ academic performance and eligibility criteria. The system should evaluate each applicant using aggregate marks, subject-wise minimum marks, attendance percentage, and family annual income.

The program should identify eligible students, rank them according to their aggregate marks, and resolve ties using predefined rules. In this case study, the tie-breaking rules are:

1. Higher aggregate marks receive a higher rank.
2. If aggregate marks are equal, higher attendance receives a higher rank.
3. If both are equal, lower family annual income receives a higher rank.

Assumed eligibility criteria:

- Aggregate marks: at least 75%.
- Minimum marks in every subject: 60%.
- Attendance: at least 75%.
- Annual family income: not more than ₹2,50,000.

These are sample rules for the project; actual university scholarship rules may differ.

## 2. Algorithm

1. Start the program.
2. Read the number of student applicants.
3. For each applicant, read their name, aggregate marks, subject-wise marks, attendance, and annual family income.
4. Check whether the applicant satisfies all four eligibility criteria.
5. Store eligible applicants in a list.
6. Sort the eligible applicants by:
   - Aggregate marks in descending order.
   - Attendance in descending order.
   - Annual family income in ascending order.
7. Assign ranks to eligible applicants.
8. Display the eligible students with their ranks.
9. Display the students who are not eligible and their reasons.
10. Stop the program.

## 3. Flowchart
mermaid
```

flowchart TD
    A([Start]) --> B[/Input number of applicants/]
    B --> C[/Input name, aggregate, subject marks, attendance and income/]
    C --> D{All eligibility criteria satisfied?}
    D -- Yes --> E[Store eligible student]
    D -- No --> F[Record rejection reasons]
    E --> G{More applicants?}
    F --> G
    G -- Yes --> C
    G -- No --> H[Sort eligible students by aggregate, attendance, income and name]
    H --> I[Assign ranks]
    I --> J[/Display rank list and rejected applicants/]
    J --> K([Stop])

```


## 5. Sample Input

For testing, enter these values when you run the program.

```
Enter number of applicants: 3

Applicant 1
Enter student name: Asha
Enter aggregate percentage: 82
Enter number of subjects: 2
Enter marks for subject 1: 82
Enter marks for subject 2: 80
Enter attendance percentage: 90
Enter annual family income: 200000

Applicant 2
Enter student name: Ravi
Enter aggregate percentage: 82
Enter number of subjects: 2
Enter marks for subject 1: 80
Enter marks for subject 2: 84
Enter attendance percentage: 90
Enter annual family income: 150000

Applicant 3
Enter student name: Sita
Enter aggregate percentage: 78
Enter number of subjects: 2
Enter marks for subject 1: 70
Enter marks for subject 2: 80
Enter attendance percentage: 88
Enter annual family income: 220000
```

## 6. Sample Output

```
===== SCHOLARSHIP RANK LIST =====
Rank 1: Ravi | Aggregate: 82.0% | Attendance: 90.0% | Income: Rs. 150000
Rank 2: Asha | Aggregate: 82.0% | Attendance: 90.0% | Income: Rs. 200000
Rank 3: Sita | Aggregate: 78.0% | Attendance: 88.0% | Income: Rs. 220000

===== INELIGIBLE STUDENTS =====
All applicants are eligible.
```

Why is Ravi ranked first? Ravi and Asha have the same aggregate marks and attendance. Ravi has a lower family income, so Ravi receives the higher rank.


