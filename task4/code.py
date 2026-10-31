name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentives: "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid input! Values cannot be negative.")

else:
    allowance = basic * 0.20
    overtime = hours * 200

    gross = basic + allowance + overtime + incentive

    if gross <= 10000:
        deduction = 0
    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05
    else:
        deduction = 500 + (gross - 20000) * 0.10

    net = gross - deduction

    print("\n--- SALARY STATEMENT ---")
    print("Employee Name:", name)
    print("Basic Pay: Rs.", basic)
    print("Allowances: Rs.", allowance)
    print("Overtime Pay: Rs.", overtime)
    print("Incentives: Rs.", incentive)
    print("Gross Salary: Rs.", gross)
    print("Total Deduction: Rs.", deduction)
    print("Net Salary: Rs.", net)

