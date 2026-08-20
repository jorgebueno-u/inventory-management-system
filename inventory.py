import json
import csv

from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            print("A product with this ID already exists.")
            return False

        self.products.append(product)
        return True

    def view_products(self):
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            print(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def delete_product(self, product_id):
        product = self.search_product(product_id)

        if product is None:
            return False

        self.products.remove(product)
        return True

    def update_product(self, product_id, price=None, quantity=None):
        product = self.search_product(product_id)

        if product is None:
            return False

        if price is not None:
            product.update_price(price)

        if quantity is not None:
            product.update_quantity(quantity)

        return True

    def save_inventory(self, filename="inventory.json"):
        data = [product.to_dict() for product in self.products]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_inventory(self, filename="inventory.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.products = [
                Product.from_dict(product)
                for product in data
            ]

        except FileNotFoundError:
            self.products = []

    def export_to_csv(self, filename="inventory.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Product ID",
                "Name",
                "Category",
                "Price",
                "Quantity"
            ])

            for product in self.products:
                writer.writerow([
                    product.product_id,
                    product.name,
                    product.category,
                    product.price,
                    product.quantity
                ])
