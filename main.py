from inventory import Inventory
from product import Product


def display_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add product")
    print("2. View products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Save inventory")
    print("7. Export inventory to CSV")
    print("8. Exit")


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

        if inventory.add_product(product):
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


def update_product(inventory):
    try:
        product_id = int(input("Enter product ID: "))

        product = inventory.search_product(product_id)

        if product is None:
            print("Product not found.")
            return

        print("\nCurrent product:")
        print(product)

        print("\nWhat would you like to update?")
        print("1. Price")
        print("2. Quantity")
        print("3. Both")

        option = input("Select an option: ")

        if option == "1":
            price = float(input("Enter new price: "))

            if price < 0:
                print("Price cannot be negative.")
                return

            inventory.update_product(product_id, price=price)

        elif option == "2":
            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

            inventory.update_product(product_id, quantity=quantity)

        elif option == "3":
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative.")
                return

            inventory.update_product(
                product_id,
                price=price,
                quantity=quantity
            )

        else:
            print("Invalid option.")
            return

        print("Product updated successfully.")

    except ValueError:
        print("Invalid input. Please try again.")


def main():
    inventory = Inventory()

    # Load previous inventory
    inventory.load_inventory()

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
            update_product(inventory)

        elif option == "5":
            delete_product(inventory)

        elif option == "6":
            inventory.save_inventory()
            print("Inventory saved successfully.")

        elif option == "7":
            inventory.export_to_csv()
            print("Inventory exported to CSV successfully.")

        elif option == "8":
            inventory.save_inventory()
            print("Inventory saved. Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
