1. Problem Statement
Develop a Python program to calculate an employee’s salary based on basic pay, allowances, overtime pay, and incentives. The system should calculate the gross salary, apply progressive deductions based on salary slabs, and generate a formatted salary statement showing gross salary, deductions, and net salary.

Assumed payroll rules for this project:
- House Rent Allowance (HRA) = 20% of basic pay.
- Dearness Allowance (DA) = 10% of basic pay.
- Overtime pay = overtime hours × overtime rate per hour.
- Incentives are entered by the user.
- Progressive deductions are calculated on gross salary:
  - First ₹10,000: no deduction.
  - Next ₹10,000: 5%.
  - Next ₹20,000: 10%.
  - Amount above ₹40,000: 15%.
These are sample rules for this assignment, not actual statutory payroll or tax rules.
2. Algorithm
1. Start the program.
2. Enter the employee’s name and basic salary.
3. Calculate HRA and DA using the given percentages.
4. Enter overtime hours, overtime rate per hour, and incentives.
5. Calculate overtime pay.
6. Calculate gross salary by adding basic pay, HRA, DA, overtime pay, and incentives.
7. Calculate progressive deductions according to the salary slabs.
8. Calculate net salary by subtracting deductions from gross salary.
9. Display the formatted salary statement.
10. Stop the program.
3. Flowchart
```mermaid
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
  





```



5. Sample Input
Use the following values when you run the program.
Enter employee name: Ravi
Enter basic pay: 30000
Enter overtime hours: 10
Enter overtime rate per hour: 200
Enter incentives: 3000


6. Sample Output
===== EMPLOYEE PAYROLL SYSTEM =====

========== SALARY STATEMENT ==========
Employee Name       : Ravi
Basic Pay           : Rs. 30000.00
HRA (20%)           : Rs. 6000.00
DA (10%)            : Rs. 3000.00
Overtime Pay        : Rs. 2000.00
Incentives          : Rs. 3000.00
--------------------------------------
Gross Salary        : Rs. 44000.00
Total Deductions    : Rs. 3100.00
--------------------------------------
Net Salary          : Rs. 40900.00
======================================


Calculation:
- Gross salary = ₹30,000 + ₹6,000 + ₹3,000 + ₹2,000 + ₹3,000 = ₹44,000.
- Deduction = ₹500 + ₹2,000 + ₹600 = ₹3,100.
- Net salary = ₹44,000 − ₹3,100 = ₹40,900.
