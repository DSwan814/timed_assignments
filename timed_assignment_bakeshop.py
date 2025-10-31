tax_rate = 0.0945
items = ["Muffin", "King Cake Slice", "Croissant", "Scone"]
prices = [5.95, 4.95, 3.95, 3.75]

print("Boudreaux & Thibideaux's Bakery")
print("-------------------------------")
for i in range(len(items)):
    print(f"{i + 1}. {items[i]}: ${prices[i]: 2f}")
print("-------------------------------")

total = 0

while True:
    choice = int(input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete: "))
    if choice.upper() == "DONE":
        break
    if choice.isdigit:
        choice = int(choice)
        
        if 1 <= choice <= len(items):
            quantity = int(input(f"How many of that item would you like to order? "))
            subtotal = prices[choice -1] * quantity
            total += subtotal
            print(f"You have ordered {quantity} {items[choice - 1].lower()}(s) for ${prices[choice - 1]:.2f} each\n")
        else:
            print("I'm sorry, that is not an appropriate response.\n")

    else:
        print("I'm sorry, that is not an appropriate response.\n")

       
       
      

final_total = total + (total * tax_rate)
print("-------------------------------")
print(f"Your total is: ${total:.2f}")
