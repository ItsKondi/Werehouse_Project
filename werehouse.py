# -*- coding: utf-8 -*-
import csv

items = [ 
    {"name" : "tomatoes", "quantity" : 345, "unit" : "kg", "unit_price": 9.40},
    {"name" : "cucumbers", "quantity" : 230, "unit" : "kg", "unit_price": 7.20},
    {"name" : "potatoes", "quantity" : 980, "unit" : "kg", "unit_price": 4.50},
    {"name" : "apples", "quantity" : 500, "unit" : "kg", "unit_price": 12.20},
    {"name" : "pears", "quantity" : 450, "unit" : "kg", "unit_price": 15.60}
]

sold_itmes = []

floor = "_"
def add_item():
        while True:
            try: 
                name = input("Enter the name of the item: ").strip().lower()
                if name == "exit":
                    print("Coming back to the main menu...")
                    break
                if any(item['name'] == name for item in items):
                    quantity = float(input("Enter the quantity: "))
                    items[items.index(next(item for item in items if item['name'] == name))]['quantity'] += quantity
                    print("Item already exists. Quantity updated.")
                    break
                    

                quantity = float(input("Enter the quantity: "))
                unit_name = input("Enter the unit: ").strip().lower()
                if unit_name == "exit":
                    print("Coming back to the main menu...")
                    break
                
                unit_price = float(input("Enter the unit price: "))

                if name == "" or quantity <= 0 or unit_name == "" or unit_price <= 0:
                    print("Wrong data. Try again!")
                    continue
                
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
            print("Item added successfully! Curent werehouse status:")
            get_items(items)
            break
def sell_item():
    while True:
        try:
            name = input("Enter the name of the item to sell: ").strip().lower()
            if name == "exit":
                print("Coming back to the main menu...")
                break

            item = next((i for i in items if i['name'] == name), None)
            if not item:
                print("Item not found. Try again!")
                continue

            quantity = float(input("Enter the quantity to sell: "))
            if quantity <= 0:
                print("Quantity must be greater than 0. Try again!")
                continue

            if item['quantity'] < quantity:
                print(f"Not enough items in stock. Available: {item['quantity']} {item['unit']}. Try again!")
                continue

            item['quantity'] -= quantity
            print(f"Sold {quantity} {item['unit']} of {name} for {quantity * item['unit_price']:.2f} PLN.")

            sold_item = next((si for si in sold_itmes if si['name'] == name), None)
            if sold_item:
                sold_item['quantity'] += quantity
            else:
                sold_itmes.append({
                    "name": name,
                    "quantity": quantity,
                    "unit": item['unit'],
                    "unit_price": item['unit_price']
                })
            print("\nCurrent warehouse status:")
            get_items(items)
            print("\nSold items status:")
            get_items(sold_itmes)

            return

        except ValueError:
            print("Invalid input. Please try again!")

def get_costs():
    total_costs = sum(item['unit_price'] * item['quantity'] for item in items)
    return total_costs

def get_income():
    total_income = sum(item['unit_price'] * item['quantity'] for item in sold_itmes)
    return total_income

def show_revenue():
    total_costs = get_costs()
    total_income = get_income()
    profit = total_income - total_costs
    print(f"Total costs: {total_costs:.2f} PLN")
    print(f"Total income: {total_income:.2f} PLN")
    print(f"Profit: {profit:.2f} PLN")
    
def get_items(items):
    print(f"{'Name':<15}{'Quantity':<10}{'Unit':<10}{'Unit Price PLN':<15}")
    print(f"{(floor * 4):<15}{(floor * 8):<10}{(floor * 4):<10}{(floor * 15):<15}")
    for item in items:
        print(f"{item['name']:<15}{item['quantity']:<10.2f}{item['unit']:<10}{(item['unit_price']):.2f}")

def load_items_from_csv(file_path = "D:/Konrad/Desktop/codding/kodilla/werehouse_project/werehouse.csv"):
    items.clear()
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = {
                    "name": row["name"],
                    "quantity": float(row["quantity"]),
                    "unit": row["unit"],
                    "unit_price": float(row["unit_price"])
                }
                items.append(item)
        print("Items loaded successfully!")
        
    except FileNotFoundError:
        print("File not found. Starting with default items.")
        return
    
def load_profit_from_csv(file_path = "D:/Konrad/Desktop/codding/kodilla/werehouse_project/profit.csv"):
    sold_itmes.clear()
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = {
                    "name": row["name"],
                    "quantity": float(row["quantity"]),
                    "unit": row["unit"],
                    "unit_price": float(row["unit_price"])
                }
                sold_itmes.append(item)
        print("Profit loaded successfully!")

    except FileNotFoundError:
        print("File not found. Starting with default items.")
        return
    
def export_items_to_csv(file_path = "D:/Konrad/Desktop/codding/kodilla/werehouse_project/werehouse.csv"):
    try:
        with open(file_path, mode='w', newline='') as csvfile:
            fieldnames = ["name", "quantity", "unit", "unit_price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in items:
                writer.writerow(item)
        print("Items saved successfully!")
    except FileNotFoundError:
        print("File not found. Starting with default items.")
        return
    
def export_profit_to_csv(file_path = "D:/Konrad/Desktop/codding/kodilla/werehouse_project/profit.csv"):
    try:
        with open(file_path, mode='w', newline='') as csvfile:
            fieldnames = ["name", "quantity", "unit", "unit_price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in sold_itmes:
                writer.writerow(item)
        print("Profit saved successfully!")
    except FileNotFoundError:
        print("File not found. Starting with default items.")
        return
    
load_items_from_csv()
load_profit_from_csv()

while True:
    prompt = input("What would you like to do? ").strip().lower()
    if prompt == "show":
        get_items(items)
    elif prompt == "add":
        add_item()
    elif prompt == "sell":
        sell_item()
    elif prompt == "show_revenue":
        show_revenue()
    elif prompt == "load":
        load_items_from_csv()
        load_profit_from_csv()
    elif prompt == "save":
        export_items_to_csv()
        export_profit_to_csv()
    elif prompt == "exit":
        print("Exiting the program...")
        exit(0)
    else:
        print("Wrong command. Try again.")

    

            



            

