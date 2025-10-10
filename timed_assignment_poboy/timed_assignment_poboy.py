tax_rate = 0.0945  #9.45%
print("Boudreaux & Thibideaux's Po-Boy Shop")
print("------------------------------------")
print("1. Catfish Poboy: $14.95")
print("2. Roast Beef Poboy: $13.95")
print("3. Sausage Poboy: $12.95")
print("4. Gumbo: $4.95")
print("------------------------------------")




poboy_order = float(input("Enter the price of menu item to calculate the new total with tax: "))



subtotal = poboy_order 
tax = subtotal * tax_rate
total = poboy_order + tax


print(f"Your total is: ${total:.2f}")