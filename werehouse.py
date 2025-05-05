items = [ 
    {"name" : "tomatoes", "quantity" : 345, "unit" : "kg", "unit_price": 9.40},
    {"name" : "cucumbers", "quantity" : 230, "unit" : "kg", "unit_price": 7.20},
    {"name" : "potatoes", "quantity" : 980, "unit" : "kg", "unit_price": 4.50},
    {"name" : "apples", "quantity" : 500, "unit" : "kg", "unit_price": 12.20},
    {"name" : "pears", "quantity" : 450, "unit" : "kg", "unit_price": 15.60}
]
floor = "_"
def add_item():
        while True:
            try: 
                name = input("Enter the name of the item: ")
                quantity = int(input("Enter the quantity: "))
                unit_name = input("Enter the unit: ")
                unit_price = float(input("Enter the unit price: "))
                new_item = {
                    "name": name,
                    "quantity": quantity,
                    "unit": unit_name,
                    "unit_price": unit_price
                }
                items.append(new_item)
            except ValueError:
                print("Wrong data type. Try again!")
                continue
            if name == "" or quantity <= 0 or unit_name == "" or unit_price <= 0:
                print("Wrong data. Try again!")
                continue
            if any(item['name'] == name for item in items):
                print("Item already exists. Try again!")
                continue
            if name == "exit" or quantity == exit or unit_name == "exit" or unit_price == exit:
                print("Exiting the program...")
                exit(0)
            print("Item added successfully! Curent werehouse status:")
            get_items(items)
            break

def get_items(items):
    print(f"{'Name':<15}{'Quantity':<10}{'Unit':<10}{'Unit Price PLN':<15}")
    print(f"{(floor * 4):<15}{(floor * 8):<10}{(floor * 4):<10}{(floor * 15):<15}")
    for item in items:
        print(f"{item['name']:<15}{item['quantity']:<10}{item['unit']:<10}{(item['unit_price']):.2f}")
while True:
    prompt = input("What would you like to do? ").strip().lower()
    if prompt == "show":
        get_items(items)
    elif prompt == "add":
        add_item()
    elif prompt == "exit":
        print("Exiting the program...")
        exit(0)
    else:
        print("Wrong command. Try again.")

    

            



            

