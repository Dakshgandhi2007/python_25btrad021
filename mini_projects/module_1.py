item = input("Enter item name: ")
price = float(input("Enter price per unit: "))
qty = int(input("Enter quantity: "))

total = price * qty

print("\n----- BILL -----")
print(f"Item: {item}")
print(f"Price per unit: {price}")
print(f"Quantity: {qty}")
print(f"Total Amount: {total:.2f}")
