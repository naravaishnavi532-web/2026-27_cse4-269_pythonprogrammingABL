name = input("Enter customer name: ")
n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0
items = []

for i in range(n):
    print("\nProduct", i + 1)

    product = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ").lower()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 10
    elif category == "electronics":
        tax_rate = 18
    else:
        print("Invalid category!")
        continue

    amount = price * quantity
    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    items.append([product, quantity, amount, tax])

if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

discount = min(discount, 500)
final_bill = subtotal + total_tax - discount

print("\n------ ITEMIZED INVOICE ------")
print("Customer Name:", name)

for item in items:
    print("\nProduct:", item[0])
    print("Quantity:", item[1])
    print("Amount: Rs.", item[2])
    print("Tax: Rs.", item[3])

print("\nSubtotal: Rs.", subtotal)
print("Total Tax: Rs.", total_tax)
print("Discount: Rs.", discount)
print("Final Payable Amount: Rs.", final_bill)

