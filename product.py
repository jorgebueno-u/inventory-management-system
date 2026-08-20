class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

    def update_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.price = price

    def __str__(self):
        return (
            f"ID: {self.product_id} | "
            f"Name: {self.name} | "
            f"Category: {self.category} | "
            f"Price: ${self.price:.2f} | "
            f"Quantity: {self.quantity}"
        )
