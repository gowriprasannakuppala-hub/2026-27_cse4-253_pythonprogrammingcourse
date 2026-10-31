#calculate railway ticket fares for multiple passengers
print("RAILWAY FARE AND RESERVATION CALCULATOR")

n = int(input("Enter number of passengers: "))

total_amount = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter journey distance in km: "))

    print("\nTravel Classes")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")

    choice = int(input("Select travel class: "))

    # Distance slab fare
    if distance <= 100:
        rate = 1.0
    elif distance <= 300:
        rate = 1.5
    else:
        rate = 2.0

    # Travel class selection
    if choice == 1:
        class_name = "Sleeper"
        multiplier = 1
    elif choice == 2:
        class_name = "AC 3 Tier"
        multiplier = 2
    elif choice == 3:
        class_name = "AC 2 Tier"
        multiplier = 3
    else:
        print("Invalid class selection")
        continue

    basic_fare = distance * rate * multiplier

    # Age concession
    if age < 5:
        basic_fare = 0
    elif age >= 60:
        basic_fare = basic_fare * 0.80

    reservation_fee = 40

    total_fare = basic_fare + reservation_fee

    print("\nCancellation")
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = basic_fare * 0.25
        final_fare = penalty
        print("Cancellation penalty: Rs.", penalty)
    else:
        final_fare = total_fare

    print("\nPassenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Travel Class:", class_name)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Final Fare: Rs.", round(final_fare, 2))

    total_amount += final_fare

print("\n------------------------------")
print("Total Amount: Rs.", round(total_amount, 2))
print("------------------------------")
print("Thank you for using Railway Calculator!")

