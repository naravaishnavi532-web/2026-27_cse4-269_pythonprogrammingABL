name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
income = float(input("Enter annual income: "))

consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

if age < 0 or income < 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input! Values cannot be negative.")

else:
    total = consultation + diagnostic + treatment
    concession = 0

    if age >= 60:
        concession += 10

    if income < 150000:
        concession += 5

    if concession > 15:
        concession = 15

    discount = total * concession / 100
    final_bill = total - discount

    if final_bill == 0:
        category = "Full Concession"
    elif final_bill <= 2000:
        category = "Low Payment"
    else:
        category = "Regular Payment"

    print("\n--- BILL DETAILS ---")
    print("Patient Name:", name)
    print("Total Bill: Rs.", total)
    print("Concession:", concession, "%")
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final_bill)
    print("Patient Classification:", category)

