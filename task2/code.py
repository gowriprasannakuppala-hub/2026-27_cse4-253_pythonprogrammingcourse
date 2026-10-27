
# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.05
INCREASE_LIMIT = 30


def calculate_bill(units):
 
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 3)

    else:
        energy_charge = (
            (100 * 2)
            + (100 * 3)
            + ((units - 200) * 5)
        )


    surcharge = 0
    rebate = 0

    if units > 200:
        surcharge = energy_charge * SURCHARGE_RATE

    elif units < 100:
        rebate = energy_charge * REBATE_RATE

  
    total_bill = (
        energy_charge
        + FIXED_CHARGE
        + surcharge
        - rebate
    )

    return energy_charge, surcharge, rebate, total_bill



months = int(input("Enter number of months: "))

if months < 1:
    print("Number of months must be at least 1.")

else:
    bills = []
    consumptions = []

   
    for month in range(1, months + 1):
        units = int(input(f"Enter units for month {month}: "))

        if units < 0:
            print("Units cannot be negative.")
            break

        energy, surcharge, rebate, total = calculate_bill(units)

        consumptions.append(units)
        bills.append(total)

        print(f"\nMonth {month}")
        print(f"Units consumed: {units}")
        print(f"Energy charge: Rs. {energy:.2f}")
        print(f"Fixed charge: Rs. {FIXED_CHARGE:.2f}")
        print(f"Surcharge: Rs. {surcharge:.2f}")
        print(f"Rebate: Rs. {rebate:.2f}")
        print(f"Total bill: Rs. {total:.2f}")

  
    if len(bills) == months:
        print("\n--- Monthly Bill Comparison ---")

        for i in range(1, len(bills)):
            previous_bill = bills[i - 1]
            current_bill = bills[i]

            increase = (
                (current_bill - previous_bill)
                / previous_bill
            ) * 100

            print(
                f"Month {i} to Month {i + 1}: "
                f"{increase:.2f}% change"
            )

            if increase > INCREASE_LIMIT:
                print("Warning: Unusual bill increase!")
            else:
                print("No unusual increase.")

    print("\nBilling process completed.")

