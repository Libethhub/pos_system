import datetime

def product_catalog():
    print("=======================================================")
    print("                Tech and Electronic                ")
    print("                   retail system                ")
    print("=======================================================")
    print("---------------------Product Catalog-------------------")
    for idx, item in enumerate(products, start=1):
        print(f"{idx}. {item['name']} - ${item['price']:.2f} (Stock: {item['stock_quantity']})")
    print("-------------------------------------------------------")

# Creating a predefined product catalog using a list with name, price, and available quantity
products = [
    {"name": "Samsung- Galaxy A16 5G 128GB", "price": 199.99, "stock_quantity": 70},
    {"name": "HP Envy Printer", "price": 20.0, "stock_quantity": 80},
    {"name": "Apple iPhone 15", "price": 950, "stock_quantity": 30},
    {"name": "Air Cooler Fan", "price": 135, "stock_quantity": 15},
    {"name": "Air Purifier", "price": 450, "stock_quantity": 20},
    {"name": "Ice Maker", "price": 130, "stock_quantity": 40},
    {"name": "Gaming Mouse Pad", "price": 150, "stock_quantity": 15},
    {"name": "15 Laptop Backpacks", "price": 120, "stock_quantity": 20},
    {"name": "Apple AirPods Max", "price": 494.99, "stock_quantity": 20},
    {"name": "Playstation 5", "price": 466.99, "stock_quantity": 40}
]

# Show catalog at the start
product_catalog()

# Adding a shopping cart dictionary
cart = {}

# Search_product function
def search_product(product_name):  # Allows the user to search for the name of the product
    for product in products:  # Using a loop in the dictionary
        if product["name"].lower() == product_name.lower():  # Eliminates invalid inputs .lower()
            return product  # If the product is found
    return None  # If the product is not found

# Add to cart
def put_in_cart(product_name, quantity):  # Parameters that allow the user to add and select the product
    product = search_product(product_name)  # Search_item function
    if not product:
        print(f"Note: {product_name} is not available.")  # Applying the f-string and stating stock unavailability
        return
    if product["stock_quantity"] < quantity:  # Checks the quantity of the product
        print(f"The remaining supply of {product_name} is {product['stock_quantity']} units.")  # Applying the f-string
        return

    if product_name in cart:  # Allow the user to add to the cart
        cart[product_name] += quantity  # Adds new amount to the quantity
    else:
        cart[product_name] = quantity  # Adds product with quantity to cart
    product["stock_quantity"] -= quantity  # Updates the stock after adding to cart
    print(f"{quantity} x '{product_name}' was successfully added to the cart.")  # Confirming the addition

# Remove from cart function
def delete_in_cart(product_name):  # Parameters that allow the user to delete the product
    if product_name in cart:
        del cart[product_name]
        print(f"❌ {product_name} removed from cart.")
    else:
        print(f"{product_name} is not in the cart.")  # Informs if product is not in the cart

# View cart function
def view_cart():
    if not cart:  # Checks the cart dictionary
        print("The cart is empty.")
        return
    print("====Cart====")
    total_amount = 0
    for product_name, quantity in cart.items():  # Helps display an itemized list with numbered entries
        product = search_product(product_name)  # Retrieve product information
        if product:
            item_price = product["price"]
            subtotal = item_price * quantity
            total_amount += subtotal  # Adds to total amount
            print(f"{product_name}")
            print(f"Quantity: {quantity}")
            print(f"Price per unit: ${item_price:.2f}")
            print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")

# Receipt function
def receipt(subtotal=0.0, tax=0.0, total=0.0, received=0.0, change_due=0.0):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date and time
    print("\n\n*******************Best Buy Co., Inc*******************       ")
    print("                 601 Penn Ave S, Richfield,                       ")
    print("                      Minnesota, 55423                           ")
    print("                    Tel: 1-612-291-1000                           ")
    print("=======================Sales receipt===============================")
    print(f"{date}")
    for product_name, quantity in cart.items():
        product = search_product(product_name)
        if product:
            price = product["price"]
            line_total = price * quantity
            print(f"Description                 | Quantity           | Amount ")
            print(f"{product_name}| @ {quantity} ${price:.2f}        |= ${line_total:.2f}")
    print("------------------------------------------------------------------")
    print(f"                                Subtotal:         ${subtotal:.2f}")
    print(f"                                Sales Tax:        ${tax:.2f}")
    print(f"                                Total:            ${total:.2f}")
    print(f"                                Amount Paid:      ${received:.2f}")
    print(f"                                Change:           ${change_due:.2f}")
    print("-----------------------------------------------------------------")
    print("*******************Thank you for shopping with us!****************\n\n\n")

# Check low stock
def check_low_stock():
    for product in products:
        if product["stock_quantity"] < 5:
            print(f"⚠️ Low stock alert: {product['name']} has only {product['stock_quantity']} left!")

# Checkout function
def checkout():
    if not cart:  # Checks the cart dictionary
        print("The cart is empty.")
        return
    subtotal = 0
    for product_name, quantity in cart.items():
        product = search_product(product_name)
        if product:
            subtotal += product["price"] * quantity

    # Apply discount for large orders
    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.05
        print(f"Discount (5%): -${discount:.2f}")
        subtotal -= discount  # Apply discount to subtotal

    # Apply tax
    tax_rate = 0.15
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"Subtotal after discount: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    # Process payment
    while True:
        try:
            received = float(input("Enter amount received from customer: $"))
            if received < total:
                print("--------Not enough funds-----")
            else:
                change_due = received - total
                receipt(subtotal, tax, total, received, change_due)
                cart.clear()  # Clear the cart after purchase
                check_low_stock()  # Check for low stock after purchase
                break
        except ValueError:
            print("Please enter a valid number.")

# Menu option
while True:
    print("***POS Menu option🔢📜****")
    print("1️⃣ Add to cart")
    print("2️⃣ Remove from cart")
    print("3️⃣ View cart")
    print("4️⃣ Checkout")
    print("5️⃣ Cancel Order")
    print("6️⃣ Exit")

    selection = input("Please select the number of your choice: ")

    if selection == "1":
        name = input("Enter the name of the product you want to add: ").strip()
        try:
            quantity = int(input("Please enter the quantity: "))
            put_in_cart(name, quantity)
        except ValueError:
            print("Please enter a valid number")  # Ensure quantity input is valid
    elif selection == "2":
        name = input("Enter the product name to remove: ").strip()
        delete_in_cart(name)
    elif selection == "3":
        view_cart()
    elif selection == "4":
        checkout()
    elif selection == "5":
        cart.clear()  # Clear the cart if user cancels the order
        print("Order has been canceled. Your cart is now empty.")
    elif selection == "6":
        answer = input("⚠ You choose to exit. Are you sure? \n✅ Y for yes OR ❌ N for No: ")
        if answer.lower() == 'y':
            print("Goodbye")
            break
        else:
            continue
    else:
        print("Invalid input. Please enter a number from 1 to 6.")
