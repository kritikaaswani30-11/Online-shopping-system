# -------------------------------
# ONLINE SHOPPING SYSTEM
# -------------------------------

# Data storage (temporary - no database)
users = {}
products = {
    1: {"name": "Smartphone", "price": 15000},
    2: {"name": "Shoes", "price": 2000},
    3: {"name": "Headphones", "price": 3000},
    4: {"name": "Laptop", "price": 50000}
}

cart = []
current_user = None


# -------------------------------
# 1. REGISTRATION MODULE
# -------------------------------
def register():
    print("\n--- User Registration ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users:
        print("User already exists!")
    else:
        users[username] = password
        print("Registration Successful!")


# -------------------------------
# 2. LOGIN MODULE
# -------------------------------
def login():
    global current_user
    print("\n--- User Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful!")
        current_user = username
    else:
        print("Invalid Username or Password!")


# -------------------------------
# 3. PRODUCT BROWSING MODULE
# -------------------------------
def view_products():
    print("\n--- Available Products ---")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - ₹{details['price']}")


# -------------------------------
# 4. CART & ORDER MODULE
# -------------------------------
def add_to_cart():
    view_products()
    choice = int(input("Enter Product ID to add to cart: "))

    if choice in products:
        cart.append(products[choice])
        print("Product added to cart!")
    else:
        print("Invalid Product ID!")


def view_cart():
    print("\n--- Your Cart ---")
    total = 0
    for item in cart:
        print(f"{item['name']} - ₹{item['price']}")
        total += item['price']

    print("Total Amount: ₹", total)


def place_order():
    if not cart:
        print("Cart is empty!")
    else:
        print("\nOrder placed successfully!")
        cart.clear()


# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    while True:
        print("\n===== ONLINE SHOPPING SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. View Products")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            view_products()
        elif choice == "4":
            if current_user:
                add_to_cart()
            else:
                print("Please login first!")
        elif choice == "5":
            if current_user:
                view_cart()
            else:
                print("Please login first!")
        elif choice == "6":
            if current_user:
                place_order()
            else:
                print("Please login first!")
        elif choice == "7":
            print("Thank you for using Online Shopping System!")
            break
        else:
            print("Invalid choice!")


# Run program
main()
