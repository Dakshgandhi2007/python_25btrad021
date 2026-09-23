def calculate_bill(items):
    total = 0
    print("\n----- BILL -----")
    print(f"{'Item':<15}{'Price':<10}{'Qty':<5}{'Amount':<10}")
    print("-" * 40)
    
    for item, price, qty in items:
        amount = price * qty
        total += amount
        print(f"{item:<15}{price:<10.2f}{qty:<5}{amount:<10.2f}")  # fixed
    
    print("-" * 40)
    print(f"{'Total':<30}{total:.2f}")  # fixed

n = int(input("How many items? "))
items = []

for i in range(n):
    print(f"\nItem {i+1}:")
    name = input("  Name: ")
    price = float(input("  Price per unit: "))
    qty = int(input("  Quantity: "))
    items.append((name, price, qty))

calculate_bill(items)
