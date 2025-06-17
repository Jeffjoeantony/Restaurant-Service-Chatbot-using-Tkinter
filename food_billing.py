# Restaurant Food Billing Program 

print("Welcome to ABC Restaurant")
input("!! Press ENTER to proceed !!")

c_name = input("Please enter your name: ")
c_phone = int(input("Please enter your phone number: "))
c_details = (c_name, c_phone)

menu = {
    "Veg Fried Rice": 100.00,
    "Non-veg Fried Rice": 120.00,
    "Chicken Biriyani": 150.00,
    "Lime Juice": 25.00
}

print()
print("     --------M.E.N.U--------     ")
print("  Items                    Price")
print("1. Veg Fried Rice           100.00")
print("2. Non-veg Fried Rice       120.00")
print("3. Chicken Biriyani         150.00")
print("4. Lime Juice               25.00\n")

while True:
    itms = int(input("Enter number of items (1 or 2): "))
    if itms in (1, 2):
        break
    else:
        print("Invalid input. Please enter 1 or 2.")

while True:
    itm1 = input("Enter item 1: ")
    if itm1 in menu:
        qty1 = int(input("Quantity: "))
        break
    else:
        print("Item not in menu")

item1_total = menu[itm1] * qty1
item2_total = 0

if itms == 2:
    while True:
        itm2 = input("Enter item 2: ")
        if itm2 in menu:
            qty2 = int(input("Quantity: "))
            item2_total = menu[itm2] * qty2
            break
        else:
            print("Item not in menu")

total_bill = item1_total + item2_total

print("\n-----------------")
print("     BILL        ")
print("-----------------")
print("Customer:", c_details)
print(f"{itm1} * {qty1} = {item1_total}")
if itms == 2:
    print(f"{itm2} * {qty2} = {item2_total}")
print("-----------------")
print("Total:",total_bill)
print("THANK YOU")

