
# POS_SYSTEM
## Tech & Electronics POS System (Python Terminal Based)

# Goals Objective of the Program

This project allows practice building an interactive terminal application simulating a retail check-out system for an electronics shop. It supports browsing products, adding/removing items to/from the shopping cart, checking out with tax and discounts, generating receipts, and providing low-stock alerts. The attempt was made to use only core Python constructs such as lists, dictionaries, conditionals, and functions ensuring all features are implemented within a single file.

## Instructions to Follow Run the Program

**Requirements**

Make sure that Python 3.x is available on your machine.

**Procedure to Follow Run**

Download or copy the project files to your desired local folder in your machine.

Open the command terminal or shell.

Run the file by executing:

python pos_system.py

Follow the on-screen options to navigate the system.

Modifications Needed if Adapting for Other Uses

In case the system needs to be customized/simplified for a particular business case, the quirks are listed below:

Change the list of products in the code for the business by removing redundant items or adding new ones along with changing their prices and stock quantities.

Modify the tax rate or discount limit in checkout() if the business case requires changeable acceptance policies regarding tax or discounts.

**Control Over Currency Formatting**

The US dollar is currently implemented for payment. Alter formatting.
**Issues and limitations**

## Issues:
•	Users must enter the product names exactly as they appear in the product catalogue.

•	One customer is served at a time (meaning no concurrent sessions).

•	It is not permitted to sell a product in fractional–partial quantities. Only whole units can be sold.

•	Sales tax is a constant rate of 15% and discounts 5% if the purchase exceeds $5000.

## Limitation:
•	The program does not have any editable persistent data storage meaning that the inventory resets when the program ends.

•	There is no inventory restocking mechanism either, nor is there an admin panel.

•	The application does not have a GUI and is solely command-line based.

•	Anything not displayed in the terminal is not logged, including printed transaction history.

•	The program features weak input validation such as assuming that users input valid product names of the correct format and number.

________________________________________
## Features
## 1. Product Catalog
•	Displays a comprehensive tech product range including their names, prices, and available stock.
## 2. Add to Cart
•	Product name and quantity is entered by the user.
•	Confirm availability and all stock caps before augmenting the cart.
•	Automatic decrement of stock reserve is done for each sold product.
## 3. Remove from Cart
•	Removes specified product from the cart if it exists.
## 4. View Cart
•	Displays detailed cart breakdown including product titles, number of items purchased, their individual prices, and overall total.
## 5. Checkout Process
•	Calculates the sum of all the item's costs without tax applied to them.
•	Gives a 5% discount if the subtotal is more than $5000.
•	Check value of amount given, calculate change.
•	Generates final receipt.
## 6. Receipt Generation
•	Receipt includes Date/Time, product details, subtotal, tax, total, amount paid, and change over is printed and provided to customer.
## 7. Low Stock Alerts
•	Notifies if any product is at lesser than 5 remaining pieces after the checkout.
## 8. Cancel Order
•	Allows the user clear the cart prior to the final amount checkout.
## 9. Exit Program
•	Closes the program after the users  confirmation.
________________________________________
Summary
The educational based POS system is created for small shops needing basic sales and inventory management, though it can be improved with database integration, GUI support, or file handling.

