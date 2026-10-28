

# Employee Payroll and Deduction Analysis

def calculate_deduction(gross):
    deduction = 0

    # First Rs. 10,000: 0%
    # Next Rs. 10,000: 5%
    if gross > 10000:
        deduction += min(gross - 10000, 10000) * 0.05

    # Next Rs. 20,000: 10%
    if gross > 20000:
        deduction += min(gross - 20000, 20000) * 0.10

    # Amount above Rs. 40,000: 15%
    if gross > 40000:
        deduction += (gross - 40000) * 0.15

    return deduction


print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))

overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Calculate allowances
hra = basic * 0.20
da = basic * 0.10

# Calculate overtime pay
overtime_pay = overtime_hours * overtime_rate

# Calculate gross salary
gross = basic + hra + da + overtime_pay + incentives

# Calculate progressive deductions
deduction = calculate_deduction(gross)

# Calculate net salary
net_salary = gross - deduction

# Display salary statement
print("\n========== SALARY STATEMENT ==========")
print(f"Employee Name       : {name}")
print(f"Basic Pay           : Rs. {basic:.2f}")
print(f"HRA (20%)           : Rs. {hra:.2f}")
print(f"DA (10%)            : Rs. {da:.2f}")
print(f"Overtime Pay        : Rs. {overtime_pay:.2f}")
print(f"Incentives          : Rs. {incentives:.2f}")
print("--------------------------------------")
print(f"Gross Salary        : Rs. {gross:.2f}")
print(f"Total Deductions    : Rs. {deduction:.2f}")
print("--------------------------------------")
print(f"Net Salary          : Rs. {net_salary:.2f}")
print("======================================")
