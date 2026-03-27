import csv

def add_product():
    """
    1) valid = 0 / while valid != 1 ensures the user enters a valid value before continuing
    """
    
    valid = 0
    while valid != 1:
        name = str(input("\n| Enter the product name: ")).capitalize().strip()
        if name == "":
            print("\n>> Name cannot be empty <<")
        else:
            valid = 1

    valid = 0
    while valid != 1:
        try:
            stock = int(input("| Enter the stock: "))
            if stock < 0:
                print("\n>> Stock cannot be negative <<\n")
            else:
                valid = 1
        except ValueError:
            print("\n>> Error: Stock must be an integer <<\n")

    valid = 0
    while valid != 1:
        try:
            unit_price = float(input("| Enter the unit price: $"))
            if unit_price < 0:
                print("\n>> Price cannot be negative <<\n")
            else:
                valid = 1
        except ValueError:
            print("\n>> Error: Price must be a number <<\n")
    
    product_and_more = {"Name": name, "Stock": stock, "Unit_price": unit_price} 
    print(f"\n| Product registered successfully")
    return product_and_more 
    # The variable product_and_more returns the product dictionary to be used outside


def calculate_statistics(inventory):
    """
    1) if not inventory validates if the list is empty before calculating
    """
    # If the inventory is empty, print this:
    if not inventory:
        print("\n>> Inventory is empty. <<\n")
        return
 
    subtotal = lambda p: p["Unit_price"] * p["Stock"]   # Lambda to calculate subtotal for each product
    total_units = sum(p["Stock"] for p in inventory) 
    # Sums the quantity of products to validate total items in inventory
    total_value = sum(subtotal(p) for p in inventory) 
    # Sums all subtotals to get total inventory value
    most_expensive_product = max(inventory, key=lambda p: p["Unit_price"]) 
    # Finds the most expensive product
    highest_stock_product = max(inventory, key=lambda p: p["Stock"]) 
    # Finds the product with highest stock
  
    print("\n" + "=" * 40)
    print("INVENTORY STATISTICS")
    print("=" * 40)
    print(f"Total units in stock : {total_units}")
    print(f"Total inventory value : ${total_value:,.2f}")
    print(f"Most expensive product : {most_expensive_product['Name']} (${most_expensive_product['Unit_price']:,.2f})")
    print(f"Highest stock : {highest_stock_product['Name']} ({highest_stock_product['Stock']} units)")
    print("-" * 40)
    print("  Subtotals per product:")
    for p in inventory:
        print(f"  >> {p['Name']} = ${subtotal(p):,.2f} ")
    print("=" * 40 + "\n")


def export_csv(warehouse):
    """
    1) export_csv is the function responsible for exporting the warehouse list,
       which contains product dictionaries and their attributes
    """
    
    with open("warehouse.csv", "w", newline="", encoding="utf-8") as file:
        # Creates the file for writing and closes it automatically
        fields = ["Name", "Stock", "Unit_price"]
        writer = csv.DictWriter(file, fieldnames=fields)
        # Writes CSV files from dictionaries matching keys with headers
        
        writer.writeheader()        # Writes headers
        writer.writerows(warehouse) # Writes all products
    print("Inventory saved to warehouse.csv")


def import_csv(warehouse):

    try:
        with open("warehouse.csv", "r", newline="", encoding="utf-8") as file: 
        # Opens the file for reading and closes automatically
            
            reader = csv.DictReader(file)
            warehouse.clear() # Clears current list
            for row in reader:
                warehouse.append({
                    "Name": row["Name"],
                    "Stock": int(row["Stock"]), 
                    # CSV stores everything as text, must convert
                    "Unit_price": float(row["Unit_price"]) 
                })
        print(f"Inventory loaded: {len(warehouse)} products.")
    except FileNotFoundError:
        print("warehouse.csv file not found")
