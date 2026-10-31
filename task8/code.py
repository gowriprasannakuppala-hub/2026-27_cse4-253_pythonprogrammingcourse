#FUEL CONSUMPTION AND ROUTE COMPARISON
print("FUEL CONSUMPTION AND ROUTE COMPARISON")

n = int(input("Enter number of vehicles: "))

distance = float(input("Enter journey distance in km: "))
reserve_percent = float(input("Enter reserve fuel percentage: "))

vehicles = []

for i in range(n):

    print("\nVehicle", i + 1)

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/l): "))
    fuel_price = float(input("Enter fuel price per litre: "))
    available_fuel = float(input("Enter available fuel in litres: "))

    if mileage <= 0 or fuel_price <= 0 or available_fuel < 0:
        print("Invalid vehicle details!")
        continue

    fuel_required = distance / mileage

    reserve_fuel = fuel_required * reserve_percent / 100

    total_fuel = fuel_required + reserve_fuel

    cost = fuel_required * fuel_price

    feasible = available_fuel >= total_fuel

    vehicles.append({
        "name": name,
        "fuel": fuel_required,
        "reserve": reserve_fuel,
        "total": total_fuel,
        "cost": cost,
        "feasible": feasible
    })

print("\n----- VEHICLE COMPARISON REPORT -----")

for v in vehicles:

    print("\nVehicle:", v["name"])
    print("Fuel Required:", round(v["fuel"], 2), "litres")
    print("Reserve Fuel:", round(v["reserve"], 2), "litres")
    print("Total Fuel Needed:", round(v["total"], 2), "litres")
    print("Journey Cost: Rs.", round(v["cost"], 2))

    if v["feasible"]:
        print("Status: Feasible")
    else:
        print("Status: Not Feasible")

feasible_vehicles = [
    v for v in vehicles if v["feasible"]
]

if feasible_vehicles:

    best = min(feasible_vehicles, key=lambda x: x["cost"])

    print("\n----- BEST OPTION -----")
    print("Lowest Cost Vehicle:", best["name"])
    print("Minimum Journey Cost: Rs.", round(best["cost"], 2))

else:
    print("\nNo vehicle satisfies the fuel reserve requirement.")

print("\nAnalysis Completed!")

