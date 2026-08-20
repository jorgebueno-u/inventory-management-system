from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

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
