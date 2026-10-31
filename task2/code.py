
bills = []
n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter electricity units consumed: "))

    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 200 + (units - 100) * 3
    else:
        energy = 500 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05
    rebate = 20 if units < 100 else 0

    total = energy + fixed + surcharge - rebate
    bills.append(total)

    print("Energy Charge:", energy)
    print("Fixed Charge:", fixed)
    print("Surcharge:", surcharge)
    print("Rebate:", rebate)
    print("Total Bill: Rs.", round(total, 2))

print("\nMonthly Bill Comparison")

for i in range(n):
    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = ((bills[i] - bills[i-1]) / bills[i-1]) * 100

        if increase > 30:
            print("Unusual Increase:", round(increase, 2), "%")
        else:
            print("Normal Increase/Change:", round(increase, 2), "%")

