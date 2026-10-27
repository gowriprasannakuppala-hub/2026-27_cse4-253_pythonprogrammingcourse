
# Hospital Billing and Patient Classification System

CONSULTATION_FEE = 500
SENIOR_AGE = 60
SENIOR_CONCESSION = 0.10
HIGH_BILL_LIMIT = 10000
HIGH_BILL_CONCESSION = 0.05


def calculate_bill(age, diagnostic, treatment):
    original_bill = (
        CONSULTATION_FEE + diagnostic + treatment
    )

    concession_rate = 0

  
    if age >= SENIOR_AGE:
        concession_rate += SENIOR_CONCESSION

   
    if original_bill > HIGH_BILL_LIMIT:
        concession_rate += HIGH_BILL_CONCESSION


    concession_rate = min(concession_rate, 0.15)

    concession = original_bill * concession_rate
    final_bill = original_bill - concession

    return original_bill, concession, final_bill


def classify_patient(final_bill):
    if final_bill < 2000:
        return "Low Payment"
    elif final_bill <= 10000:
        return "Medium Payment"
    else:
        return "High Payment"


print("HOSPITAL BILLING SYSTEM")

try:
    name = input("Enter patient name: ").strip()
    age = int(input("Enter patient age: "))
    diagnostic = float(input("Enter diagnostic charges: Rs. "))
    treatment = float(input("Enter treatment charges: Rs. "))

 
    if not name:
        print("Error: Patient name cannot be empty.")
    elif age < 1 or age > 120:
        print("Error: Age must be between 1 and 120.")
    elif diagnostic < 0 or treatment < 0:
        print("Error: Charges cannot be negative.")
    else:
        original, concession, final = calculate_bill(
            age, diagnostic, treatment
        )

        category = classify_patient(final)

        print("\n--- HOSPITAL BILL ---")
        print("Patient Name:", name)
        print("Patient Age:", age)
        print(f"Consultation Fee: Rs. {CONSULTATION_FEE:.2f}")
        print(f"Diagnostic Charges: Rs. {diagnostic:.2f}")
        print(f"Treatment Charges: Rs. {treatment:.2f}")
        print(f"Original Bill: Rs. {original:.2f}")
        print(f"Concession: Rs. {concession:.2f}")
        print(f"Final Bill: Rs. {final:.2f}")
        print("Patient Classification:", category)

except ValueError:
    print("Error: Enter valid numeric values for age and charges.")

