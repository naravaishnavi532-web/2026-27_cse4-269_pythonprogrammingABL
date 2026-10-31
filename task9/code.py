
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expense categories: "))

total_spending = 0
largest_expense = 0
largest_category = ""

for i in range(n):
    print("\nCategory", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    rate = float(input("Enter exchange rate (INR): "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    # Currency conversion
    converted_amount = amount * rate

    # Calculate conversion fee
    fee = converted_amount * fee_percent / 100

    # Total expense
    expense = converted_amount + fee

    total_spending += expense

    print("Expense in INR:", round(expense, 2))

    # Find largest expense
    if expense > largest_expense:
        largest_expense = expense
        largest_category = category

# Compare spending with budget
print("\n--- Travel Budget Report ---")
print("Total Spending:", round(total_spending, 2))
print("Largest Expense Category:", largest_category)
print("Largest Expense:", round(largest_expense, 2))

if total_spending <= budget:
    print("Remaining Budget:", round(budget - total_spending, 2))
    print("Travel is within the budget.")
else:
    print("Budget Exceeded By:", round(total_spending - budget, 2))
    print("Travel is over the budget.")

