n = int(input("Enter number of passengers: "))
distance = float(input("Enter travel distance (km): "))

print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")

choice = int(input("Select travel class: "))

if choice == 1:
    class_name = "Sleeper"
    class_charge = 100
elif choice == 2:
    class_name = "AC 3 Tier"
    class_charge = 300
elif choice == 3:
    class_name = "AC 2 Tier"
    class_charge = 500
else:
    class_name = ""
    class_charge = 0

if n <= 0 or distance <= 0 or choice not in [1, 2, 3]:
    print("Invalid input!")

else:
    cancel = input("Cancel ticket? (yes/no): ").lower()
    if cancel not in ["yes", "no"]:
        print("Invalid cancellation choice!")
    else:
        total = 0

        for i in range(n):
            print("\nPassenger", i + 1)
            name = input("Enter passenger name: ")
            age = int(input("Enter age: "))

            if age < 0:
                print("Invalid age!")
                continue

            if distance <= 100:
                fare = distance * 2
            elif distance <= 300:
                fare = 200 + (distance - 100) * 1.5
            else:
                fare = 500 + (distance - 300) * 1

            fare += class_charge

            if age >= 60:
                concession = 20
            elif age < 12:
                concession = 50
            else:
                concession = 0

            discount = fare * concession / 100
            discounted = fare - discount
            reservation = 50
            bill = discounted + reservation

            print("Passenger:", name)
            print("Travel Class:", class_name)
            print("Basic Fare:", fare)
            print("Concession:", concession, "%")

            if cancel == "yes":
                penalty = discounted * 0.25
                refund = discounted - penalty
                print("Cancellation Penalty:", penalty)
                print("Refund Amount:", refund)
                print("Reservation Fee (non-refundable):", reservation)
            else:
                total += bill
                print("Reservation Fee:", reservation)
                print("Final Fare:", bill)

        if cancel == "no":
            print("\nTotal Booking Amount: Rs.", total)

