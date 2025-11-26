
def display_menu():
    print("1. Croissant: $3.95")
    print("2. King Cake Slice: $4.95")
    print("3. Crawfish Pie: $3.65 per slice or $22 for a pie (8 slices)")
    print("4. Catfish Po-boy: $14.95")
    print("5. Roast Beef Po-boy: $13.95")
    print("6.Sausage Poboy: $12.95")
    print("7. Gumbo: $5.95")

def get_price(choice):
    choice = str(choice).lower()
    if choice == "1" or choice == "croissant":
        return 5.99
    elif choice == "2" or choice == "king cake slice":
        return 3.95
    elif choice == "3" or choice == "crawfish pie":
        return 14.95
    elif choice == "4" or choice == "catfish po-boy":
        return 13.95
    elif choice == "5" or choice == "roast beef po-boy":
        return 12.95
    elif choice == "6" or choice == "sausage po-boy":
        return 5.95
    elif choice == "7" or choice == "gumbo":
        return 3.95
    else:
        return None


def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def add_tax(amount):
    return amount * 1.0945

def main():
    display_menu()
    prices = []

    while True:
        choice = input("What would you like to order? Type the appropriate number of the menu item or 0 when order is complete: ").lower()

        if choice == "0":
            break
        price = get_price(choice)
        if price is None:
            print("Invalid menu choice. Try again.")
            continue

        quantity = int(input("How many would you like?: "))
        prices.append(price *quantity)

        prices.append(get_price(choice)
                      )
    subtotal = calculate_total(prices)
    total = add_tax(subtotal)

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Total: {total:.2f}")


main()