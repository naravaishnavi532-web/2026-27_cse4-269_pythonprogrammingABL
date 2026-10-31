
# Campus Event Financial Planning

import math

participants = int(input("Enter expected number of participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Calculate costs
fixed_cost = venue + equipment + transport

variable_cost = (catering + certificate) * participants

total_cost = fixed_cost + variable_cost

# Calculate participant contributions
contributions = participants * registration_fee

total_funds = contributions + sponsorship

# Calculate shortfall or surplus
difference = total_funds - total_cost

# Calculate break-even registrations
cost_per_participant = catering + certificate
remaining_fixed_cost = max(0, fixed_cost - sponsorship)

print("\n--- Campus Event Financial Report ---")
print("Fixed Costs:", fixed_cost)
print("Variable Costs:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", contributions)
print("Sponsorship:", sponsorship)

if difference >= 0:
    print("Financial Surplus:", difference)
else:
    print("Sponsorship Shortfall:", abs(difference))

# Break-even calculation
if registration_fee > cost_per_participant:
    minimum = math.ceil(
        remaining_fixed_cost /
        (registration_fee - cost_per_participant)
    )
    print("Minimum Registrations for Break-even:", minimum)
else:
    print("Break-even cannot be achieved with this registration fee.")

