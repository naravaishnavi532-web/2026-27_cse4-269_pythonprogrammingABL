data = float(input("Enter required data (GB): "))
calls = float(input("Enter required call minutes: "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

plans = [
    ["Plan A", 199, 2, 100, 28],
    ["Plan B", 299, 5, 200, 28],
    ["Plan C", 399, 10, 300, 56]
]

best_plan = None
min_cost = float('inf')

if data < 0 or calls < 0 or validity <= 0 or budget < 0:
    print("Invalid input!")

else:
    for p in plans:
        extra_data = max(0, data - p[2])
        extra_calls = max(0, calls - p[3])

        extra_charge = extra_data * 20 + extra_calls
        total = p[1] + extra_charge

        print("\n", p[0])
        print("Excess Charges: Rs.", extra_charge)
        print("Total Cost: Rs.", total)

        if p[4] >= validity and total <= budget:
            if total < min_cost:
                min_cost = total
                best_plan = p[0]

    print("\n--- BEST PLAN ---")

    if best_plan:
        print("Most Economical Plan:", best_plan)
        print("Total Cost: Rs.", min_cost)
    else:
        print("No eligible plan found.")

