
# Manufacturing Cost and Profitability Analysis

units = int(input("Enter number of units produced: "))

material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage = float(input("Enter wastage percentage: "))
machine = float(input("Enter total machine cost: "))

selling_price = float(input("Enter selling price per unit: "))
target = float(input("Enter required profit percentage: "))

# Calculate costs
material_cost = units * material
wastage_cost = material_cost * wastage / 100
labour_cost = units * labour

total_cost = material_cost + wastage_cost + labour_cost + machine

# Calculate revenue and profit
revenue = units * selling_price
profit = revenue - total_cost

profit_percentage = (profit / total_cost) * 100

# Display results
print("\n--- Manufacturing Report ---")
print("Material Cost:", material_cost)
print("Wastage Cost:", wastage_cost)
print("Labour Cost:", labour_cost)
print("Machine Cost:", machine)
print("Total Manufacturing Cost:", total_cost)
print("Total Revenue:", revenue)
print("Profit:", profit)
print("Profit Percentage:", round(profit_percentage, 2), "%")

# Check profit target
if profit_percentage >= target:
    print("Production meets the profit target.")
else:
    print("Production does not meet the profit target.")

