class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Create a Product object
p = Product(100)

# Access the price using the getter
print("Price:", p.price)

# Update the price using the setter
p.price = 150
print("Updated Price:", p.price)

# Delete the price using the deleter
del p.price
# Try to access again (this will raise an AttributeError if uncommented)
# print(p.price)
