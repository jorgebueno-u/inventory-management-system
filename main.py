from inventory import Inventory
from product import Product


def display_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add product")
    print("2. View products")
    print("3. Search product")
    print("4. Delete product")
    print("5. Exit")


def add_product(inventory):
    try:
        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        product = Product(
            product_id,
            name,
            category,
            price,
            quantity
        )

        inventory.add_product(product)
        print("Product added successfully.")

    except ValueError:
        print("Invalid input. Please try again.")


def search_product(inventory):
    try:
        product_id = int(input("Enter product ID: "))

        product = inventory.search_product(product_id)

        if product:
            print(product)
        else:
            print("Product not found.")

    except ValueError:
        print("Invalid product ID.")


def delete_product(inventory):
    try:
        product_id = int(input("Enter product ID: "))

        if inventory.delete_product(product_id):
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    except ValueError:
        print("Invalid product ID.")


def main():
    inventory = Inventory()

    while True:
        display_menu()

        option = input("Select an option: ")

        if option == "1":
            add_product(inventory)

        elif option == "2":
            inventory.view_products()

        elif option == "3":
            search_product(inventory)

        elif option == "4":
            delete_product(inventory)

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
