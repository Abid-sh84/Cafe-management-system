menu = {
    'pizza': 100,
    'coffee': 80,
    'salad': 70,
    'burger': 250, 
    'water-bottle': 50,  
    'pasta': 50,
}

print("Welcome to my restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order: ").lower()
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Order item '{item}' is not available yet.")
    
    another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_order != 'yes':
        break

print(f"Total amount to be paid is: Rs{order_total}")
