
# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN COST OPTIMIZATION =====")


data_usage = float(input("Enter required data usage (GB): "))
call_usage = float(input("Enter required call minutes: "))
min_validity = int(input("Enter minimum validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

n = int(input("Enter number of mobile plans: "))

plans = []
eligible_plans = []

for i in range(n):
    print(f"\nEnter details for Plan {i + 1}")

    name = input("Plan name: ")
    price = float(input("Plan price (Rs.): "))
    included_data = float(input("Included data (GB): "))
    included_calls = int(input("Included call minutes: "))
    validity = int(input("Validity (days): "))
    extra_data_rate = float(input("Extra data charge per GB: "))
    extra_call_rate = float(input("Extra call charge per minute: "))

   
    excess_data = max(0, data_usage - included_data)
    excess_calls = max(0, call_usage - included_calls)

    data_charge = excess_data * extra_data_rate
    call_charge = excess_calls * extra_call_rate


    total_cost = price + data_charge + call_charge

    plan = {
        "name": name,
        "price": price,
        "excess_data": excess_data,
        "excess_calls": excess_calls,
        "data_charge": data_charge,
        "call_charge": call_charge,
        "total_cost": total_cost,
        "validity": validity
    }

    plans.append(plan)

    
    if total_cost <= budget and validity >= min_validity:
        eligible_plans.append(plan)


print("\n========== PLAN COST COMPARISON ==========")

for plan in plans:
    status = (
        "Eligible"
        if plan in eligible_plans
        else "Not eligible"
    )

    print(f"\nPlan: {plan['name']}")
    print(f"Base price: Rs. {plan['price']:.2f}")
    print(f"Extra data charge: Rs. {plan['data_charge']:.2f}")
    print(f"Extra call charge: Rs. {plan['call_charge']:.2f}")
    print(f"Total cost: Rs. {plan['total_cost']:.2f}")
    print(f"Validity: {plan['validity']} days")
    print(f"Status: {status}")


print("\n========== BEST PLAN ==========")

if eligible_plans:
    best_plan = min(
        eligible_plans,
        key=lambda p: (p["total_cost"], p["name"].lower())
    )

    print("Most economical plan:", best_plan["name"])
    print(f"Total cost: Rs. {best_plan['total_cost']:.2f}")
    print(f"Validity: {best_plan['validity']} days")
else:
    print("No plan satisfies both budget and validity requirements.")

print("==========================================")

