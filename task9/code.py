# MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT
print("MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT")

n = int(input("Enter number of products: "))
budget = float(input("Enter your shopping budget: "))

products = []

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price <= 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

def calculate_total(items):
    subtotal = sum(
        p["price"] * p["quantity"] for p in items
    )

    if subtotal >= 5000:
        discount = subtotal * 0.10
    else:
        discount = 0

    return subtotal, discount, subtotal - discount

subtotal, discount, total = calculate_total(products)

print("\nOriginal Shopping Total:", round(total, 2))

# Reduce quantities if budget is exceeded
products.sort(key=lambda x: x["price"], reverse=True)

while total > budget:

    reduced = False

    for p in products:
        if p["quantity"] > 1:
            p["quantity"] -= 1
            reduced = True
            break

    if not reduced:
        break

    subtotal, discount, total = calculate_total(products)

print("\n----- FINAL SHOPPING REPORT -----")

for p in products:
    cost = p["price"] * p["quantity"]

    print("\nProduct:", p["name"])
    print("Quantity:", p["quantity"])
    print("Price:", p["price"])
    print("Total:", round(cost, 2))

print("\nSubtotal:", round(subtotal, 2))
print("Discount:", round(discount, 2))
print("Final Amount:", round(total, 2))

if total <= budget:
    print("Status: Within Budget")
    print("Remaining Budget:", round(budget - total, 2))
else:
    print("Status: Budget Cannot Be Met")
    print("Minimum Amount Required:", round(total, 2))

print("\nShopping Analysis Completed!")

